FROM python:3.11-slim as builder

WORKDIR /app/cmdcomp/
RUN pip install --upgrade pip && pip install --no-cache-dir poetry
COPY . /app/cmdcomp/
RUN poetry build -f wheel
RUN poetry version --short > dist/VERSION


FROM python:3.11-slim as runner

WORKDIR /app/cmdcomp/
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app/cmdcomp/dist /tmp/dist
RUN pip install --no-cache-dir "/tmp/dist/cmdcomp-$(cat /tmp/dist/VERSION)-py3-none-any.whl"

ENTRYPOINT ["cmdcomp"]
