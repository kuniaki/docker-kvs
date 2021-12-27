import os, sys, time, datetime, requests, json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException

chrome_path = '/usr/bin/chromium-browser'
chromedriver_path = '/usr/lib/chromium/chromedriver'
o = Options()
o.binary_location = '/usr/bin/chromium-browser'
o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--no-sandbox')
o.add_argument('--window-size=1200x600')

SELENIUM_HUB_HOST = os.environ['SELENIUM_HUB_HOST']
SELENIUM_HUB_PORT = int(os.environ['SELENIUM_HUB_PORT'])
HUBURL = f'http://{SELENIUM_HUB_HOST}:{SELENIUM_HUB_PORT}/wd/hub'

WEB_HOST = os.environ['WEB_HOST']
WEB_PORT = int(os.environ['WEB_PORT'])
WEBURL = f'http://{WEB_HOST}:{WEB_PORT}/'

print("FLOW1")

driver = webdriver.Remote(
            command_executor=HUBURL,
            desired_capabilities=DesiredCapabilities.CHROME)

print("FLOW2")

driver.get(WEBURL)

print("FLOW3")


d = webdriver.Chrome(chromedriver_path, options=o)
print(WEBURL)
d.get('http://127.0.0.1')
print(d.title)
d.quit()

