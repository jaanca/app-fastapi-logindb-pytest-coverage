#! /usr/bin/env bash

# Run migrations
alembic upgrade head

uvicorn --host=0.0.0.0 --port=80 main:app
