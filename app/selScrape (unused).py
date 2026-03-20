from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_amazon_price(url):

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
    )
    # 1. Start browser
    driver = webdriver.Chrome(options=options)

    try:
        # 2. Open page
        driver.get(url)

        # 3. Wait for price to load (IMPORTANT)
        wait = WebDriverWait(driver, 10)

        elements = driver.find_elements(By.CSS_SELECTOR, "span.a-price > span.a-offscreen")

        price_text = None

        for el in elements:
            text = el.text.strip()
            if text and "$" in text:
                price_text = text
                break

        if not price_text:
            raise Exception("No valid price found")

        price = float(price_text.replace("$", "").replace(",", ""))
        

        return price

    finally:
        # 6. Always close browser
        driver.quit()