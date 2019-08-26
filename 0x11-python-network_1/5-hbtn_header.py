#!/usr/bin/python3
''' shows value of X-Request_Id in response header  '''
import requests
from sys import argv


if __name__ == "__main__":
    reqst = requests.get(argv[1])
    print(reqst.headers.get('X-Request-Id'))
