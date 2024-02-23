FROM python:3.12-slim as builder
RUN pip install pdm
WORKDIR /work
COPY src pyproject.toml pdm.lock README.md /work/
RUN pdm build

FROM python:3.12-slim
COPY --from=builder /work/dist /dist
RUN pip install /dist/*.whl
CMD ["python", "-m", "translator_for_slack.app"]
