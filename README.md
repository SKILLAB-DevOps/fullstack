# Installation

```bash
uv init fullstack
cd fullstack
uv venv
. venv/bin/activate
uv pip install .
```

## Run Dockerfiles

```bash
docker build -t backend -f Dockerfile.backend .
docker build -t db -f Dockerfile.db .
docker build -t frontend -f Dockerfile.frontend .

docker run --name backend -p8000:8000 backend
```

## Run docker-compose

```bash
docker-compose up
docker-compose down
```