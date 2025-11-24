import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#<a id="a1" name="n1" class="c1" title="click me" href="http://www.google.com">Google</a>
#locator no.5--> link text

driver=Chrome()

driver.get("https://aksharatraining.com/sample1.html")

driver.find_element(By.LINK_TEXT,"Google").click()

time.sleep(2)