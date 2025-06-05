import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_duckduckgo_advanced_interaction(driver):
    driver.get("https://duckduckgo.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

    results = driver.find_elements(By.CSS_SELECTOR, "a.result__a")
    assert len(results) > 0
    results[0].click()
    driver.implicitly_wait(5)

    assert "selenium" in driver.current_url.lower()