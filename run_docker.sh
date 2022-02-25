#!/bin/bash

#echo "******* Git pull *******"
#git pull origin master

echo "******* Stop-Delete Docker Container-Images *******"
docker kill flask_app_uber
docker kill postgres_uber
docker container rm flask_app_uber
docker container rm postgres_uber
#docker rmi $(docker images -q)
#docker volume rm uber_project_postgres_data

echo "******* building docker containers *******"
docker-compose up --build -d

echo "****** bash complete *******"