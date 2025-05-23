FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8200

CMD ["streamlit", "run", "app.py", "--server.port=8200", "--server.address=0.0.0.0"]
