filename = "f1"
sim_unlocks = Unlocks
sim_items = {
	Items.Power : 9999999999,
	Items.Weird_Substance : 9999999999, 
}
sim_globals = {"a" : 13}
seed = -1
speedup = 64
run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
quick_print(run_time/60)