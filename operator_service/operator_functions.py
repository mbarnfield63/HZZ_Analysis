import json
import infofile

def get_samples():
    with open('samples.json') as json_file:
        samples = json.load(json_file)
    return samples

def get_file_names(samples):

    messages = [] # define empty list to hold messages to send to workers
    
    for s in samples: # loop over samples
        for val in samples[s]['list']: # loop over each file
            if s == 'data':
                prefix = "/Data/"
            else:
                prefix = "/MC/mc_"+str(infofile.infos[val]["DSID"])+"."
            
            message = prefix+" "+val
            messages.append(message) # append file message to list of messages

    return messages # return list of messages to send to workers