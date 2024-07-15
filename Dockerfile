FROM python:3.10

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container 
RUN mkdir /kao_website 

# setting the working directory 

WORKDIR /kao_website

# copy the current directory elements into the container at /kao_website 

ADD . /kao_website/

# install any needed packages specified in requirements.txt 
RUN pip install -r requirements.txt 
