from bs4 import BeautifulSoup

html_doc = '''<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>
</body>
</html>'''

# Parse the HTML
soup = BeautifulSoup(html_doc, "html.parser")
rows = soup.find_all('tr')[1:]  # skip header row

# Extract data
forecast = []
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    forecast.append({'day': day, 'temp': temp, 'condition': condition})

# Display Weather Data
print("5-Day Forecast:")
for entry in forecast:
    print(f"{entry['day']}: {entry['temp']}°C, {entry['condition']}")

# Find Highest Temperature
max_temp = max(entry['temp'] for entry in forecast)
hottest_days = [entry['day'] for entry in forecast if entry['temp'] == max_temp]
print(f"\nDay(s) with the highest temperature ({max_temp}°C): {', '.join(hottest_days)}")

# Find Sunny Days
sunny_days = [entry['day'] for entry in forecast if entry['condition'].lower() == "sunny"]
print(f"Day(s) with Sunny condition: {', '.join(sunny_days)}")

# Calculate Average Temperature
temperatures = [entry['temp'] for entry in forecast]
avg_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature of the week: {avg_temp}°C")
