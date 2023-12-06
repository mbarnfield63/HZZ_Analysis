# Mini Project 2 - Scientific Computing
## Chemistry with Scientific Computing MSci, University of Bristol

## Atlas Open Data
This computing project focused on turning one of the open data notebooks into a cloud computing package. Without the ability to run in a cloud setting, this project will focus on creating multiple worker containers within docker and 'parallelising' the collection/analysis of the data from [http://opendata.atlas.cern](http://opendata.atlas.cern)

The original jupyter notebook can be found within the repository this work is based on:
[https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git)

## Build Images
Build each respective image (operator, worker, output) using:

  `docker image build -t [name] .`

## Setup network
Create network first: 

  `docker network create rabbit`

Start RabbitMQ broker (attaching 'rabbit' network): 

  `docker run --rm -d -p 15672:15672 -p 5672:5672 --network rabbit --name rabbitmq rabbitmq:3-management`


## Run containers on network
Wait until RabbitMQ server is fully initialised, then run all containers using:

  `docker run --rm -it --network rabbit [output/worker/operator]`
