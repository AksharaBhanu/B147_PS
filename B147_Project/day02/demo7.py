import time

from selenium.webdriver import Chrome

driver=Chrome()
time.sleep(1)
driver.get("http://www.google.com")
time.sleep(1)
driver.get("http://www.fb.com")
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
time.sleep(1)
driver.quit()
