#We will be using python as our base image
FROM python:3.7

#For the preprocessing file, we need to install numpy on the container
RUN pip install numpy

#Computing the path on the container (not used with volume)
RUN mkdir /app
RUN mkdir /app/pipeline
RUN mkdir /app/docker
RUN mkdir /app/pipeline/model
RUN mkdir /app/pipeline/preprocessing
RUN mkdir /app/pipeline/utils

#Copying all the files (not used with volumes)
#COPY app/pipeline/model/model.py /app/pipeline/model/model.py
#COPY app/pipeline/preprocessing/preprocessing.py /app/pipeline/preprocessing/preprocessing.py
#COPY app/pipeline/utils/utils.py /app/pipeline/utils/utils.py 

#Starting with app as our initial work directory
WORKDIR /app

#Showing result of this model.py when running 
CMD ["python", "pipeline/model/model.py"]