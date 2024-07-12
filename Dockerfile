# syntax=docker/dockerfile:1
FROM python:3.10-slim
ENV PYTHONUNBUFFERED True
ENV APP_HOME /src

# Linuxに必要なパッケージのインストール
RUN apt-get update && apt-get install -y \
    bash \
    bzip2 \
    build-essential \
    curl \
    cargo \
    cmake \
    g++ \
    gcc \
    git \
    gfortran \
    libc-dev \
    libffi-dev \
    libssl-dev \
    libmariadb-dev \
    libopenblas-dev \
    zlib1g-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip setuptools wheel

# WORKDIR /code
WORKDIR $APP_HOME

# ベースの依存関係のインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]