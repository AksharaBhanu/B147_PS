from selenium.webdriver import Chrome

driver=Chrome()
driver.get("https://aksharatraining.com/") #enter the url (send the url to addressbar)
print(driver.title)
print(driver.current_url) #get the url present in the address bar
print(driver.page_source) #get the html code of the page
driver.close()