import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def logout(driver):
    driver.find_element(By.CLASS_NAME, "avatar").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//*[contains(text(),'Logout')]").click()
    time.sleep(1.5)

    driver.quit()
    print("Logout successful")
