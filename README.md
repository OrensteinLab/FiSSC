
# FiSSC

A tool to find the smallest sequence cover of mutated reads. The repository for the paper 'FiSSC: Finding small sequence covers to sets of degenerate reads with applications to RNA editing'


## Requirements

Our tool has been tested on the following configuration on a Linux machine:
 - python 3.9.18
 - gurobipy 11.0.2
 - networkx 3.2.1
 - numpy 1.26.4
 - pandas 2.1.2

 
## Setting Up the Tool
First, create a file named `gurobi.json` which contains the details for the gurobi license.
```json
{
  "WLSACCESSID": "XXXXX",
  "WLSSECRET": "XXXXX",
  "LICENSEID": 12345
}

```


## Running the Tool

Make sure to put the zipped fasta files in the `data` folder. The files should be in a similar format to the file `example.fa.gz`.

### Running the FiSSC Algorithm

To execute the FiSSC algorithm, use the following command:
```bash
python ./tool.py --file_name <file-name> --ILP_time_restriction_in_minutes <minutes> --threads <thread_count> [--do_logs]
```

- **file_name**: Only include the name of the file, without a path to the `data` folder.
- **ILP_time_restriction_in_minutes**: Specify an integer to set the time limit (in minutes) for the ILP solver per connected component in the read graph.
- **threads**: Define the number of threads available for the ILP solver.
- **--do_logs** (optional): Generates a CSV log file for the filtering process.

Example command:
```bash
python ./tool.py --file_name GRIA-CNS-RESUB.C0x1291.aligned.sorted.MinRQ998.reads.degenerate.fa.gz --ILP_time_restriction_in_minutes 240 --threads 64 --do_logs
```


The tool produces the following files:
1. A `*__consensus.txt` file which contains the constant and degenerate positions in all the sequences.
2. A `*_picked_sequences.csv` file which contains all the sequences picked by either the filtering step or the ILP solver.

[comment]: <> (Add contact in the final submission)

### Running other Algorithms

To execute the other algorithms, use the following command:
```bash
python ./tool.py --algorithm <algorithm> --file_name <file-name> 
```

The available options are: 
- FiSSC (default)
- Greedy
- MIS_ILP

'Greedy' will produce both an upper bound for the sequence cover size (using greedy min-clique cover) and a lower bound (using greedy MIS). The results are then saved in `*__greedy_results.txt`.

Example command:
```bash
python ./tool.py --algorithm Greedy --file_name GRIA-CNS-RESUB.C0x1291.aligned.sorted.MinRQ998.reads.degenerate.fa.gz 
```


'MIS_ILP' will produce a lower bound using a solution to MIS using ILP. The results are then saved in `*_mis_ilp_results.txt`. Can use `ILP_time_restriction_in_minutes` to restrict the running time of the ILP solver.

Example command:
```bash
python ./tool.py --algorithm MIS_ILP --file_name GRIA-CNS-RESUB.C0x1291.aligned.sorted.MinRQ998.reads.degenerate.fa.gz --ILP_time_restriction_in_minutes 1440 
```
