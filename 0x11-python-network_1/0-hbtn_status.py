#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
and displays the body of the response.
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    # Use 'with' statement to handle the request and response
    with urllib.request.urlopen(url) as response:
        body = response.read()  # Read the response body
        
        # Display the output in the required format
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))

