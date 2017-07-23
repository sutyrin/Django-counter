#!/bin/bash

set -e 
cd counter 

./manage.py migrate 
./manage.py runserver 0.0.0.0:8080