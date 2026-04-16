#get python
FROM python:3.10-slim
# set work directory
WORKDIR /app
#copy all files
COPY . .
#command to run the app
CMD ["python", "fileflow.py"]
