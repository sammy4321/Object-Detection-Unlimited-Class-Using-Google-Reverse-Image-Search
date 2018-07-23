import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re


print('Process Started....')
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
driver.get("https://www.google.co.in/imghp?hl=en&tab=wi")
link = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/form/div[2]/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/a")
link.click()
link = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[3]/div/div[2]/form/div[1]/div/a")
link.click()
driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("/home/samarth/Desktop/blii.jpeg")
print('Uploading Image....')
while True:
	url_to_search = driver.current_url
	#print(url_to_search)
	if "search" in url_to_search:
		break
	
print('Almost There....')
url_to_search = driver.current_url
driver.quit()

driver = webdriver.Firefox(firefox_options=options)
driver.get(url_to_search)

html = driver.page_source

soup=BeautifulSoup(html,"html.parser")
aaa = str(soup.findAll("a",{"class":"fKDtNb"})[0])

#print(aaa)
print("Final Result : ",aaa.split(">")[1].split("<")[0])

driver.quit()