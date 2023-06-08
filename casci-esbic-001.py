import cellpylib as cpl
import numpy as np

# GP Rule
gp = 6647864381429528876515014584928523775
noise_prob = 0.0
def function(n, c, t):
    n_to_use = n.copy()
    for i,x in enumerate(n_to_use):
        if np.random.random() < noise_prob:
            n_to_use[i] = 1-x
    return cpl.binary_rule(n_to_use, gp)

DC = []
no_of_iterations = 10**5
for i in range(no_of_iterations):
    print(i)
    cellular_automaton = cpl.init_random(149)
    IC_MAJOR = sum(cellular_automaton[0])
    cellular_automaton = cpl.evolve(cellular_automaton, timesteps=149,
                                    apply_rule=function, r=3)
    FINAL = sum(cellular_automaton[-1])
    if IC_MAJOR < 74 and FINAL == 0:
        dc = True
    elif IC_MAJOR >= 74 and FINAL == 149:
        dc = True
    else:
        dc = False
    DC.append(dc)

count = 0
for value in DC:
    if value:
        count += 1

acc = count/len(DC)
print(acc)
