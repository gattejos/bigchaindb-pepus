FROM gattejos/rethingdb-cluster

ENV LC_CTYPE C.UTF-8

RUN apt-get update
RUN apt-get -y install python3 python3-pip libffi-dev
RUN pip3 install --upgrade pip
#RUN pip3 install --upgrade setuptools

RUN mkdir -p /usr/src/app

COPY . /usr/src/app/

WORKDIR /usr/src/app

#RUN pip3 install --no-cache-dir -e .
RUN pip3 install -r requirements.txt
RUN pip3 install -e .


WORKDIR /data

ENV BIGCHAINDB_CONFIG_PATH /data/.bigchaindb
ENV BIGCHAINDB_SERVER_BIND 0.0.0.0:9984
ENV BIGCHAINDB_API_ENDPOINT http://bigchaindb:9984/api/v1

RUN mv /usr/src/app/default.conf /etc/rethinkdb/

ENTRYPOINT ["bigchaindb", "--dev-start-rethinkdb", "--dev-allow-temp-keypair" ]

CMD ["start"]

EXPOSE 8080 9984 28015 29015
