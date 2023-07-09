# Guild Developer

## Docker Image Build
```sh
docker build -t yassun4dev/cmdcomp:$(poetry version --short) .
docker build -t yassun4dev/cmdcomp:latest .
```

## Docker Image Publish

```sh
docker push yassun4dev/cmdcomp:$(poetry version --short)
docker push yassun4dev/cmdcomp:latest
```
