FROM python:3.10-slim AS development_build

# python:
ENV  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random
  # pip:
ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

# set work directory
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --no-cache-dir -r requirements.txt
# copy project
COPY . .
