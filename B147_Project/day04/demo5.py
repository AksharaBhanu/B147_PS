import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#open the browser
driver=Chrome()
#enter the url
driver.get("https://pos.aksharatraining.in/pos/public/#")
#enter username
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("admin")
#enter password
driver.find_element(By.CSS_SELECTOR,'#input-password').send_keys("pointofsale")
#click on go button
driver.find_element(By.CSS_SELECTOR,"button[name='login-button']").click()
#wait and print the title
time.sleep(3)
print(driver.title)

#close the browser
driver.close()