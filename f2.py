filename = "f1"
sim_unlocks = Unlocks
sim_items = {Items.Carrot : 99999999999, Items.Power : 99999999999}
sim_globals = {}
seed = -1
speedup = 100
run = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
quick_print(run)