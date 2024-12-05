FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

COPY start_after_test.sh /start_after_test.sh
RUN chmod +x /start_after_test.sh


CMD ["/start_after_test.sh"]