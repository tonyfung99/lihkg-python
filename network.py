import hashlib
import requests
import time

common_header = {
    'X-LI-DEVICE': '7137b91d34c213695cf29dc3da2a8f5a95c3b976',
    'X-LI-DEVICE-TYPE': 'android',
    'User-Agent': 'LIHKG/16.0.4 Android/9.0.0 Google/Pixel XL',
    'orginal': 'https://lihkg.com',
    'referer': 'https://lihkg.com/category/1' 
}

device_sha1 = '7137b91d34c213695cf29dc3da2a8f5a95c3b976' # need to be generated
device_type = 'android'
agent = 'LIHKG/16.0.4 Android/9.0.0 Google/Pixel XL'

# Functions
#  
def digest(time, token, url):
    content = 'jeams$get$%s$$%s$%d' % (url, token, time)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

# print(digest(time, token, url))

def request(url, t = None):
    timestamp = int(time.time())
    auth_header = {}

    if t != None :
        auth_header = {
            'X-LI-REQUEST-TIME': str(timestamp), 
            'X-LI-USER':'49970', 
            'X-LI-DIGEST': digest(timestamp, t, url)
        }
    headers = {**common_header, **auth_header}
    # print(headers)
    r = requests.get(url, headers = headers)
    # print(r.json())
    return r
    

def getToken(email, password):
    
    r = requests.post('https://lihkg.com/api_v2/auth/login', headers=common_header, data={'email': email, 'password':password})
    
    if r.json()['success'] == 0:
        print(r.json()['error_message'])
    else:
        print(r.json()['response']['user']['nickname'])

    return r.json()['response']['token']
