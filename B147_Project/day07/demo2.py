from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

subject=input("Please enter the subject(Java/SQL)")

driver=Chrome()
driver.get("https://aksharatraining.com/sample5.html")
xp=f"//td[text()='{subject}']/../td[2]"
print(xp)
cost=driver.find_element(By.XPATH,xp).text
print('cost of ',subject,' is ',cost)
