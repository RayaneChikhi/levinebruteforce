from itertools import product

def generate_strategies(n):
    return ((1,) + mid + (1,) for mid in product(range(1, n + 1), repeat=vn - 2))

def computeGame(strategyA, strategyB, stack_A, stack_B):
    a = stack_A[strategyA[possible_hat_configs.index(stack_B)] - 1]
    b = stack_B[strategyB[possible_hat_configs.index(stack_A)] - 1]
    return min(a, b)

def bruteforce(n, optimalProb):
    optimalStrategies = set()
    numOptimalStrats = 0    
    cur_max = 0
    curiter = -1
    
    for strategyA in generate_strategies(n):
        curiter += 1
        print(f"{(curiter / total_strategies) * 100:.2f} %")
        S = 0
        for stackA in possible_hat_configs:
            for stackB in possible_hat_configs:
                S += computeGame(strategyA, strategyA, stackA, stackB)
        probability = S / dn
        if probability == optimalProb and ((strategyA, strategyA) not in optimalStrategies):
            optimalStrategies.add(strategyA)
            numOptimalStrats += 1
        if probability > cur_max:
            cur_max = probability
    
    return cur_max, numOptimalStrats, optimalStrategies

n = 4
possible_hat_configs = tuple(product([0, 1], repeat=n))
total_strategies = n ** (2 ** n)
vn = 2**n
dn = 2**(2*n)
optimalProbability = 0.34765625    
best_probability, numOptimalStrats, optimalStrategies = bruteforce(n, optimalProbability)
print(f"Best success probability for n={n}: {best_probability}")
print("Number of optimal strategies (modulo the first value and the last one):", numOptimalStrats)
print("Optimal strategies:", optimalStrategies)
