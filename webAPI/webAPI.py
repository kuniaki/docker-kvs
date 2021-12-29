import requests
import json

apiurl = 'http://asahitestapp.eastus.cloudapp.azure.com'

def getAll():
    return requests.get(apiurl+'/api/v1/keys/').json()

def get(key):
    return requests.get(apiurl+'/api/v1/keys/'+key).json()

def post(key, value):
    return requests.post(apiurl+'/api/v1/keys/'+key, value).json()

def put(key, value):
    return requests.put(apiurl+'/api/v1/keys/'+key, value).json()

def delete(key):
    return requests.delete(apiurl+'/api/v1/keys/'+key).json()


def main():
    line = ''
    while (line.lower() != 'quit'):
        line = input()
        ll = line.split(' ')
        if ll[0].lower() == 'get':
            if len(ll) == 1:
                print(getAll())
            else:
                print(get(ll[1]))
        elif ll[0].lower() == 'post':
            print(post(ll[1], ll[2]))
        elif ll[0].lower() == 'put':
            print(put(ll[1], ll[2]))
        elif ll[0].lower() == 'delete':
            print(delete(ll[1]))
        elif ll[0].lower() != 'quit':
            print("invalid input")

if __name__ == '__main__':
    main()

