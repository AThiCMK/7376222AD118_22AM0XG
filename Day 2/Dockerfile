FROM python:3.9-slim

WORKDIR /ml-app

COPY app.py /ml-app/app.py

RUN pip install --no-cache-dir scikit-learn joblib

ENV APP=app.py

CMD ["python","app.py"]
