FROM --platform=i386 i386/python:3

WORKDIR /app
COPY app/ /app
COPY /flag.txt /flag.txt

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "app.py"]
