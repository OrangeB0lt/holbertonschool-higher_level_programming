#!/usr/bin/python3
''' displays X-Request-Id in header of response '''
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(request.Request(argv[1])) as response:
        print(response.header.get('X-Request-Id'))
