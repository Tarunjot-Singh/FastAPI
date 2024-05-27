FastAPI application

FastAPI is a modern, high-performance, batteries-included Python web framework that's perfect for building RESTful APIs.

Installation
pip install requirements.txt

Run the Server
fastapi dev main.py

Further, you can go to Offical Swagger UI to play around with the API
http://127.0.0.1:8000/docs

This application has the following routes:
1 - /csv  
2 - /embedding

Testing:
Use the command below to run UnitTest
pytest

Docker Image:
In order to build a docker image, Please refer to official docs https://fastapi.tiangolo.com/deployment/docker/

Once Docker is setup, use the command below to run
docker-compose up --build
