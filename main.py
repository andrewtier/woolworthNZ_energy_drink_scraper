from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import re
import os
from dotenv import load_dotenv
from filter_drinks import extract_key  # import from separate file
#yo i broke it
options = Options()
options.headless = True

load_dotenv()  # Load environment variables from .env file
gecko_path = os.getenv('GECKO_PATH')
service = Service(executable_path=gecko_path)
driver = webdriver.Firefox(service=service, options=options)

url = 'https://www.woolworths.co.nz/shop/browse/drinks/soft-drinks-sports-drinks/energy-drinks?page=1'
driver.get(url)
time.sleep(5)  # wait for page load

soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()

# Find all product cards
drinks = soup.find_all('cdx-card', class_='cdx-card-cup-adjustment card ng-star-inserted')

seen = set()
drink_list = []

for drink in drinks:
    title_elem = drink.find('h3', id=re.compile(r'product-\d+-title'))
    if title_elem:
        full_title = title_elem.text.strip()
    else:
        full_title = "No Title"

    price_elem = drink.find('span', class_='cupPrice ng-star-inserted')
    if price_elem:
        match = re.search(r'\$(\d+\.\d+)', price_elem.text)
        price = float(match.group(1)) if match else float('inf')
    else:
        price = float('inf')

    key = extract_key(full_title)

    if key not in seen:
        seen.add(key)
        drink_list.append((full_title, price))

# Sort by price ascending
drink_list.sort(key=lambda x: x[1])

# Print results
for title, price in drink_list:
    print(f"{title}: ${price:.2f}/1L")
