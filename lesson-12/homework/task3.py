from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time  # Import for sleep

# Basic Chrome setup
chrome_options = Options()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(
    service=Service(r"C:\Users\user\Documents\Apps\chromedriver-win64\chromedriver.exe"),
    options=chrome_options
)
wait = WebDriverWait(driver, 10)

try:
    # Step 1: Homepage with delay
    driver.get("https://www.demoblaze.com")
    time.sleep(2)  # Wait for initial load

    # Step 2: Click Laptops with delay before and after
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops"))).click()
    time.sleep(2)  # Wait for category to load

    # Scrape function with small delay between cards
    def scrape_laptops():
        laptops = []
        cards = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".card-block")))
        for card in cards:
            time.sleep(0.5)  # Small delay between items
            try:
                laptops.append({
                    "name": card.find_element(By.CLASS_NAME, "card-title").text,
                    "price": card.find_element(By.TAG_NAME, "h5").text,
                    "description": ""
                })
            except:
                continue
        return laptops

    # Scrape first page
    all_laptops = scrape_laptops()

    # Try next page with delays
    try:
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.ID, "next2"))).click()
        time.sleep(2)  # Wait for next page load
        all_laptops += scrape_laptops()
    except:
        print("No next page or error clicking")

    # Save data
    with open("laptops.json", "w") as f:
        json.dump(all_laptops, f, indent=4)
    print("Done! Saved to laptops.json")

finally:
    driver.quit()