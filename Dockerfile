FROM python:3.9

ENV PYTHONIOENCODING=utf8

WORKDIR /code
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN chmod a+x /code/entrypoint.sh
ENTRYPOINT [ "/code/entrypoint.sh" ]
