#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
from urllib import error


if __name__ == '__main__':
    try:
        url_arg = sys.argv[1]
        with urllib.request.urlopen(url_arg) as url_response:
            print(url_response.read().decode('UTF-8'))
    except error.HTTPError as http_error:
        print('Error code:', http_error.code)
