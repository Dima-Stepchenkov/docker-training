FROM python:3.9-alpine

ARG USER_ID=1000
RUN adduser -D -u ${USER_ID} appuser && \
    mkdir -p /app && chown appuser:appuser /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev

COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

CMD ["python", "HelloWorld.py"]
