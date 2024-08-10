FROM python:3.10

# تعيين دليل العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry
RUN poetry install --no-root

# نسخ باقي الملفات
COPY . /app/

# تشغيل السكربت
CMD ["poetry", "run", "python", "main.py"]
