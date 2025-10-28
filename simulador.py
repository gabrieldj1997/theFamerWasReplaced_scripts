filename = "simulacao"
sim_unlocks = Unlocks
sim_items = {}
for i in Items:
	sim_items[i] = 9999999999
sim_globals = {}
seed = -1
speedup = 64
run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
quick_print(run_time/60)