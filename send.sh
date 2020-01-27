!#/bin/bash

python pythonscripts/parse.py /saver/data/output.xml | psql -U postgres -d postgres -h 172.17.0.1