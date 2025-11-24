import time

from selenium.webdriver import Firefox

print('Main Starts')

e=Firefox()
time.sleep(2)
e.close()

print('Main Ends')