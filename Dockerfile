FROM python3:latest
COPY . . 
CMD ["python3", "app.py"]