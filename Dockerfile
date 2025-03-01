FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg libffi-dev
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY requirements.txt .

COPY . .

CMD ["python", "bot.py"]
