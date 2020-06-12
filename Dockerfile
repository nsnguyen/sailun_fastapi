FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt /

# Adds dependencies Python Auth Lib requires.
# Cryptograph lib needs to be compiled by gcc. This dependency is added temporarily.
#RUN apk --update add openssl
#RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base

RUN pip install --upgrade pip

# install fastapi
RUN pip install --no-cache-dir fastapi

RUN pip install -r /requirements.txt

#RUN apk del build-dependencies

COPY ./ /app
ENV MODULE_NAME="app.main"
ENV PORT="8080"
EXPOSE 8080

RUN groupadd -r app \
    && useradd -r -g app app
USER app
