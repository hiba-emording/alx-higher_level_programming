#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    data = requests.get(url)

    print("Body response:")
    print("\t- type:", type(data.text))
    print("\t- content:", data.text)
