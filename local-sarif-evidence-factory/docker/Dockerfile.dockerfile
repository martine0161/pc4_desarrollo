# Stage 1: Build con herramientas de análisis
FROM python:3.11-slim AS analyzer

WORKDIR /app

# Instalar herramientas de análisis
RUN pip install --no-cache-dir \
    bandit \
    pip-audit \
    cyclonedx-bom

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY app/ ./app/
COPY analysis/ ./analysis/
COPY scripts/ ./scripts/

# Stage 2: Runtime mínimo
FROM python:3.11-slim

WORKDIR /app

COPY --from=analyzer /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=analyzer /app ./

# Usuario no root
RUN useradd -m -u 1000 scanner && \
    chown -R scanner:scanner /app

USER scanner

CMD ["python", "app/main.py"]
```

**docker/.dockerignore:**
```
evidence/
docs/
*.pyc
__pycache__/
.git/