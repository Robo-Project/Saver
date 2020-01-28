# Saver

## How to use

To build and run with docker

    docker build -t [container name]
    docker run --rm -v [volume with output.xml]:/saver/data [container name]


To run manually

    sh send.sh /path/to/output.xml


## Documentation

#### simple-parse.py

Takes the file to parse as input and outputs sql-queries based on it    

#### send.sh

Takes the file to parse and passes it to simple-parse.py

Pipes the output of simple-parse.py to psql