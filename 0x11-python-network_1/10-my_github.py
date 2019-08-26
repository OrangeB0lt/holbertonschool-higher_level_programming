#!/usr/bin/python3
''' script takes github credentials and uses them to display id '''
import requests
from sys import argv


if __name__ == "__main__":
    userId = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2])).json()
    if "id" in userId:
        print(userId['id'])
    else:
        print(None)
