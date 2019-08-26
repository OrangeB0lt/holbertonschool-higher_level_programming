#!/usr/bin/python3
''' send POST request to passed URL with passed in email address '''
import requests
from sys import argv


if __name__ == "__main__":
    reqst = requests.post(argv[1], data={'email': argv[2]})
    print(reqst.text)
