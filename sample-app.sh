#!/bin/bash
rm -rf tempdir
mkdir tempdir

cp sample_app.py tempdir/.

echo "FROM python:3.11-slim" > tempdir/Dockerfile
echo "RUN pip install --no-input --progress-bar off flask" >> tempdir/Dockerfile
echo "COPY sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 8080" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

cd tempdir
docker build -t sampleapp:day4 .
docker run -t -d -p 8080:8080 -e STUDENT_TOKEN="$STUDENT_TOKEN" --name samplerunning sampleapp:day4
docker ps -a
