import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()

driver.get("https://aksharatraining.com/sample2.html")

element=driver.find_element(By.TAG_NAME,'a') #returns 1st matching element

element.click()

time.sleep(3)

