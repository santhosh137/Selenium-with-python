###imorting the selenium packages to be imported

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

driver.get("https://github.com/santhosh137/Selenium-with-python")
