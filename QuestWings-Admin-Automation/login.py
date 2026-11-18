import time
from selenium.webdriver.common.by import By
from config import EMAIL,PASSWORD

def login(driver):

    driver.find_element(By.ID, "email").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Login successful")
    time.sleep(1.5)
