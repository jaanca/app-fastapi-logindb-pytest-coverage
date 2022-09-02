FROM python:3.9.6-slim-bullseye

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80
ENTRYPOINT ["/bin/bash", "entrypoint.sh"]

