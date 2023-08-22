FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /src

ADD ./src/requirements.txt /src/

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src/

CMD ["uvicorn", "api_handler.main:app", "--host", "0.0.0.0", "--port", "80"]