FROM python:3.9.18-slim-bullseye
WORKDIR /app
COPY ./ /app/
RUN pip install --no-cache-dir -r requirements.txt
ENV TELEGRAM_BOT_API_KEY=""
ENV GEMINI_API_KEYS=""
CMD ["sh", "-c", "python main.py ${7218686976:AAF9sDAr5tz8Nt_eMBoOl9-2RR6QsH5onTo} ${AIzaSyBytHaZDwFzOhtsvDXJOOX7p2WCs7-jWC0}"]
