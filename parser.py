import rebop
import csv
import re

def rxn_adder(network):
    mm = rebop.Gillespie()
    for rxn in network:
      if rxn[2]==1:
        mm.add_reaction(f"k *{rxn[0]}", [], [f"{rxn[1]}"])
      else:
        mm.add_reaction(f"k *{rxn[0]}*{rxn[1]}", [f"{rxn[1]}"], [])

    return mm

def rxn_runner(mm, network, initial_value, param_value):
    params = {"k": param_value}
    initial_values = {rxn[0]: 100 for rxn in network}
    ds = mm.run(initial_values, tmax=250, nb_steps=100, params=params, rng=0)

    return ds

def read_topo_file(file_path):
    network = []
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Skip the header line
        for line in lines[1:]:  
            row = re.split(r'\s+', line.strip())  # Split by any whitespace
            if len(row) == 3:
                source, target, type_value = row
                network.append([source, target, int(type_value)])  # Convert Type to int
                
    return network