#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays a header variable 'X-School-User-Id' with value 98
curl -sH "X-School-User-Id: 98" "$1" 
