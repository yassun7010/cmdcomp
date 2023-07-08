FROM python:3.11-slim as builder

WORKDIR /apps/cmdcomp/
RUN pip install --upgrade pip && pip install --no-cache-dir poetry
COPY . /apps/cmdcomp/
RUN poetry build -f wheel
RUN mv dist/cmdcomp-$(poetry version --short)-py3-none-any.whl dist/cmdcomp.whl

FROM python:3.11-slim as runner

WORKDIR /apps/cmdcomp/
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /apps/cmdcomp/dist/cmdcomp.whl /tmp/cmdcomp.whl
RUN pip install --no-cache-dir /tmp/cmdcomp.whl

ENTRYPOINT ["cmdcomp"]
