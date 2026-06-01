FROM python:3.9-slim

# FFmpeg ni o'rnatish (bu musiqa yuklash uchun juda muhim)
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "bot.py"]

