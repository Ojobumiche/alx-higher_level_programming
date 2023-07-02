#!/bin/bash
# Get the content-length of a given IP address
curl -sI "$1" | awk -F ': ' '/Content-Length/ {print $2}'
