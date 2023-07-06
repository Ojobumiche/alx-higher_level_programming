#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request
to the email as a parameter, and finally displays the body of 
the response"""
import sys
import requests


if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    body = requests.post(sys.argv[1], data=email)
    print(body.text)

