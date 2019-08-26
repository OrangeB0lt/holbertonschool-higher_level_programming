#!/usr/bin/python3
''' searches for string through the star wars api  '''
import requests
from sys import argv


if __name__ == "__main__":
    param = {'search': argv[1]}
    url = "https://swapi.co/api/people"
    reqst = requests.get(url, params=param)
    people = reqst.json()
    print("Number of results: {}".format(people.get('count')))
    for person in people.get('results'):
        print(person.get('name'))