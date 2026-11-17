from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://devenrollment.uslegalservices.net/enroll?opt=general")
driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
driver.find_element(By.XPATH, "//span[text()='Yourself']").click()
driver.find_element(By.XPATH, "//span[text()='No']").click()
driver.find_element(By.XPATH, "//span[text()='Identity Defender']").click()
driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()
driver.find_element(By.ID, "address").send_keys("Florida University")
driver.find_element(By.XPATH, "(//div[contains(@class,'pac-item')])[3]").click()
WebDriverWait(driver, 10).until(lambda d: d.find_element(By.ID, "state").get_attribute("value"))
driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()
driver.find_element(By.XPATH, "(//button[normalize-space()='Select'])[1]").click()
driver.find_element(By.XPATH, "//button[contains(.,'Proceed To Checkout ')]").click()
driver.find_element(By.ID, "first_name").send_keys("Hello")
driver.find_element(By.ID, "last_name").send_keys("World")
driver.find_element(By.ID, "ssn").send_keys(Keys.HOME, "279750789")
driver.find_element(By.ID, "email").send_keys("abcc1107cc@yopmail.com")
driver.find_element(By.ID, "phone").send_keys(Keys.HOME,"7897891899")
driver.find_element(By.ID, "date_of_birth").send_keys(Keys.HOME,"02/03/1999")
driver.execute_script("window.scrollBy(0,300);")
driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()
if driver.find_elements(
    By.XPATH,
    "//*[contains(text(),'We found an existing record with your information')]"
):
    print("User already exists")
    time.sleep(4)
    driver.quit()
    exit()
else:
    driver.find_element(By.ID, "creditCardHolder").send_keys("Yelina")
    driver.find_element(By.ID, "cc").send_keys(Keys.HOME,"4111111111111111")
    driver.find_element(By.ID, "exp_month").send_keys(Keys.HOME,"02/2029")
    driver.find_element(By.ID, "ccv").send_keys(Keys.HOME,"123")
    driver.find_element(By.ID, "billingZip").send_keys(Keys.HOME,"33101")
    driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()
    driver.execute_script("window.scrollBy(0,1400);")
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[contains(.,'Check here to confirm')]").click()
    driver.find_element(By.ID, "eSignature").send_keys("FF")
    # driver.find_element(By.XPATH, "//button[contains(.,'Purchase Plan')]").click()
    time.sleep(2)

driver.quit()
time.sleep(3)

print("Enrolment successful")