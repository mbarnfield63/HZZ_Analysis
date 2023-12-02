# Import libraries
import time # to measure time to analyse

# Import functions
import hzz_functions

if __name__ == "__main__":
    start = time.time()
    samples = hzz_functions.get_samples()
    data = hzz_functions.get_data_from_files(samples)
    elapsed = time.time() - start
    print(f"Time taken: {elapsed:.2f} s.")
    hzz_functions.plot_data(data, samples)