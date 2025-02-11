#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays value
- of the X-Request-Id variable found in the header of response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get("X-Request-Id")
        print(x_request_id)
