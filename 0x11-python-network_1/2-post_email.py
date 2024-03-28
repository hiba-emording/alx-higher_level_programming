#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url_arg = sys.argv[1]
    email_arg = sys.argv[2]

    data_values = {"email": email_arg}
    encoded_data = urllib.parse.urlencode(data_values).encode("ascii")

    request = urllib.request.Request(url_arg, encoded_data)
    with urllib.request.urlopen(request) as url_response:
        print(url_response.read().decode("utf-8"))
