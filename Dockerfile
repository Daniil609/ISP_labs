FROM python:3.8.5
WORKDIR /Users
COPY print.py .
CMD ["python", "./print.py"]