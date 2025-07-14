FROM python:3.10-slim

RUN apt-get update && apt-get install -y gnupg2 curl apt-transport-https unixodbc-dev gcc g++ \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "main:app"]