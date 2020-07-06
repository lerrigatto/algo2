# Dato un insieme di m stringhe binarie dette primitive
# ed una stringa X di n bit;
# calcolare se la stringa X e` ottenibile tramite concatenazione di m
# L'algoritmo deve avere tempo O((m+n)l), dove l e` la lunghezza massima di m

def primitive(M, X):

    # Creo una tabella nXl e salvo quale primitiva fa il match
    # Scorro la tabella per righe e se ho fatto almeno un match fino a quel
    # momento cerco il prossimo.
    # Restituisco True se sono arrivato prefettamente alla fine.

    l = 0
    lmin = float('inf')

    # We need the max and min length of the primitives.
    # The max length l is increased by 1 for convenience
    for m in M:
        lm = len(m)
        if lm > l:
            l = lm
        if lm < lmin:
            lmin = lm
    l = l+1

    n = len(X)
    T = [[False] * l for i in range(n)]

    for m in M:
        lm = len(m)
        if X[0:lm] == m:
            for j in range(lm):
                T[j][lm] = True

    for i in range(1,n):
        # Row 1 is initialized outside
        for lj in range(lmin,l):
            # We can skip the colums of non used legths
            if T[i][lj] is False and T[i-1][lj] is True:
                # We are looking for non explored lines and
                # lines where the previous was a match
                for m in M:
                    # We check every possible primitive
                    lm = len(m)
                    if X[i:i+lm] == m:
                        # If it's a match, we set as True all the lines
                        # matching
                        for j in range(lm):
                            T[i+j][lm] = True

    # This is ugly but we need to check for every possible True in the last
    # line
    for i in T[n-1]:
        if i is True:
            return True
    return False

test_arrays = [
    (['01','10','011','101'], "0111010101", True),
    (['01','10','011','101'], "1001100110", True),
    (['01','10','011','101'], "0011010101", False),
    (['0','01','10','011','101'], "0011010101", True),
    (['01','10','011','101'], "0110001", False)
]


for i in range(len(test_arrays)):
    taken = [False] * len(test_arrays[i][0])
    risultato = primitive(test_arrays[i][0], test_arrays[i][1])
    if risultato is test_arrays[i][2]:
        print(f"Test {i}: Correct")
    else:
        print(f"Test {i}: Incorrect")
