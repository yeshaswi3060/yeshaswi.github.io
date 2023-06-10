from selenium import webdriver
import time 
import requests

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
input('please scan the QR code and press enter')
time.sleep(20)

driver.find_element_by_xpath("//span[@title = 'chat name']").click()
image_element = driver.find_element_by_xpath("//div[@class = 'copyable-text']//img")
with open('img.jpg', 'wb') as f:
    f.write(requests.get(image_element.get_attribute('src')).content)

driver.quit()
