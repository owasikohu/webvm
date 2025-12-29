FROM --platform=i386 python:3
RUN useradd -m user && echo "user:password" | chpasswd
RUN echo 'root:password' | chpasswd


COPY dockerfiles/yuyake_bunko/app/ /home/user
COPY dockerfiles/yuyake_bunko/flag.txt /home/user

RUN pip install -r requirements.txt

CMD [ "/bin/bash" ]
