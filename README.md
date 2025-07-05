# 🥤 Woolworths NZ Energy Drink Scraper

A Python web scraper that fetches energy drink listings from [Woolworths New Zealand](https://www.woolworths.co.nz), extracts prices per liter, and displays a **sorted list of the cheapest drinks**—with **brand filtering** and **no duplicates**.

---

## 🚀 Features

- ✅ Scrapes product names, sizes, and prices
- ✅ Filters out duplicate drinks by brand + size
- ✅ Sorts drinks by unit price ($/L)
- ✅ Uses Firefox in headless mode with Selenium + GeckoDriver
- ✅ Supports `.env` file for secure driver path setup
- ✅ Clean, modular Python code structure

---

## 🧰 Requirements

- Python 3.7+
- Firefox Browser
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (Mozilla Public License 2.0)

### Install Python Dependencies

```bash
pip install selenium beautifulsoup4 lxml python-dotenv

🛠️ Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/webscraper.git
cd webscraper

2. Download and Setup GeckoDriver

    Download GeckoDriver from here

    Extract and place geckodriver.exe in the scraper2/ folder or somewhere in your system PATH

3. Configure .env

Create a .env file in the root of the project:

GECKO_PATH=C:/Users/xndmo/Desktop/webscraper/scraper2/geckodriver.exe

    ✅ This keeps your path private and avoids sharing it on GitHub.

📂 Project Structure

webscraper/
├── scraper2/
│   ├── main.py              # Main script to run the scraper
│   ├── filter_drinks.py     # Filtering and deduplication logic
│   └── geckodriver.exe      # WebDriver (ignored by Git)
├── .env                     # Your local GeckoDriver path (ignored)
├── .gitignore               # Ignore geckodriver.exe, .env, etc.
└── README.md                # This file

💡 Usage

python scraper2/main.py

Example output:

rockstar energy drink tropical guava Can 500mL: $4.60/1L
mother energy drink rainbow sherbet Can 500mL: $4.80/1L
...

🛡️ Licensing Notes

    GeckoDriver is licensed under the Mozilla Public License 2.0

    All code in this repo is under the MIT License unless otherwise specified

📬 Contact

Have questions or want to contribute? Feel free to open an issue or reach out!


---

Let me know if you want me to generate badges (e.g., Python version, License, GitHub stars) or if 
