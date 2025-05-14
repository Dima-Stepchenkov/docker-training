#!/bin/bash

mkdir -p logs

docker compose up --build -d

echo "Aplication avaliable http://localhost"
echo "Flask logs ./logs/flask.log"
