# Data una matrice binaria di dimensioni nXn 
# vogliamo verificare se nella matrice e` possibile 
# raggiungere la cella in basso a destra partendo 
# da quella in alto a sinistra senza mai toccare celle 
# che contengono il numero 1 e spostandosi solo in basso e a dx.
# Costo: O(n^2)

def recursive_path(M, cur_i=0, cur_j=0):

    # Sto nella cella (i,j), se posso spostarmi, ricorro.
    # Se non posso spostarmi restituisco False
    # Se non posso spostarmi e sono al bordo in basso a dx, restituisco True

    n = len(M[0])
    if cur_i == cur_j == n:
        # Bordo in basso a dx
        return True

    # Basso (i,j+1)
    next_i = cur_i
    next_j = cur_j+1

    if next_j > n:
        # Superato il bordo in basso
        return False

    if path(M, next_i, next_j):
        return True

    # DX (i+1,j)
    next_i = cur_i+1
    next_j = cur_j

    if next_i > n:
        # Superato il bordo a dx
        return False
    if path(M, next_i, next_j):
        return True

    return False

def dp_path(M):
    n = len(M[0])
    T = [[False] * n]*2

    for k in range(n):
        if M[0][k] == 1:
            T[1][k] =  False
        else:
            T[1][k] = True

    for i in range(n):
        for j in range(n):
            T[0][j] = T[1][j]
        for j in range(n):
            if M[i][j] == 1:
                T[1][j] = False
            else:
                # Check raggiungibilita:
                # Dall'alto e da sx
                if T[0][j] or T[1][j-1]:
                    T[1][j] = True
    print(T)
    return T[1][n-1]

def path(M):
    return dp_path(M)

test_arrays = [
    ([
     [0,0,0,0,0,1],
     [0,1,0,1,1,1],
     [0,0,0,1,0,1],
     [0,1,0,0,0,0],
     [0,0,0,0,1,0],
     [1,1,0,1,0,0],
    ], True),
    ([
     [0,0,0,0,0,0],
     [0,1,1,1,0,0],
     [0,1,0,0,0,0],
     [0,1,0,1,1,1],
     [0,1,0,0,0,0],
     [0,0,0,0,1,0],
    ], False),
]


for i in range(len(test_arrays)):
    risultato = path(test_arrays[i][0])
    if risultato is test_arrays[i][1]:
        print(f"Test {i}: Correct")
    else:
        print(f"Test {i}: Incorrect")
