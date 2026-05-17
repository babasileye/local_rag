FROM pytorch/pytorch:2.7.0-cuda11.8-cudnn9-runtime

ARG PROJECT_DIR=/home/my_project

WORKDIR ${PROJECT_DIR}

RUN apt-get update && apt-get install -y gcc curl

RUN curl -fsSL https://ollama.com/install.sh | sh

ADD pyproject.toml .
ADD README.md .

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=True \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.7.1

RUN pip install poetry==1.7.1 && \
    poetry install && \
    poetry run python -m ipykernel install --user --name python-docker-env --display-name "Python (Docker Env)"

# Start Ollama in the background with logging
CMD ["/bin/sh", "-c", "ollama serve > /var/log/ollama.log 2>&1 &"]
    