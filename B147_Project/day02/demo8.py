import time
from selenium.webdriver import Chrome

driver=Chrome()
time.sleep(1)
driver.get("http://www.google.com")
time.sleep(2)
size=driver.get_window_size() #get current size of the browser
print(size)
print(size['width'])
print(size['height'])

driver.set_window_size(400,600) #resize the browser

time.sleep(2)
driver.close()

#write a script to move the browser:position