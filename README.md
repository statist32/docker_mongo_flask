# docker_mongo_flask
docker_mongo_flask

1.  install Docker (https://docs.docker.com/install/)
1.1 maybe you have to use the docker ToolBox (https://docs.docker.com/toolbox/toolbox_install_windows/)
2.  clone this repository
3.  head over to your bash/cmd and run ```docker-compose up``` from this repository/folder
4.  press ctrl + c once if the download and installation is finished
    after ```flask-app | * Runnung on http: ....```
4.1 You have to allow the volume access (maybe you have to set a password)
5.  install postman (https://www.getpostman.com/downloads/)

# Enter mongodb
1. First you have to enter the container
    ```
    docker exec -it mongo bash
    ```
2. just run 
    ```
    mongo
    ```
Some references:
pymongo
https://gist.github.com/jordifebrer/4ea7f993412124aff1f0d5e6b2624e12
https://api.mongodb.com/python/current/tutorial.html

docker
https://gist.github.com/bradtraversy/89fad226dc058a41b596d586022a9bd3
