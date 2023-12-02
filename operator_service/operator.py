import time
import operator_functions

if __name__ == '__main__':
    samples = operator_functions.get_samples() # retrieve samples dict
    list_samples = operator_functions.list_samples(samples) # retrieve list of samples
    print(list_samples)
    print('Complete.')
