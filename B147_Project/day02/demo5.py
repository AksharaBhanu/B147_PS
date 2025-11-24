import time

#safari-->settings--> developer--> allow remote automation
from selenium.webdriver import Safari

print('Main Starts')

e=Safari()
time.sleep(2)
e.close()

print('Main Ends')