#!/bin/bash

cd scout
docker build -t idro-scout:2.0.0 .
cd ../exposer
docker build -t idro-exposer:2.0.0 .
cd ..
docker-compose up -d