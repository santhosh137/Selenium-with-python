"""
Agenda

Conditional commands

is_displayed()

is_enabled()

is_selected()

Certain elements are displayed orr not
Certain elements are enabled or not
Certain elements are selected or not

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://www.facebook.com/")

ele=driver.find_element_by_name("email")\

print (ele.is_displayed())

print (ele.is_enabled())

ele1=driver.find_element_by_name("pass")\

print(ele1.is_displayed())

print(ele1.is_enabled())



