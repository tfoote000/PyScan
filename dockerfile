FROM python:3

WORKDIR /var/app
COPY pyscan.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./pyscan.py"]