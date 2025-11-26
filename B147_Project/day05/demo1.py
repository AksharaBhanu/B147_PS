import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#open the browser
driver=Chrome()
#enter the url
driver.get("https://pos.aksharatraining.in/pos/public/#")
#enter username
driver.find_element(By.XPATH,"//input[@id='input-username']").send_keys("admin")
#enter password
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("pointofsale")
#click on go button
driver.find_element(By.XPATH,"//button[.='Go']").click()
#wait and print the title
time.sleep(3)
print(driver.title)

#close the browser
driver.close()

#assignment --> write a script to login to below app using xpath and also one more script using css selector
# https://opensource-demo.orangehrmlive.com/web/index.php/auth/login