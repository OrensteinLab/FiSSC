import pandas as pd
from scripts.sequence_stuff import *
from scripts.plots import *
from scripts.collector import *
from scripts.filtering import *
import os
import time
import networkx as nx


def set_constant_seeds():
    np.random.seed(42)
    pd.np.random.seed(42)
    random.seed(42)
    nx.random.seed(42)


def setup_folders():
    if not os.path.exists('logs'):
        os.makedirs('logs')
        print('Created logs folder')

def main():
    setup_folders()


    for data_type in ['long_reads', 'short_reads']: 
        files = os.listdir('data/'+data_type)
        files = [file for file in files if file.endswith('.fa.gz')]

        for file in files:
            set_constant_seeds()
            starting_time = time.time()
            print(f'Working on {file}...')

            name = file.split('.fa.gz')[0]

            # check if already done
            if os.path.exists(f'data/{data_type}/{name}.filtered_picked.csv'):
                print(f'{file} already done. Skipping...')
                continue

            
                
            specific_file = f'data/{data_type}/{name}.csv'
            sequences = pd.read_csv(specific_file)['Sequence'].values
            filter = Filter(sequences, log_file_path=f'logs/{name}_filter_log.csv')
            final_working_sequences, final_picked_sequences, history = filter.do_filter()

            filter.save_picked_csv(f'data/{data_type}/{name}.filtered_picked.csv')
            filter.save_working_csv(f'data/{data_type}/{name}.filtered_working.csv')

            print(f'{name} done in {time.time()-starting_time} seconds')


if __name__ == '__main__':
    main()
