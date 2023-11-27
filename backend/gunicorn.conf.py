# Configuration file for `gunicorn` command.
# 1) Set the settings in this file.
# 2) Run `gunicorn` from the terminal in the directory containing this file

import os

from dotenv import load_dotenv

load_dotenv()

# Get the `ENVIRONMENT` env variable and convert it to lowercase if it exists
environment = os.getenv("ENVIRONMENT")
environment = environment.lower() if environment else "dev"


# Gunicorn app
# Tell Gunicorn which application to run
wsgi_app = "src.url_shortener.app.main:app"


# Requests
# Restart workers after so many requests, with some variability.
max_requests = 1000
max_requests_jitter = 50


# Logging
accesslog = "-"
acceslogformat = "%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"


# Use this formula for production, otherwise only run 2 workers
workers = 4 if environment == "PROD" or environment == "prod" else 1
worker_class = "uvicorn.workers.UvicornWorker"
