# Guild Developer

## Docker Image Build
```sh
docker build -t yassun7010/cmdcomp:$(poetry version --short) .
docker build -t yassun7010/cmdcomp:latest .
```

## Docker Image Publish

```sh
docker push yassun7010/cmdcomp:$(poetry version --short)
docker push yassun7010/cmdcomp:latest
```
