FROM python:3.6-jessie

WORKDIR /usr/bin/app

COPY . .

RUN bash -c "useradd -p password user"
RUN echo "user:Docker!" | chpasswd
RUN pip3 install -r requirements.txt

EXPOSE 21

CMD ["python3", "ftpserver.py"]