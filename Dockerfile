FROM python:latest

WORKDIR /saver
COPY . .

RUN [pip installl untangle]
CMD [python parse.py output.xml]
