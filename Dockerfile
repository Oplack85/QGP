FROM python:3.10-alpine

# تثبيت Poetry
RUN pip install poetry

# تعيين مسار العمل داخل الحاوية
WORKDIR /app

# نسخ ملفات المشروع إلى الحاوية
COPY . /app

# تثبيت التبعيات باستخدام Poetry
RUN poetry install

# الأمر الذي سيشغل التطبيق
CMD ["poetry", "run", "python", "main.py"]
