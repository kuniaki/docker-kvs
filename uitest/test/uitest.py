import os, sys, time, datetime,  json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chrome_path = '/usr/bin/chromium-browser'
chromedriver_path = '/usr/lib/chromium/chromedriver'
o = Options()
o.binary_location = '/usr/bin/chromium-browser'
o.add_argument('--headless')
o.add_argument('--disable-gpu')
o.add_argument('--no-sandbox')
o.add_argument('--window-size=1200x600')

WEB_HOST = os.environ['WEB_HOST']
WEB_PORT = int(os.environ['WEB_PORT'])
WEBURL = f'http://{WEB_HOST}:{WEB_PORT}/'

"""
Sample test
d = webdriver.Chrome(chromedriver_path, options=o)
print(WEBURL)
d.get(WEBURL)
print(d.title)
d.quit()
"""

s = Service(executable_path=chromedriver_path)
s.start()
d = webdriver.Remote(
    s.service_url,
    desired_capabilities=o.to_capabilities()
)
d.get(WEBURL)
print(d.title)
d.quit()

