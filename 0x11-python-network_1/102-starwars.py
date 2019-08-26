#!/usr/bin/python3
''' takes in string, sends search request to Star Wars API '''
import requests
from sys import argv


def request_to_star_wars(the_url, payload):
    """makes a request to input URL with q as a parameter"""
    reqst = requests.get(the_url, params=payload).json()
    name_list = []
    count = reqst.get('count')
    if count > 0:
        results = reqst.get('results')
        for character in results:
            name_list.append(character.get('name'))
    next_page = reqst.get('next')
    while next_page:
        reqst = requests.get(next_page).json()
        results = reqst.get('results')
        for character in results:
            name_list.append(character.get('name'))
        next_page = reqst.get('next')
    print("Number of results: {}".format(count))
    for name in name_list:
        print(name)

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "https://swapi.co/api/people/"
    payload = {'search': sys.argv[1]}
    request_to_star_wars(the_url, payload)