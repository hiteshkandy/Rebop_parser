import rebop

toy_network = [['A','B',1],['C','D',2],['B','C',2],['D','A',1]]
mm = rebop.Gillespie()
for rxn in toy_network:
  if rxn[2]==1:
    mm.add_reaction(f"K *{rxn[0]}", [], [f"{rxn[1]}"])
  else:
    mm.add_reaction(f"K *{rxn[0]}*{rxn[1]}", [f"{rxn[1]}"], [])
print(mm)

params = {"K": 1}

initial_values = {rxn[0]: 100 for rxn in toy_network}
ds = mm.run(initial_values, tmax=250, nb_steps=100, params=params, rng=0)

print(ds)
