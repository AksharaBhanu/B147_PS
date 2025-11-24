import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://aksharatraining.com/sample1.html")

time.sleep(2)
element=driver.find_element(By.TAG_NAME,'a')
# print(type(element))
element.click()

time.sleep(3)