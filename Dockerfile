FROM python:3.12.6

COPY requirements.txt /weather_bot/
RUN pip install -r /weather_bot/requirements.txt

COPY app/ /weather_bot/app
COPY .env.template /weather_bot/
COPY run.py /weather_bot/

WORKDIR /weather_bot

RUN dump-env --template=.env.template > .env
CMD ["python", "run.py"]