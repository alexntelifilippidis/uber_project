#!/bin/bash

#echo "******* Git pull *******"
#git pull origin master

echo "******* Stop and remove containers, networks.. *******"
docker-compose down
docker volume rm uber_project_postgres_data

echo "******* building docker containers *******"
docker-compose up --build -d

echo "****** bash complete *******"