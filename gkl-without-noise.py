import cellpylib as cpl

def gkl_rule(n):
    rule_number = 493275728351097185153566218236460895
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

DC = gkl_rule(10**5)
count = 0
for value in DC:
    if value:
        count += 1

print("The Accuracy of the GKL Rule on the DCT without noise:",count/len(DC))
