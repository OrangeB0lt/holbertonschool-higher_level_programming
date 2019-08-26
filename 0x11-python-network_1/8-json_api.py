#!/usr/bin/python3
''' sends post request with a given letter as a param  '''
import requests
from sys import argv


if __name__ == "__main__":
    argQuerty = argv[1] if len(argv) > 1 else ""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argQuerty}
    try:
        reqst = requests.post(url, data=data).json()
        if 'id' in reqst and 'name' in reqst:
            print("[{}] {}".format(reqst['id'], reqst['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")