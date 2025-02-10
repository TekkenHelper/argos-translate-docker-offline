FROM python:3.9

WORKDIR /app

COPY argos-language-packs /argos-language-packs
COPY app /app
COPY pip-packages /pip-packages

RUN pip install --no-cache-dir /pip-packages/argos/*
RUN pip install --no-cache-dir /pip-packages/flask/*
ENTRYPOINT [ "python" ]
CMD ["flask_server.py"]