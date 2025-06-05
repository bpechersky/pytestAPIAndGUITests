import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
   # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("pytest")
    search_box.submit()
    assert "pytest" in driver.page_source