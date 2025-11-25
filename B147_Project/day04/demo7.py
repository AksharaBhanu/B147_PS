import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver=Chrome()

driver.get("https://aksharatraining.com/sample2.html")

# driver.find_element(By.XPATH,'/html/body/a').click() #matches with 3, but FE returns 1st

driver.find_element(By.XPATH,'/html/body/a[2]').click() #matches with 2nd link

time.sleep(2)