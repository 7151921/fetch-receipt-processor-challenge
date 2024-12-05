#!/bin/sh

pytest --cov=app --cov-report=term-missing;

exec uvicorn app.main:app --host 0.0.0.0 --port 8000