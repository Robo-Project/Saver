#!/bin/bash

python pythonscripts/simple-parse.py $1 | psql -U postgres -d postgres -h 172.17.0.1
