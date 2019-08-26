#!/usr/bin/python3
''' takes in string, sends search request to Star Wars API '''
import requests
import sys


def request_to_star_wars(the_url, payload):
    """makes a request to input URL with q as a parameter"""
    reqst = requests.get(the_url, params=payload).json()
    results_dict = {}
    name_list = []
    count = reqst.get('count')
    if count > 0:
        results = reqst.get('results')
        for character in results:
            name = character.get('name')
            films = character.get('films')
            name_list.append(name)
            results_dict[name] = films
    next_page = reqst.get('next')
    while next_page:
        reqst = requests.get(next_page).json()
        results = reqst.get('results')
        for character in results:
            name = character.get('name')
            films = character.get('films')
            name_list.append(name)
            results_dict[name] = films
        next_page = reqst.get('next')
    for k, v in results_dict.items():
        films_list = []
        for film in v:
            reqst = requests.get(film).json()
            title = reqst.get('title')
            films_list.append(title)
        results_dict[k] = films_list
    print("Number of results: {}".format(count))
    for name in name_list:
        print(name)
        for title in results_dict[name]:
            print('\t{}'.format(title))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "https://swapi.co/api/people/"
    payload = {'search': sys.argv[1]}
    request_to_star_wars(the_url, payload)