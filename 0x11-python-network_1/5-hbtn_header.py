#!/usr/bin/python3
"""
Python script that takes in a URL, sends a requestto the URL and displays
the value of the X-Request-Id variable found in the header of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    reponse = requests.get(url)
    value = response.header.get("X-Request-Id")
    print(value)
