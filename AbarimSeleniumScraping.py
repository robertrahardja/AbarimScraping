from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Open driver and wait
driver = webdriver.Chrome()

#wait until element is here
#element = WebDriverWait(driver, 10)


#Open Abarim
driver.get("http://www.abarim-publications.com")

element = WebDriverWait(driver, 10)
element = driver.find_element_by_name('search')

#Enter name and search
element.send_keys('Abraham')
element.send_keys(Keys.RETURN)

#Choose name link
element =driver.find_element_by_xpath("//a/b[contains(text(), 'Abraham')]")


#Click name link
element.click()

#Change tab
driver.switch_to_window(driver.window_handles[1])

#Check if page has meaning
check = driver.find_elements_by_xpath("//h2[contains(text(), 'Abraham meaning')]")

#Get elements as list (looks for bold in all article
content = driver.find_elements_by_xpath("//article//b")


#print element text
for item in content:
    print item.text

#close driver
driver.quit()
