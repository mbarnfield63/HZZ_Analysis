import json
import infofile

# Data
tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/4lep/"

def get_samples():
    with open('samples.json') as json_file:
        samples = json.load(json_file)
    return samples

def construct_file_name(sample, file_name):
    if sample == 'data':
        prefix = "Data/"
    else:
        prefix = "MC/mc_" + str(infofile.infos[file_name]["DSID"]) + "."
    return tuple_path + prefix + file_name + ".4lep.root"

def list_samples(samples):
    list_samples = []
    for sample in samples:
        for file_name in samples[sample]['list']:
            file_string = construct_file_name(sample, file_name)
            list_samples.append(file_string)
    return list_samples