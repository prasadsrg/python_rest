FROM python:3.6
ADD . /dist
WORKDIR /dist
EXPOSE 5001
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "src/app.py"]
