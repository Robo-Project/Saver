FROM alpine:3.11

RUN apk add --no-cache python
RUN apk add --no-cache postgresql-client

WORKDIR /saver
COPY . .
RUN mkdir data

CMD sh send.sh /saver/data/output.xml
