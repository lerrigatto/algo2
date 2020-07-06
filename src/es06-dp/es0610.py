# Data una sequenza di interi positivi X lunga n, e un intero positivo s
# trova la sottosequenza massima di somma s in tempo O(ns)


def seq_max(X,s):
    T = [[0] * len(X)] * int(s+1)

    for sum in range(1,s+1):
        cur_sum = 0
        for n in range(len(X)):
            if cur_sum + X[n] <= sum:
                cur_sum = cur_sum + X[n]
                T[n] = sum
    return T[s][n]

test_arrays = [
    ([5,2,2,6,1,7,3,5,11,3,6], 25, True),
    ([3,3,5,13,3,5], 28, False),
]


for i in range(len(test_arrays)):
    taken = [False] * len(test_arrays[i][0])
    risultato = seq_max(test_arrays[i][0], test_arrays[i][1], )
    if risultato is test_arrays[i][2]:
        print(f"Test {i}: Correct")
    else:
        print(f"Test {i}: Incorrect")
