import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def categories_list(driver):

    driver.find_element(By.XPATH,"//*[contains(text(),'Categories')]").click()
    print("Categories fetched successfully")
    time.sleep(1.5)

def add_category(driver,category_name):

    driver.find_element(By.XPATH,"//*[contains(text(),'Add')]").click()
    time.sleep(1.5)
    driver.find_element(By.ID,"title").send_keys(category_name)
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Category added successfully")
    time.sleep(1.5)

def search_category(driver,category_name):

    driver.find_element(By.XPATH, "//input[@placeholder='Search']").clear()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys(category_name)
    time.sleep(1.5)

def edit_category(driver,category_name1):

    driver.find_element(By.XPATH, "//button[@aria-label='Edit']").click()
    time.sleep(1.5)
    driver.find_element(By.ID,"title").clear()
    time.sleep(1.5)
    driver.find_element(By.ID,"title").send_keys(category_name1)
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    print("Category updated successfully")
    time.sleep(1.5)

def delete_category(driver):

    driver.find_element(By.XPATH, "//button[@aria-label='Delete']").click()
    time.sleep(1.5)
    driver.find_element(By.XPATH, "//*[contains(text(),'Delete')]").click()
    print("Category deleted successfully")
    time.sleep(1.5)

def pagination(driver, paging_limit):
    driver.find_element(By.NAME, "category-dt_length").click()
    dropdown = Select(driver.find_element(By.NAME, "category-dt_length"))
    dropdown.select_by_value(str(paging_limit))
    print(f"Page limit is {paging_limit}")
    time.sleep(1.5)
