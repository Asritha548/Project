############################################################
# Dockerfile for a Django development environment
# Based on Python:3.6 Image
############################################################

FROM python:3.6

#Add Project to docker
ADD . /scraper application/

#Install dependencies
RUN pip install -r /scraper application/requirements.txt
   
COPY start_crawl.py /cmd/start_crawl.py

ENTRYPOINT  python /cmd/start_crawl.py