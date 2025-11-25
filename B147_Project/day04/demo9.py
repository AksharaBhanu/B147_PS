import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


driver=Chrome()

driver.get("https://aksharatraining.com/sample1.html")


driver.find_element(By.XPATH,"/html/body/a[text()='Google']").click()

time.sleep(2)