#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

""" 
Get the URL and email from command line arguments
"""
url = sys.argv[1]
email = sys.argv[2]

"""
Encode the email parameter
"""
params = urllib.parse.urlencode({'email': email}).encode('utf-8')

"""
Send the POST request and handle the response
"""
with urllib.request.urlopen(url, data=params) as response:
    """
    Decode the response body in utf-8
    """
    decoded_response = response.read().decode('utf-8')

    """
    Display the body of the response
    """
    print(decoded_response)

