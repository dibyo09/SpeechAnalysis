FROM python:3.6.1-alpine

RUN mkdir -p /src
ENV PYTHONPATH /
WORKDIR /src

RUN mkdir -p /src/kaplptreeimages/uploads

RUN mkdir -p /src/templates
ADD src/templates/*.* /src/templates/
COPY ["src/templates/*.*", "templates/"]

RUN mkdir -p /src/static/js
ADD src/static/js/*.* /src/static/js/
COPY ["src/static/js/*.*", "static/js/"]

ADD src/KalptreeSpeechRecognizer.py /src/KalptreeSpeechRecognizer.py
COPY ["src/KalptreeSpeechRecognizer.py", "KalptreeSpeechRecognizer.py"]


COPY ["src/requirements.txt", "requirements.txt"]
RUN pip3 install pipenv

RUN pip install --upgrade pip

RUN /sbin/apk add --no-cache --virtual .deps gcc musl-dev \
 && /usr/local/bin/pip install --no-cache-dir black==19.10b0 \
 && /sbin/apk del --no-cache .deps
RUN pip install -r requirements.txt
RUN [ "python", "-c", "import nltk; nltk.download('all')" ]

EXPOSE 5002
LABEL io.openshift.expose-services 5002:http
USER 1001
CMD ["python","KalptreeSpeechRecognizer.py"]