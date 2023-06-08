noise_prob = 0.01
def function(n, c, t):
    n_to_use = n.copy()
    for i,x in enumerate(n_to_use):
        if np.random.random() < noise_prob:
            n_to_use[i] = 1-x
    return cpl.binary_rule(n_to_use, gp)

def gp_rule(n):
    rule_number = 6647864381429528876515014584928523775
    DC = []
    for i in range (n):
        print(i)
        cellular_automaton = cpl.init_random(149)
        cellular_automaton = cpl.evolve(cellular_automaton, timesteps=149, apply_rule=lambda n, c, t: cpl.binary_rule(n, rule_number), r=3)
        IC_MAJOR = sum(cellular_automaton[0])
        FINAL = sum(cellular_automaton[-1])
        if IC_MAJOR < 74 and FINAL == 0:
            dc = True
        elif IC_MAJOR >= 74 and FINAL == 149:
            dc = True
        else:
            dc = False
        DC.append(dc)
    return DC

DC = gp_rule(10**5)
count = 0
for value in DC:
    if value:
        count += 1

print("The Accuracy of the GP Rule on the DCT with noise:",count/len(DC))
