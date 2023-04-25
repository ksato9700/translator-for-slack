FROM python:3.11-slim
WORKDIR /tfs
COPY translator_for_slack translator_for_slack
COPY requirements.txt requirements.txt
RUN pip install .
CMD ["python", "-m", "translator_for_slack.app"]
