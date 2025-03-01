# Python 3.10 use kar raha hu, agar tu koi aur version chahata hai toh bata
FROM python:3.10

# Working directory set kar raha hu
WORKDIR /app

# Required dependencies copy kar raha hu
COPY requirements.txt requirements.txt

# Python dependencies install kar raha hu
RUN pip install --no-cache-dir -r requirements.txt

# Baki saari files copy kar raha hu
COPY . .

# Command to run the bot
CMD ["python", "main.py"]
