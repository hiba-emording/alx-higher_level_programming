#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of response
"""
import urllib.request
import sys


if __name__ == '__main__':
    url_arg = sys.argv[1]

    request = urllib.request.Request(url_arg)
    with urllib.request.urlopen(request) as url_response:
        x_request_id = dict(url_response.headers).get("X-Request-Id")
        print(x_request_id)
