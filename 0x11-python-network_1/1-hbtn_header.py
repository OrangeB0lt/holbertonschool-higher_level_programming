#!/usr/bin/python3
''' displays X-Request-Id in header of response '''
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    URL = argv[1]
    with urllib.request.urlopen(URL) as request:
        print(response.getheader('X-Request-Id'))
