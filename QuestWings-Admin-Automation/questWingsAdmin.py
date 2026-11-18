from selenium import webdriver
import login
import categories_actions
import logout
from config import category_name,category_name1
import questWings_redirections

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(10)


questWings_redirections.url(driver)
login.login(driver)
questWings_redirections.categories(driver)
categories_actions.pagination(driver, 25)
categories_actions.add_category(driver,category_name)
categories_actions.search_category(driver,category_name)
categories_actions.edit_category(driver,category_name1)
categories_actions.search_category(driver,category_name1)
categories_actions.delete_category(driver)
categories_actions.search_category(driver,category_name1)
categories_actions.search_category(driver,category_name)
logout.logout(driver)