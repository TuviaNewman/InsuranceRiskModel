#Keep image small with python slim
FROM python:3.7-slim
#Copy from the local current dir to the image workdir:
COPY predict.py .
COPY models models/
#Install local
COPY requirements.txt .
RUN pip install gunicorn
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD [ "gunicorn","-w","1","-b","0.0.0.0:8080","predict:predict"]