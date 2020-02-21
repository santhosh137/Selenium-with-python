"""

Agenda

Basic webdriver commands

Capture title of the page

capture URL of the page

Closing  and quitting browsers



"""

import time

from  selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://github.com/santhosh137/Selenium-with-python")

print (driver.title)

print (driver.current_url)

print (driver.find_element_by_xpath('//*[@id="540d8e1d69d56561bf1d69d926179b5c-2146a756997ebad87cf67c26b8cabb4ba5e55163"]').click())

time.sleep(10)

driver.close()


