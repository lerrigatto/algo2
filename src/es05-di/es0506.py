# Dato un vettore V, si definisce spessore la differenza tra
# il massimo ed il minimo valore. Si crei un algoritmo che,
# dato V di n interi e C intero, trovi un sottovettore
# di lunghezza massima tra quelli di spessore al piu' C.


def max_sub(V, C=0):
    max_sum = 0
    max_start = None
    max_end = None
    cur_sum = 0

    for cur_end, value in enumerate(V):
        if cur_sum > 0 and value > V[cur_end-1]:
            cur_sum = cur_sum + value
            thick = V[cur_end] - V[cur_start]
            if cur_sum > max_sum:
                max_sum = cur_sum
                max_start = cur_start
                max_end = cur_end + 1
        else:
            cur_sum = value
            cur_start = cur_end

    return V[max_start:max_end]

test_arrays = [
    #   0    1    2    3    4    5    6    7    8
    ([], 0),  # Array vuoto
    ([0, -1, 1, 4, 2], 3), # 1,4
    ([1, 2, 3, 4, 5, -1, 2, 7], 6), #1-5
    ([2,7,1,2,3,4,5],4), #1-5
    ([-1,2,-1,4,5,0], 2), #4-5?
]


for i in range(len(test_arrays)):
    risultato = max_sub(test_arrays[i][0], test_arrays[i][1])
    if len(risultato) < 1:
        print(test_arrays[i], "No subarray")
    else:
        print(f"****** {risultato} -> {test_arrays[i]}")
