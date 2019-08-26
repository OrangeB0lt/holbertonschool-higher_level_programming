#!/usr/bin/python3
''' takes in a string, sends a search request to Star Wars API '''
import requests
from sys import argv


if __name__ == '__main__':

    search = argv[1]
    page = 1
    url = 'https://swapi.co/api/people/?search={}&page={}'.format(search, page)
    json = requests.get(url).json()
    print('Number of results: {}'.format(json['count']))
    try:
        while json.get('count'):
            for result in json['results']:
                print(result['name'])
            page += 1
            url = 'https://swapi.co/api/people/?search={}&page={}'.format(
                  search, page)
            json = requests.get(url).json()
    except Exception:
        pass