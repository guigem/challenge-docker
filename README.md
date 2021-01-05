# challenge-docker

#### BeCode challenge: January 2021

#### Contributors: Guillaume Gémis

## Aim of this project

The goal of this project is to create a container using [Docker](https://www.docker.com/ "Title"). 
The container will cover the following structure:
```
/app
    |-docker
    |   |-Dockerfile -> your Dockerfile
    |-pipeline
    |   |
    |   |-model
    |   |    |-model.py -> print a number between 1 and 400
    |   |-preprocessing
    |   |    |-preprocessing.py -> print a numpy array
    |   |-utils
    |   |    |-utils.py -> print "in progress..."
```
This is composed of 3 Python files and a Dockerfile needed to indicate instructions to the container when launched.

The next step was to create volumes inside of the container in order to link directly the files with the local machine in order to synchronise any changes made. 

## Installation 

In order to run and launch this project, [Numpy](https://numpy.org/doc/stable/ "Title") must be installed: 
```
pip install numpy
```
The documentation for building and running a container can be found [here](https://docs.docker.com/ "Title").



