FROM python:3.12-slim
WORKDIR /app
copy requirements.txt .
copy app.py .
RUN PIP3 install -r requirements.txt
EXPOSE 3000
CMD ["python", "app.py"]
