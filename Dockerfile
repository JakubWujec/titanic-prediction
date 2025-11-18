# docker build -t titanic-model . 
# docker run -p 9696:9696 -it titanic-model
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY "pyproject.toml" "uv.lock" ".python-version" /app/
RUN uv sync --locked

COPY "predict.py" "model.bin" ./
COPY templates /app/templates

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--host", "0.0.0.0", "--port", "9696", "predict:app"]