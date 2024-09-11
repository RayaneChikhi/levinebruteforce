from itertools import product
from random import randint
n = 7
total_strategies = n ** (2 ** n)
vn = 2**n
un = vn*vn
dn = 2**(3*n)

def generate_possible_hat_configs(n):
    return [tuple((i >> j) & 1 for j in range(n)) for i in range(1 << n)]

possible_hat_configs = generate_possible_hat_configs(n)
hat_config_dict = {
    (config1, config2): i 
    for i, (config1, config2) in enumerate(product(possible_hat_configs, repeat=2))
}


def computeGame(strategy, stack_A, stack_B,stack_C):
    f_A = strategy[hat_config_dict[(stack_B,stack_C)]]
    f_B = strategy[hat_config_dict[(stack_A,stack_C)]]
    f_C = strategy[hat_config_dict[(stack_A,stack_B)]]

    return min(stack_A[f_A - 1], stack_B[f_B - 1],stack_C[f_C - 1])

def computeProbability(strategy):
    S = 0
    for stackA in possible_hat_configs:
        for stackB in possible_hat_configs:
            for stackC in possible_hat_configs:
                S += computeGame(strategy, stackA, stackB,stackC)
    return S / dn
            
def hillclimb(numIter,numRestarts):
    
    seen = set()
    initial_strategy = None
    global_max_strategy = initial_strategy
    global_max_prob = 0
    while True:
        initial_strategy = [1] + [randint(1,n) for i in range(un-2)] + [1]
        v = tuple(initial_strategy)
        if v in seen:
            continue
        seen.add(v)
        local_max_prob = computeProbability(initial_strategy)
        potential_new_strategy = initial_strategy[:]
        for iter in range(numIter):
            idx = randint(1,un-2)
            prev = potential_new_strategy[idx]
            potential_new_strategy[idx] = randint(1,n)
            v = tuple(potential_new_strategy)
            if v in seen:
                potential_new_strategy[idx]=prev
                continue
            seen.add(v)
            cur_prob = computeProbability(potential_new_strategy)
            if cur_prob > local_max_prob:
                local_max_prob = cur_prob
                if local_max_prob > global_max_prob:
                    if local_max_prob > 0.27:
                        print("New local max probability at iteration:", iter, ",  "equal to :", local_max_prob, " with strategy: ", potential_new_strategy)
                    else:
                        print("New local max probability at iteration:", iter, ", "equal to :", local_max_prob)
                    global_max_prob = local_max_prob
                    global_max_strategy = potential_new_strategy
            else:
                potential_new_strategy[idx]=prev
        if local_max_prob > global_max_prob:
            global_max_prob = local_max_prob
            global_max_strategy = initial_strategy
    
    print("Global maximum of :", global_max_prob, "with strategy: ", global_max_strategy)


        
hillclimb(12000000,500)






