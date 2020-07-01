# Dato un vettore V di n>=2 interi con V[0] < V[n]
# si definisce gap un indice i [0,n] tale che V[i] < V[i+1]
# si scriva un algortimo che trovi un gap in tempo O(log n)

def gap(V, i=0):
    if len(V) < 2:
        return -1
    m = int(len(V)/2)-1
    #print(f"{len(V)} - {m} - {V}")
    if V[m] < V[m+1]:
        return i+m
    if V[0] < V[m]:
        return gap(V[0:m], i+m+1)
    else:
        return gap(V[m+1:], i+m+1)

test_arrays = [
    #   0    1    2    3    4    5    6    7    8
    [ -10,  -9,  10,   5,   6,   6,   7,  31],  # Array ordinato
    [],  # Array vuoto
    [   1,   1,   1,   1],   # Array per cui non vale che v[len(v)-1] > v[0]
    [   1,   2, -10, -11],   # Array per cui non vale che v[len(v)-1] > v[0]
    [   0,   5,   4,   0,   3,   1,   1,   1,   1],  # Array non ordinato
    [   0,   5,   4,   0, -10, -11,   1,   1,   1],  # Array non ordinato
    [9, 9, 4, 3, 2, 11], # gap
    [1, 2, 3, 4], # all gaps
    [2, 2, 2, 2], # no gaps
    [5, 4, 3, 2, 6], #last gap

]


for i in range(len(test_arrays)):
    risultato = gap(test_arrays[i])
    if risultato < 0:
        print(test_arrays[i], "non ha gap")
    else:
        print("Uno dei gap di", test_arrays[i], "occorre all’indice", risultato,
              ": [", test_arrays[i][risultato], ",", test_arrays[i][risultato+1], "]")
