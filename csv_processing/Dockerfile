FROM python:3.10-alpine

WORKDIR /usr/src/csv_processing

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/csv_processing/entrypoint.sh
RUN chmod +x /usr/src/csv_processing/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/csv_processing/entrypoint.sh"]