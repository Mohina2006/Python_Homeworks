import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

# Scrape the webpage
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

job_cards = soup.find_all('div', class_='card-content')

# Connect to SQLite and create table if not exists
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_link TEXT,
        UNIQUE(title, company, location)
    )
''')
conn.commit()

new_jobs = 0
updated_jobs = 0

# Scrape and insert/update each job
for job in job_cards:
    parent_article = job.find_parent('div', class_='card')
    footer = parent_article.find('footer', class_='card-footer')
    link_tag = footer.find('a') if footer else None
    apply_link = link_tag['href'] if link_tag else "No link found"

    title = job.find('h2', class_='title').text.strip()
    company = job.find('h3', class_='subtitle').text.strip()
    location = job.find('p', class_='location').text.strip()
    description = job.find('div', class_='content').text.strip()

    # Check if job exists
    cursor.execute('''
        SELECT id, description, apply_link FROM jobs
        WHERE title = ? AND company = ? AND location = ?
    ''', (title, company, location))
    existing = cursor.fetchone()

    if existing:
        job_id, old_desc, old_link = existing
        if description != old_desc or apply_link != old_link:
            cursor.execute('''
                UPDATE jobs SET description = ?, apply_link = ?
                WHERE id = ?
            ''', (description, apply_link, job_id))
            updated_jobs += 1
    else:
        cursor.execute('''
            INSERT OR IGNORE INTO jobs (title, company, location, description, apply_link)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, company, location, description, apply_link))
        new_jobs += 1

conn.commit()
print(f"{new_jobs} new jobs added.")
print(f"{updated_jobs} existing jobs updated.")

# --------------- Filtering and Exporting ----------------

# You can change these filters
filter_location = "New York"      # Set to None to disable
filter_company = None             # Set to company name or None

query = "SELECT title, company, location, description, apply_link FROM jobs WHERE 1=1"
params = []
if filter_location:
    query += " AND location = ?"
    params.append(filter_location)
if filter_company:
    query += " AND company = ?"
    params.append(filter_company)

cursor.execute(query, params)
filtered_jobs = cursor.fetchall()

# Function for CSV Export
def export_to_csv(jobs_data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Company', 'Location', 'Description', 'Apply Link'])
        writer.writerows(jobs_data)
    print(f"Exported {len(jobs_data)} filtered job(s) to {filename}")

# Call the function
csv_filename = "filtered_jobs.csv"
export_to_csv(filtered_jobs, csv_filename)

conn.close()
