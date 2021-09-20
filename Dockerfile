FROM python:3.9 as builder
WORKDIR /tfs
COPY translator_for_slack translator_for_slack
COPY pyproject.toml pyproject.toml
RUN pip install --use-feature=in-tree-build .

FROM python:3.9-slim
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
CMD ["python", "-m", "translator_for_slack.app"]
