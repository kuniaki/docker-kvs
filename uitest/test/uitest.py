import os, sys, time, datetime, requests, json
import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service


WEB_HOST = os.environ['WEB_HOST']
WEB_PORT = int(os.environ['WEB_PORT'])
WEBURL = f'http://{WEB_HOST}:{WEB_PORT}/'
WEBURL = 'http://asahihdgrjenkinsslave1.eastus.cloudapp.azure.com'
APIURL = WEBURL + '/api/v1'

logging.basicConfig(level=logging.DEBUG)
mylogger= logging.getLogger()


def test_get_success_nokey():
  clean_and_add_keys()
  try:
    print("deiver_elements webdriver")
    (driver, elems) = get_driver_elements()
    print("deiver_elements webdriver-1")
    print(driver)
    print("deiver_elements webdriver-2")
    print(driver.title)
    print("deiver_elements webdriver-3")
    elems['get-button'].click()
    time.sleep(1)
    test_name = sys._getframe().f_code.co_name
    mylogger.info(test_name)
    take_screenshot(driver, test_name)
    assert elems['request-url'].text   == '/api/v1/keys/'
    assert elems['request-body'].text  == ''
    assert elems['response-code'].text == '200'
    rbody = json.loads(elems['response-body'].text)
    assert rbody == {'apple':'red', 'banana':'yellow'}
    driver.quit()
  except:
    driver.quit()
    raise

def get_driver_elements():
    chrome_path = '/usr/bin/chromium-browser'
    chromedriver_path = '/usr/lib/chromium/chromedriver'
    o = Options()
    o.binary_location = '/usr/bin/chromium-browser'
    o.add_argument('--headless')
    o.add_argument('--disable-gpu')
    o.add_argument('--no-sandbox')
    o.add_argument('--window-size=1200x600')

    d = webdriver.Chrome(chromedriver_path, options=o)

    WEBURL = 'http://asahihdgrjenkinsslave1.eastus.cloudapp.azure.com'
    d.get(WEBURL)
    elements = {}
    for html_id in ['key', 'value',
                 'get-button', 'post-button', 'put-button', 'delete-button',
                 'request-url', 'request-body', 'response-code', 'response-body']:
     elements[html_id] = d.find_element_by_id(html_id)
    print(d)
    return (d, elements)

def clean():
  r = requests.get(f'{APIURL}/keys/')
  for key in r.json():
    requests.delete(f'{APIURL}/keys/{key}')
  num_keys = len(requests.get(f'{APIURL}/keys/').json())
  assert 0 == num_keys

def clean_and_add_keys():
  clean()
  r = requests.put(f'{APIURL}/keys/apple', data='red')
  assert r.status_code == 200
  r = requests.put(f'{APIURL}/keys/banana', data='yellow')
  assert r.status_code == 200

def take_screenshot(driver, title):
  today = datetime.datetime.today()
  timestamp = today.strftime("%Y%m%d%H%M%S")
  driver.save_screenshot(f'/images/{timestamp}-{title}.png')
