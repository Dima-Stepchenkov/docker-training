#!/bin/bash


docker network create app-network 2>/dev/null || true


docker compose up -d --build

echo "Aplication avalible on http://localhost"
