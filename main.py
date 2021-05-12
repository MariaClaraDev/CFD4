from selenium import webdriver
from selenium.webdriver.support.ui import Select
 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Bin\chromedriver.exe")
driver.get("https://www.globo.com")

driver.find_element_by_class_name("header-search__input").send_keys("coronavirus" + Keys.RETURN)
driver.implicitly_wait(3) # seconds

print("filters__dropdown__list__right")
