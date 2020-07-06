# Data una sequenza S di interi positivi e una sottosequenza S2
# La sottosequenza si definisce valida se per ogni coppia di elementi di S
# almeno un elemento e` presente in S2. Il valore di una sottosequenza e` la
# somma dei suoi elementi.
# Scrivere un algoritmo che, data S, calcoli il valore minimo di una
# sottosequenza massima in tempo O(n)

def subs(S):
    l = len(S)
    T = [float('inf')] * l
    for i in range(0,l):
        m = min(S[i-1],S[i])
        T[i] = m
        if m == S[i-1]:
            if i>1 and T[i-2] == T[i-1]:
                T[i] = S[i]
    sum = 0
    sub = []
    for i in T:
        if i not in sub:
            sub.append(i)
            sum = sum + i
    print(sub)
    return sum


test_arrays = [
    ([1,2,3,5,4,6,7], 15),
]


for i in range(len(test_arrays)):
    risultato = subs(test_arrays[i][0])
    if risultato is test_arrays[i][1]:
        print(f"Test {i}: Correct")
    else:
        print(f"Test {i}: Incorrect")
