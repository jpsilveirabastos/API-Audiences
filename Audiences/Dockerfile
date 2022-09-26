FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /audience_data

COPY ./requirements.txt /audience_data/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /audience_data/requirements.txt

COPY ./app /audience_data/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]