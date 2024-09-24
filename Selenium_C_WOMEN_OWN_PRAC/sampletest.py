from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
print("Sample Test case Started!!!!")
#Chrome Driver
driver=webdriver.Chrome()
#Maximize the windows size
driver.maximize_window()

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.close()
