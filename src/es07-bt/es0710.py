# Dato un intero n si stampino i quadrati magici di ordine n.
# Un quadratro magico e` una matrice n x n contenente tutti i valori
# {1,...,n^2} tali che la somma di ogni riga, colonna, e delle due diagonali
# sia la stessa.
# Tale somma e` uguale a (n(n^2+1)/2

def print_matr(M):
    for line in M:
        print(''.join(str(line)))
    print("---")

def magic_sq(n, M, T, S, i=0, j=0):
    lsum = (n*(n*n+1))/2
    if i == n:
        print(S)
        print_matr(M)
        return
    for v in range(1,n*n+1):
        if not T[v]:
            diag = None
            diag_ok = True
            if i==j:
                diag = 2*n
            if i+j == n:
                diag = 2*n + 1
            if diag and S[diag]+v > lsum:
                diag_ok = False

            if diag_ok and \
                S[i]+v <= lsum and \
                S[n+j]+v <=lsum:

                if diag_ok and diag:
                    S[diag] = S[diag] + v
                S[i] = S[i] + v
                S[n+j] = S[n+j] + v
                M[i][j] = v
                T[v] = True
                if j < n-1:
                    # Continua sulla riga
                    magic_sq(n,M,T,S,i,j+1)
                else:
                    magic_sq(n,M,T,S,i+1)
                T[v] = False
                M[i][j] = 0
                S[i] = S[i] - v
                S[n+j] = S[n+j] - v
                if diag_ok and diag:
                    S[diag] = S[diag] - v

n=3
M = [[0] * n for _ in range(n)]
T = [False] * int(n*n+1)
S = [0] * int(2*n +2)
magic_sq(n, M, T, S)
