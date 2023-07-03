#!/usr/bin/python3
<<<<<<< HEAD
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

=======
"""
POST request to the passed URL with the email as a parameter
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response (decoded in utf-8)
    """
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf8')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        result = response.read()
        print(result.decode('utf8'))

if __name__ == "__main__":
    main(argv)
>>>>>>> 75fb044a161a5149d6e1289bb2dde9136eda6c7a
