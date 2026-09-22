FROM python:3.12-alpine AS builder
WORKDIR /build
COPY app/requirements.txt .
RUN pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt

FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app/ .
EXPOSE 8081
CMD ["python", "app.py"]