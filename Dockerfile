FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PATH="/code/.venv/bin:$PATH"

# * Install all the dependencies from pyproject.toml
COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked

# * Copy your FastAPI script
COPY "predict.py" "pipeline_v1.bin" ./

EXPOSE 9696

# * Run it with uvicorn 
ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]

