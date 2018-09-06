FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ENV RABBITMQ_USERNAME guest
ENV RABBITMQ_PASSWORD guest

ENTRYPOINT [ "python" ]