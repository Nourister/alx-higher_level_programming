#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    parameter = {
        "email": email
    }
    query_string = urllib.parse.urlencode(parameter)
    data = query_string.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_text = response.read().decode("utf-8")
        print(response_text)
