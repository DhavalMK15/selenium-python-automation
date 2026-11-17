from selenium import webdriver
import time
from openpyxl import load_workbook
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Read Excel
workbook = load_workbook("testdata.xlsx")
sheet = workbook.active

# Loop through all rows in Excel
for row in range(2, sheet.max_row + 1):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    address = sheet.cell(row, 1).value
    first_name = sheet.cell(row, 2).value
    last_name = sheet.cell(row, 3).value
    ssn = sheet.cell(row, 4).value
    email = sheet.cell(row, 5).value
    phone = sheet.cell(row, 6).value
    dob = sheet.cell(row, 7).value
    card_holder = sheet.cell(row, 8).value
    card_number = sheet.cell(row, 9).value
    expiry = sheet.cell(row, 10).value
    cvv = sheet.cell(row, 11).value
    zipcode = sheet.cell(row, 12).value

    driver.get("https://devenrollment.uslegalservices.net/enroll?opt=general")

    driver.find_element(By.XPATH, "//button[@aria-label='Close']").click()
    driver.find_element(By.XPATH, "//span[text()='Yourself']").click()
    driver.find_element(By.XPATH, "//span[text()='No']").click()
    driver.find_element(By.XPATH, "//span[text()='Identity Defender']").click()
    driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()

    driver.find_element(By.ID, "address").send_keys(address)
    driver.find_element(By.XPATH, "(//div[contains(@class,'pac-item')])[3]").click()

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "state").get_attribute("value")
    )

    driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()
    driver.find_element(By.XPATH, "(//button[normalize-space()='Select'])[1]").click()
    driver.find_element(By.XPATH, "//button[contains(.,'Proceed To Checkout ')]").click()

    driver.find_element(By.ID, "first_name").send_keys(first_name)
    driver.find_element(By.ID, "last_name").send_keys(last_name)
    driver.find_element(By.ID, "ssn").send_keys(Keys.HOME, str(ssn))
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "phone").send_keys(Keys.HOME, str(phone))
    driver.find_element(By.ID, "date_of_birth").send_keys(Keys.HOME, str(dob))

    driver.execute_script("window.scrollBy(0,300);")

    driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()

    driver.find_element(By.ID, "creditCardHolder").send_keys(card_holder)
    driver.find_element(By.ID, "cc").send_keys(Keys.HOME, str(card_number))
    driver.find_element(By.ID, "exp_month").send_keys(Keys.HOME, str(expiry))
    driver.find_element(By.ID, "ccv").send_keys(Keys.HOME, str(cvv))
    driver.find_element(By.ID, "billingZip").send_keys(Keys.HOME, str(zipcode))

    driver.find_element(By.XPATH, "//button[contains(.,'Next')]").click()

    driver.execute_script("window.scrollBy(0,1400);")
    time.sleep(1)

    driver.find_element(By.XPATH, "//label[contains(.,'Check here to confirm')]").click()
    driver.find_element(By.ID, "eSignature").send_keys("FF")

    # driver.find_element(By.XPATH, "//button[contains(.,'Purchase Plan')]").click()

    print(f"{first_name} {last_name} - Enrollment completed ✅")

    time.sleep(3)
    driver.quit()