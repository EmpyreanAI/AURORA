FROM python:3.7
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "sample/main.py"]
