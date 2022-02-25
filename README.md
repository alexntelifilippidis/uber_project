#Deploy ML models using Flask + PostgreSQL inside Docker

## Running the solution

In order to run this solution, you just have to install Docker, Docker compose, then go to this repository in cmd, and then type:
```
bash run_docker.sh
```
After the API will run on http://localhost:5000/

For Docker installation instructions follow:

— [Docker installation](https://docs.docker.com/engine/install/ubuntu/)

— [Make Docker run without root](https://docs.docker.com/engine/install/linux-postinstall/)

— [Docker Compose installation](https://docs.docker.com/compose/install/)

## Understanding the solution


— The fast way: the project is structured as follows: Flask app and WSGI entry point are localed in flask_app directory.
PostgreSQL and project configuration files are located in postgresql directory. Both directories contain Docker files that are connected using docker_compose.yml file in the main directory. 
  
   For simplicity, I also added run_docker.sh file for an even easier setting-up and running this solution. 
```
.
├── flask_app 
│   ├── app.py          
│   ├── wsgi.py
│   ├── requirements.txt
│   ├── uber.log
│   └── Dockerfile
├── postgresql
│   ├── scripts          
│   └── Dockerfile
├── docker-compose.yml
├── run_docker.sh
├── gitignore
└── README.md

```
## API endpoints manual