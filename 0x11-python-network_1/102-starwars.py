#!/usr/bin/python3
''' takes in string, sends search request to Star Wars API '''
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
            for result in json.get('results'):
                print(result.get('name'))
                for film in result.get('films'):
                    print('\t' + requests.get(film).json().get('title'))
            page += 1
            url = 'https://swapi.co/api/people/?search={}&page={}'.format(
                  search, page)
            json = requests.get(url).json()
    except Exception:
        pass
