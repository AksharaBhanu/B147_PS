#using attribute in xpath
#/tag[@AN='AV']
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver=Chrome()

driver.get("https://aksharatraining.com/sample2.html")


driver.find_element(By.XPATH,"/html/body/a[@href='http://www.fb.com']").click()

time.sleep(2)