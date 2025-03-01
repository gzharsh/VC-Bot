# Python 3.10 ka lightweight version use kar
FROM python:3.10-slim  

# Working directory set kar
WORKDIR /app  

# Pehle dependencies install kar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  

# Baaki saari files copy kar
COPY . .  

# Bot ko run karne ka command
CMD ["python", "bot.py"]  
