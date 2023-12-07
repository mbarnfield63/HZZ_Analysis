# Mini Project 2 - Scientific Computing
## Chemistry with Scientific Computing MSci, University of Bristol

## Atlas Open Data
This computing project focused on turning one of the open data notebooks into a cloud computing package. Without the ability to run in a cloud setting, this project will focus on creating multiple worker containers within docker and 'parallelising' the collection/analysis of the data from [http://opendata.atlas.cern](http://opendata.atlas.cern)

The original jupyter notebook can be found within the repository this work is based on:
[https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git)

## Files to be run
The user can define what data they wish to include within the plot by modifying the samples.json file in the main directory.

## Run
The number of workers can be defined within the [docker-compose file](https://github.com/mbarnfield63/HZZ_Analysis/blob/master/docker-compose.yml).

All building of the images, and running the services can be achieved using simply `docker compose up`.

The plot will be saved within the directory this is run from (example plot shown in directory).
