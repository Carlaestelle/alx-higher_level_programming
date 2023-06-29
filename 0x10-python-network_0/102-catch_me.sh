#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me and server respond "You got me!"
curl -sLX PUT -H "origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
