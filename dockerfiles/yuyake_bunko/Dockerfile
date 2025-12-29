FROM --platform=i386 i386/python:3

WORKDIR /app
COPY dockerfiles/yuyake_bunko/app/ /app
COPY dockerfiles/yuyake_bunko/flag.txt /flag.txt

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "app.py"]
CMD [ "/bin/bash" ]
