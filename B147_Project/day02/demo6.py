import time

from selenium.webdriver import Chrome

driver=Chrome()  #open chrome browser
driver.get('http://www.google.com') #enter the url and get the page
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.close()
