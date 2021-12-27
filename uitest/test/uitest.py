import os, sys, time, datetime, requests, json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import UnexpectedAlertPresentException


WEB_HOST = os.environ['WEB_HOST']
WEB_PORT = int(os.environ['WEB_PORT'])
WEBURL = f'http://{WEB_HOST}:{WEB_PORT}/'


def test_get_success_nokey():
  clean_and_add_keys()
  try:
    (driver, elems) = get_driver_elements()
    elems['get-button'].click()
    time.sleep(1)
    test_name = sys._getframe().f_code.co_name
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
  options = Options()
  o = Options()
  o.binary_location = '/usr/bin/chromium-browser'
  o.add_argument('--headless')
  o.add_argument('--disable-gpu')
  o.add_argument('--no-sandbox')
  o.add_argument('--window-size=1200x600')
  driver = webdriver.Chrome(chromedriver_path, options=o)
  WEBURL = 'http://asahihdgrjenkinsslave1.eastus.cloudapp.azure.com'
  driver = driver.get(WEBURL)
  elements = {}
  for html_id in ['key', 'value', 
                 'get-button', 'post-button', 'put-button', 'delete-button',
                 'request-url', 'request-body', 'response-code', 'response-body']:
    elements[html_id] = driver.find_element_by_id(html_id)
  return (driver, elements)

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
