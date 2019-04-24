#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.firefox.options import Options
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(firefox_options=options, executable_path=r"C:\Users\zcp17\Downloads\geckodriver-v0.24.0-win64 (1)\geckodriver.exe")



import unittest, time, re
from bs4 import BeautifulSoup as bs
from dateutil import parser
import pandas as pd
import itertools
import matplotlib.pyplot as plt


# In[ ]:


##Bot target search information: 
bot_year = '2005'
bot_make = 'Acura'
bot_model = 'TL'
bot_vin = '19UUA65505A000427'
bot_plate = '985 KQR'
year_make_model = '2005 Acura TL'

address = '295 khartoum st se'
city = 'Salem'
state = 'Oregon'
Zip = '97306'

loss_location = '4825 Commercial St SE, Salem, OR 97302'

city_state = city +  " " + state
print(city_state)


# In[ ]:


driver.get('https://www.autocheck.com/vehiclehistory/?siteID=0')
driver.implicitly_wait(5)
search_auto = driver.find_element_by_id('vin')
search_auto.clear()
search_auto.send_keys(bot_vin)

time.sleep(1)
search_auto = driver.find_element_by_id('vin')
search_auto.send_keys(Keys.ENTER)
time.sleep(1)


# In[ ]:


###New Tab Facebook
driver.execute_script("window.open('{}');".format('https://www.facebook.com'))
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
login_fb = driver.find_element_by_xpath('//*[@id="email"]')
login_fb.clear()
login_fb.send_keys('zpelley@my.chemeketa.edu')

time.sleep(1)

pass_fb = driver.find_element_by_id('pass')
pass_fb.clear()
pass_fb.send_keys('mineshaft')

time.sleep(1)

pass_fb = driver.find_element_by_id('pass')
pass_fb.send_keys(Keys.ENTER)


###search marketplace

market_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div/div[3]/div[1]/ul/li[4]/a/div')
market_button.click()

time.sleep(1)
location = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div/div[4]/div[2]/div[2]/span/label/input')
location.clear()
location.send_keys(city_state)
time.sleep(1)
location.send_keys(Keys.ENTER)
time.sleep(1)

###search for vehicle
veh_search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div/div[4]/div/div/span/span/label/input')
veh_search.clear()
veh_search.send_keys(year_make_model)

time.sleep(1)

veh_search.send_keys(Keys.ENTER)


# In[ ]:


##New tab Craigslist
driver.execute_script("window.open('{}');".format('https://www.bing.com/'))

driver.switch_to.window(driver.window_handles[2])
driver.implicitly_wait(5)
search_cl = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
search_cl.clear()
search_cl.send_keys('craigslist ' + '' + city_state)


submit_button_cl = driver.find_element_by_id('sb_form_go')
submit_button_cl.click()

time.sleep(1)

submit_cl_button = driver.find_element_by_xpath('/html/body/div[2]/main/ol/li[1]/div[2]/ul[1]/li[1]/h3/a')
submit_cl_button.click()

time.sleep(1)

owner_button = driver.find_element_by_xpath('/html/body/section/form/div[2]/div/ul/li[2]/a')
owner_button.click()


time.sleep(1)



cl_veh_search = driver.find_element_by_id('query')
cl_veh_search.clear()
cl_veh_search.send_keys(year_make_model)

time.sleep(1)

submit_cl_button = driver.find_element_by_class_name('searchbtn')
submit_cl_button.click()

time.sleep(1)


# In[ ]:


###New tab Google Maps

driver.execute_script("window.open('{}');".format('https://www.google.com/maps'))
driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[3])
search_map = driver.find_element_by_id('searchboxinput')
search_map.clear()
search_map.send_keys(address + ''+ city_state)

time.sleep(1)
search_map = driver.find_element_by_id('searchboxinput')
search_map.send_keys(Keys.ENTER)

time.sleep(1)

direction = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[7]/div[9]/div/div[1]/div/div/div[4]/div[1]/div/button')
direction.click()

time.sleep(1)

loss_loc = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input')
loss_loc.clear()
time.sleep(1)
loss_loc.send_keys(loss_location)

time.sleep(1)

loss_loc.send_keys(Keys.ENTER)

