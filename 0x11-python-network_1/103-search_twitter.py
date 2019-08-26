#!/usr/bin/python3
''' Uses twitter API to display 5 most recent tweet base on args '''
import requests
import base64
from sys import argv

def encoder(search):
    result = []
    for char in search:
        if char == '#':
            result.append('%23')
        else:
            result.append(char)
    return ''.join(result)


if __name__ == '__main__':

    pub = argv[1]
    secret = argv[2]
    string = str(base64.b64encode(bytes(pub + ':' + secret, 'utf-8')),
                 'utf-8')
    search = argv[3]

    auth_url = 'https://api.twitter.com/oauth2/token'
    headers = {'Authorization': 'Basic ' + string, 'Content-Type':
               'application/x-www-form-urlencoded;charset=UTF-8'}
    body = 'grant_type=client_credentials'
    r = requests.post(auth_url, headers=headers, data=body)
    access_token = r.json().get('access_token')
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    search_url = 'https://api.twitter.com/1.1/search/tweets.json?q={}'.format(
                 search)
    encoded_search_url = encoder(search_url)
    data = requests.get(encoded_search_url, headers=headers).json()
    count = 0
    for status in data.get('statuses'):
        result = '[{}] {} by {}'.format(status.get('id'), status.get('text'),
                                        status.get('user').get('name'))
        print(result)
        count += 1
        if count == 5:
            break