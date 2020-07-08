# Dato n, si stampino tutte le matrici di interi n x n tali che
# le righe e le colonne della matrice siano in ordine crescente

def print_matr(M):
    for line in M:
        print(''.join(str(line)))
    print("---")

def stampa_bt(n, M, i=0, j=0, c=0):
    if i == n:
        print_matr(M)
        return
    else:
        if c>0:
            M[i][j] = c
            # Controllo se sono a fine riga
            if j < n -1:
                stampa_bt(n,M,i,j+1)
            else:
                stampa_bt(n,M,i+1,0)
        else:
            for x in range(1,n+2):
                # Nella posizione 0,0 non ho vicini da controllare
                if i==0 and j==0:
                    stampa_bt(n,M,i,j,x)

                order = True
                # Controllo prima riga, ogni colonna
                if i == 0 and j>0:
                    order &= M[i][j-1] <= x
                # Controllo riga e colonna centrali
                if i>0 and j>0:
                    order &= M[i-1][j] <= x and M[i][j-1] <= x
                # Controllo prima colonna
                if i>0 and j==0:
                    order &= M[i-1][j] <= x and M[i][j+1] <= x

                if order:
                    stampa_bt(n,M,i,j,x)

n=3
M = [[0] * n for _ in range(n)]
stampa_bt(n, M)
