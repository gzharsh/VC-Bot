FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg libffi-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
