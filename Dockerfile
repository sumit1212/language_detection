
FROM python:3.9


WORKDIR /home/mrs/Documents/Language_detection


COPY . /home/mrs/Documents/Language_detection


RUN pip install -r requirements.txt


# COPY . /Language_detection/app