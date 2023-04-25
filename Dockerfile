FROM python:3.11-slim as builder
WORKDIR /tfs
COPY translator_for_slack translator_for_slack
COPY pyproject.toml pyproject.toml
RUN pip install .

FROM python:3.11-slim
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
CMD ["python", "-m", "translator_for_slack.app"]
