#!/bin/sh

exec uvicorn main:app --host 0.0.0.0 --port 5000 --reload --log-config log_config.yml