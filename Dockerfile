FROM python:latest

WORKDIR /saver
COPY . .

CMD [python parse.py output.xml]
