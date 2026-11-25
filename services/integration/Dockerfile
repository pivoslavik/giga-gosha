FROM python:3.12.16-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl=7.88.1-10+deb12u15 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
COPY packages/runtime/ packages/runtime/
COPY services/integration/ services/integration/

USER 65532:65532
CMD ["python", "-m", "services.integration"]
