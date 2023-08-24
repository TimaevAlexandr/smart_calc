FROM python:alpine3.8
COPY . /app
WORKDIR /app
RUN apk update && apk add tk
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "python", "main.py"]