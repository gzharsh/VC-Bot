# Step 1: Python ka latest stable version use kar
FROM python:3.10  

# Step 2: Working directory set kar
WORKDIR /app  

# Step 3: Pehle requirements.txt copy kar
COPY requirements.txt .

# Step 4: Dependencies install kar
RUN pip install --no-cache-dir -r requirements.txt  

# Step 5: Baaki saari files copy kar
COPY . .  

# Step 6: Bot ko run karne ka command
CMD ["python", "bot.py"]  
