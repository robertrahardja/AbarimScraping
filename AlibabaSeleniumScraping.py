from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Open driver and wait
driver = webdriver.Chrome()


#Open Alibaba
driver.get("https://www.alibaba.com/product-detail/Wholesale-PVC-Free-Rectangular-White-Soft_60520535225.html?spm=a2700.7724838.0.0.hSC9MV")

#switch to frame
driver.switch_to_frame(driver.find_element_by_id("alibaba-login-box"))

usr = driver.find_element_by_id("fm-login-id")
password = driver.find_element_by_id("fm-login-password")

usr.send_keys("robertrahardja@gmail.com")
password.send_keys("4l4b4b4RR")

driver.find_element_by_name("submit-btn").click()


#Choose name link
element =driver.find_element_by_xpath("//div[@class='container-table']")

print element.text
#Click name link
#element.click()


#close driver
driver.quit()
