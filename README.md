# python_functions

[![Python Functions CI](https://github.com/JacquesLeen/python_functions/actions/workflows/main.yaml/badge.svg)](https://github.com/JacquesLeen/python_functions/actions/workflows/main.yaml)


## Microservice Call

```bash
curl -X 'POST' \
  'https://fantastic-invention-vrg4xwpq54j2xg4w-8000.app.github.dev/wiki/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft",
  "sentences": 2
}'
```

## Container Build & Run

```bash
docker build -t  wikipedia-api:latest .
docker run -p 8000:8000 wikipedia-api:latest
```
