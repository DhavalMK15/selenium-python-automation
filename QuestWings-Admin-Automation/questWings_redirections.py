import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def url(driver):
    driver.get("https://dk.questwing.com/login")
    time.sleep(1.5)

def categories(driver):
    driver.find_element(By.XPATH, "//*[contains(text(),'Categories')]").click()
    print("Categories fetched successfully")
    time.sleep(1.5)