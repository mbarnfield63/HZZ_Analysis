# Mini Project 2 - Scientific Computing
## Chemistry with Scientific Computing MSci, University of Bristol

## Atlas Open Data
This computing project focused on turning one of the open data notebooks into a cloud computing package. Without the ability to run in a cloud setting, this project will focus on creating multiple worker containers within docker and 'parallelising' the collection/analysis of the data from [http://opendata.atlas.cern](http://opendata.atlas.cern)

The original jupyter notebook can be found within the repository this work is based on:
[https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git](https://github.com/atlas-outreach-data-tools/notebooks-collection-opendata.git)

## Running
Build the file using:
`docker image build -t hzz .`
Run the image using:
`docker run -d -v .:/path/in/container hzz`

(assuming you're in the directory of the Dockerfile)
