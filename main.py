from parser import rxn_adder, rxn_runner, read_topo_file

file_path = input('enter topo file path\n')
initial_value = input('enter initial value for all species\n')
param_value = input('enter rate parameter - k value\n')

network = read_topo_file(file_path)
mm = rxn_adder(network)
ds = rxn_runner(mm, network, initial_value=initial_value, param_value=param_value)

print(mm,ds)