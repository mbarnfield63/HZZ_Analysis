# Import libraries
import time # to measure time to analyse

# Import functions
import hzz_functions

# Samples to process
samples = {
    'data': {
        'list' : ['data_A','data_B','data_C','data_D'],
    },
    r'Background $Z,t\bar{t}$' : { # Z + ttbar
        'list' : ['Zee','Zmumu','ttbar_lep'],
        'color' : "#6b59d3" # purple
    },
    r'Background $ZZ^*$' : { # ZZ
        'list' : ['llll'],
        'color' : "#ff0000" # red
    },
    r'Signal ($m_H$ = 125 GeV)' : { # H -> ZZ -> llll
        'list' : ['ggH125_ZZ4lep','VBFH125_ZZ4lep','WH125_ZZ4lep','ZH125_ZZ4lep'],
        'color' : "#00cdff" # light blue
    },
}

if __name__ == "__main__":
    start = time.time()
    data = hzz_functions.get_data_from_files(samples)
    elapsed = time.time() - start
    print(f"Time taken: {elapsed:.2f} s.")
    hzz_functions.plot_data(data, samples)