import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()

driver.get("https://aksharatraining.com/sample1.html")


element=driver.find_element(By.TAG_NAME,'x') #NSEE

element.click()

