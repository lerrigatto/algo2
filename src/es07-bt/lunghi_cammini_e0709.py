# Data una matrice n x n le cui celle sono numerate da 1 a n^2
# Si calcoli la lunghezza massima possibile per cammini che toccano
# le celle con numerazione crescente e incremento di 1
# I cammini possono partire da qualunque cella.
# Ogni spostamento avviene solo su celle adiacenti verticalmente o
# orizontalmente.
# Le matrici sono numerate a caso
# Restituisce il numero di nodi percorsi


def max_path(mat):
    # Creo un array di appoggio
    # Scorro la matrice (sia i da zero a n^2)
    #   Pongo array[i] a True se l'elemento i+1 e` raggiungibile
    #   Pongo array[i] a False altrimenti
    # Conto la massima sottosequenza nell'array di appoggio

    # Costruisci array di appoggio
    mat_len = len(mat)
    T = [ 0 for _ in range(n*n)]
    for i in range(n):
        for j in range(n):
        T_index = mat[i][j] -1
        # RECHECK THIS IF
        # THIS IS A WRONG COPYPASTE
        if  j < n-1 and mat[i][j+1] == mat[i][j]+1 or \
            i < n-1 and mat[i+1][j] == mat[i][j]+1 or \
            j > n-1 and mat[i-1][j] == mat[i][j]+1 or \
            j > n-1 and mat[i][j-1] == mat[i][j]+1 :
            T[T_index] = 1
        else:
            T[T_index] = 0

    # Trova massima sottosequenza in T

    max_path = 0
    return max_path

def main():
    B = [[9,7,6],
         [8,2,5],
         [1,3,4]
        ]
    print(B)

    max_path(B)
main()
