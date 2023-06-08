FROM python:3.9.10

COPY . /app/
WORKDIR /app/
RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

CMD python3 -m bot
