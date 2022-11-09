FROM python:3.10-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN apk --no-cache add libpq
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
