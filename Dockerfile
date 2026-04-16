#get python
FROM python:3.10-slim
# set work directory
WORKDIR /app
#copy all files
COPY . .
#create folders 
#RUN mkdir -p input processed quarantine archive logs reports
#command to run the app
CMD ["python", "fileflow.py"]
