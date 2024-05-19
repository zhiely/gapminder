# use official python runtime as parent image
FROM python:3.10-slim-buster

# set working directory to /app
WORKDIR /app

# copy requirements file into containter at /app
COPY app/requirements.txt requirements.txt

#install dependencies
RUN pip install -r requirements.txt

#copy current directory contents into container at /app
COPY app/ /app

# make port 8501 available to the world outside this container
EXPOSE 8501

#run app.py when container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]