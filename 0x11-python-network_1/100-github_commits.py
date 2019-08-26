#!/usr/bin/python3
''' takes in 2 args and gets 10 commits '''
from sys import argv
import requests



if __name__ == "__main__":
    """
    argv[1] = repository
    argv[2] = owner
    """
    reqst = requests.get('https://api.github.com/repos/{}/{}/commits'
                       .format(argv[2], argv[1])).json()
    count = 0
    for commit in reqst:
        name = commit.get("commit").get("author").get("name")
        sha = commit.get("sha")
        print("{}: {}".format(sha, name))
        count += 1
        if count == 10:
            break