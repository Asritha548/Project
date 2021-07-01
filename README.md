Project Architecture Overview 

In the project we are using 2 containers which work together to make our system scalable with any number of urls
1.DataBase
2.Scraper

### DB Container 
This is the DB.The container is build on the base image of Postgres.The ENV_variables are :
- POSTGRES_PASS:Password for the database user
- POSTGRES_USER:Username for  the user who have access to the database
- POSTGRES_DB: Datatabase name 

Note: To prevent data loss after the restart of the database, we will mount a vloume at this path '/var/lib/postgresql/data'


### Scraper Container 
 This container hold the scraper i.e the container which will crawl the list of urls and save that to the Database.The ENV_varables are:
- DB_PASS:Password for DB user.
- DB_USER:Username for  the user who have access to the data.
- DB_NAME: Database name which is defined in Db container
- DB_HOST: The ip in which the DB container is hosted

We will be using Docker compose to link the DB and Scraper application containers.

### Testing strategy:
- we will be using the sudo docker ps command to check the status of the containers.
- The most reliable way is to check /proc/1/cgroup. It will tell you the control groups of the init process, and when you are not in a container, that will be / for all hierarchies. When you are inside a container, you will see the name of the anchor point. With Docker containers, it will be something like /docker/<containerid>. 
- Testing strategy should be changed according to the OS where the container is running. Tools that can be used to test Docker containers include Kitematic and Vagrant.
 
 ### Design flaws and recommendations:
 - In this design, we didn't consider the OS where the container is running. But, we should add the new list "include tasks" to handle the different Operating systems(linux, macos and windows).
 
 List to be included in ansible playbook file:
 ---

- include_tasks: linux.yml
  when: ansible_system == 'Linux'

- include_tasks: macos.yml
  when: ansible_system == 'Darwin'
 
- Along with the DB and Scraper container there is a necessity to add the Application API container which will provide the API service for the scraper.The data which is saved in DB by scraper can be accessed using this container. For caching the response of the url request, we have to mount a volume in the path '/scraper-cache',so the cached data will not be lost. We can reuse the data once we restart the container.