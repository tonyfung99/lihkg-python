
import sys

import os
import util
import network

util.clear() 

# https://lihkg.com/api_v2/thread/category?cat_id=15&page=1&count=60&type=now
def goList(cat_id = 15, page = 1):
    os.system('clear')
    url = 'https://lihkg.com/api_v2/thread/category?cat_id=%d&page=%d&count=%d&type=now' % (cat_id, page, 100)
    r = network.request(url, token)
    items = r.json()['response']['items']
    for item in items:
        print(item['thread_id'], item['title'])

# https://lihkg.com/api_v2/thread/909714/page/1?order=reply_time
def goPost(post_id, page = '1'):
    action = page
    while action != 'b':
        print(action)
        os.system('clear')
        if action == 'n':
            page = str(int(page) + 1)
        elif action == 'r':
            pass
        else:
            page = action

        url = 'https://lihkg.com/api_v2/thread/%s/page/%s?order=reply_time' % (post_id, page)
        resp = network.request(url, token).json()['response']
        print(resp['title'],  resp['page'], '/',  resp['total_page'])
        posts = resp['item_data']
        for post in posts:
            print(post['user_nickname'],':')
            print(post['msg'])
            print('-----------')
        
        if 'me' in resp:
            print('hi,', resp['me']['nickname'])

        current_paging = '%s/%s' % (resp['page'], resp['total_page'])
        action = input('page ' + current_paging + ' / [n]ext / [b]ack / [r]efresh: ')



# Main
#  
token = None

goLogin = input('Login or Not? y/n: ')
# goLogin = 'y'
if goLogin.lower() == 'y':
    email = input('email: ')
    password = input('password: ')
    # email = 'hihi@hihi.com'
    # password = 'xxx'
    token = network.getToken(email, password)
else:
    print('Not Logged in')


for channel in util.CHANNELS: 
    print(channel['id'], channel['name'])


channel_id = int(input(util.highlight('Channel Id: ')))


util.clear()
print(chr(27) + "[2J")


thread_id = None

while thread_id != 'q':
    goList(channel_id)
    thread_id = input('thread_id or quit(q): ')
    goPost(thread_id) 