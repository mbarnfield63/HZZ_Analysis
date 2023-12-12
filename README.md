# Mini Project 2 - Scientific Computing
## Chemistry with Scientific Computing MSci, University of Bristol

## Atlas Open Data
This computing project focused on turning one of the open data notebooks into a cloud computing package. Without the ability to run in a cloud setting, this project will focus on creating multiple worker containers within docker and 'parallelising' the collection/analysis of the data from [http://opendata.atlas.cern](http://opendata.atlas.cern)

The original jupyter notebook can be found within the repository this work is based on:
[https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git)

## Files to be run
The user can define what data they wish to include within the plot by modifying the samples.json file in the main directory.

## Run
The number of workers for the swarm can be defined within the [docker-compose file](https://github.com/mbarnfield63/HZZ_Analysis/blob/master/docker-compose.yml).

Functions for swarm mode:
- Initialise swarm functionality using: `docker swarm init`
- Start the swarm using: `docker stack deploy -c docker-compose.yml <stack_name>`
- Add/remove workers using: `docker service scale worker=<number>`
- Restart/update operator & output using: `docker service update --image <new_image> <service_name>`

The plot will be saved within the directory this is run from (example plot shown in directory).
