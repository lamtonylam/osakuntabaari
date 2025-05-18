# Osakuntabaari calendar

## Description

Serves .ics calendar files that contain Hämäläis-Osakunta's osakuntabaari student canteen menus. The purpose is to easily view what food is on offer,
straight from calendar software.

# Development

> [!IMPORTANT]  
> install [UV package manager](https://docs.astral.sh/uv/) if it is not already installed on your machine

1. Install dependencies

```
uv sync --locked
```

2. Run the app

```
uv run src/main.py
```

# Running on docker

1. Build image

```
docker build . -t osakuntabaari
```

2. Run docker image

```
docker run -p 5000:5000 osakuntabaari
```
