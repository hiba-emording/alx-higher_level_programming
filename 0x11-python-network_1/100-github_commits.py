#!/usr/bin/python3
"""
A script that lists the 10 most recent commits on a given GitHub repository.

Usage:
    ./script_name.py <repository_name> <owner_name>
"""
import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repo_name)
    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print("{}: {}".format(sha, author_name))
    except IndexError:
        pass
