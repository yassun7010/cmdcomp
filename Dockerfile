FROM python:3.11-slim as builder

WORKDIR /apps/cmdcomp/
RUN pip install --upgrade pip && pip install --no-cache-dir poetry
COPY . /apps/cmdcomp/
RUN poetry build -f wheel
RUN poetry version --short > dist/VERSION


FROM python:3.11-slim as runner

WORKDIR /apps/cmdcomp/
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /apps/cmdcomp/dist /tmp/dist
RUN pip install --no-cache-dir "/tmp/dist/cmdcomp-$(cat /tmp/dist/VERSION)-py3-none-any.whl"

ENTRYPOINT ["cmdcomp"]
