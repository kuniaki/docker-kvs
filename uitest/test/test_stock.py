import os, sys, time, datetime, requests, json
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service


WEB_HOST = os.environ['WEB_HOST']
WEB_PORT = int(os.environ['WEB_PORT'])
#WEBURL = f'http://{WEB_HOST}:{WEB_PORT}/'
#WEBURL = 'http://asahihdgrjenkinsslave1.eastus.cloudapp.azure.com'
<<<<<<< HEAD
WEBURL = 'https://www.jenkinsdev.net/'
=======
WEBURL = 'https://ckv.ngrok.io/'
>>>>>>> main

def test_click_stock_button():
  try:
    driver = get_driver()
    time.sleep(1)
    driver.find_element_by_id("stock-button").click()
    time.sleep(1)
    driver.find_element_by_id("btn-getinfo").click()
    time.sleep(5)
    take_screenshot(driver, sys._getframe().f_code.co_name)
    driver.quit()
  except:
    driver.quit()
    raise

def get_driver():
    chrome_path = '/usr/bin/chromium-browser'
    chromedriver_path = '/usr/lib/chromium/chromedriver'
    o = Options()
    o.binary_location = '/usr/bin/chromium-browser'
    o.add_argument('--headless')
    o.add_argument('--disable-gpu')
    o.add_argument('--no-sandbox')
    o.add_argument('--window-size=1200x1000')

    d = webdriver.Chrome(chromedriver_path, options=o)

    d.get(WEBURL)
    return d


def take_screenshot(driver, title):
  today = datetime.datetime.today()
  timestamp = today.strftime("%Y%m%d%H%M%S")
  driver.save_screenshot(f'/images/{timestamp}-{title}.png')
