# Project

The project consist of two parts :
1)A Scrapy project- which is used to crawl data from specified url list.
2)A Django REST API- is used to access the result of the scraped data.


###System Overview

In our system we are using 3 containers which work together to make our system scalable with any number of urls
1.DataBase
2.Application
3.Scraper


###DB Container 
This container holds the DB for the use of our system.The container is build on the base image of Postgres.The ENV_variables which should be passed are :
- POSTGRES_PASS:Password for the database user
- POSTGRES_USER:Username for  the user who have access to the database
- POSTGRES_DB: Datatabase name 

To prevent data loss after the restart of the database, we will mount a vloume at this path '/var/lib/postgresql/data'


### Scraper Container 
 This container hold the scraper i.e the container which will crawl the list of url and save that to the Database.The Dockerfile for the docker image will be present in the repo under web-analysis folder.The ENV_varables which should be passed are:
- DB_PASS:Password for DB user.
- DB_USER:Username for  the user who have access to the data.
- DB_NAME: Database name which is defined in Db container
- DB_HOST: The ip in which the DB container is hosted

We will be using Docker compose to link the DB, Scraper and Application containers. 

###Application Container 

This container will hold the Application,ie, API service for our scraper.The data which is saved in DB by scraper can be accessed using this container.The Dockerfile for the docker image will be present in the repo under'application' folder.The ENV_variables  which should be passed are:

- DB_PASS:Password for DB user .
- DB_USER:Username for  the user who have access to the data.
- DB_NAME: Database name which is defined in Db container
- DB_HOST: The ip in which the DB container is hosted 
- Admin_USERNAME=Username of API admin user
- Admin_PASSWORD=password of API admin user
- Admin_EMAIL=email of API admin user
- DEBUG_VAR= True / False (to set DEBUG variable in scrapy settings.py)

Scraper container will be linked to DB container.We will be exposing port 80 since this is a webservice. 

### Install Docker compose

``` pip install docker-compose ```
 Since we use multi containers, we are defining the docker compose file.


### Insert url to Crawl
1.Create a csv file which contain the urls 'urls.csv' 

2.Add this csv file to 'application' folder

### System Layout

![alt tag](https://raw.githubusercontent.com/sayonetech/automated-scraper/master/specs/SYSTEM-ARCHITECTUER.png)

### To build in LOCAL

1. Pull the repo to your local system.
2. Navigate to project folder. 
3. Update the path of Scraper Dockerfile in docker-compose.yml
4. To make the system run, use the following code 
   ```docker-compose up ```
    This command will automatically create the Docker image and will run the container .
5. To check whether the container is live or not, run the following code.
   ``` sudo docker ps ```
    This will show the live containers in system.There you can find our 3 containers.

The results will be shown in admin page, while running in local. Refer the api structure while it is running in live. 

