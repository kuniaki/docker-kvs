import os
from requests import get, post, put, delete

##APP_HOST = os.environ['APP_HOST']
##APP_PORT = int(os.environ['APP_PORT'])
##BASEURL = 'https://{}:{}'.format(APP_HOST, APP_PORT)
BASEURL = 'https://www.jenkinsdev.net'

################
## index.html ##
################

def test_index1():
  r = get(f'{BASEURL}/')
  assert r.status_code == 200

def test_index2():
  r = get(f'{BASEURL}/index.html')
  assert r.status_code == 200


#############
## favicon ##
#############

def test_favicon():
  r = get(f'{BASEURL}/static/favicon.png')
  assert r.status_code == 200


#########
## css ##
#########

def test_css_bootstrap():
  r = get(f'{BASEURL}/static/css/bootstrap-4.3.1.min.css')
  assert r.status_code == 200


#########
## js ##
#########

def test_js_jquery():
  r = get(f'{BASEURL}/static/js/jquery-2.2.4.min.js')
  assert r.status_code == 200

def test_js_bootstrap_bundle():
  r = get(f'{BASEURL}/static/js/bootstrap-4.3.1.bundle.min.js')
  assert r.status_code == 200

def test_js_bootstrap():
  r = get(f'{BASEURL}/static/js/bootstrap-4.3.1.min.js')
  assert r.status_code == 200

def test_js_mykvs():
  r = get(f'{BASEURL}/static/js/kvs.js')
  assert r.status_code == 200

