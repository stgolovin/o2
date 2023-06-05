FROM python:3.11

RUN mkdir /o2
WORKDIR /o2

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /o2/

EXPOSE 8000

CMD ["python", "main.py"]
