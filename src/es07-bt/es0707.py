# Dato n, si stampino tutte le matrici n x n di valori {a,b,c} tali che
# i simboli in ciascuna riga siano tutti uguali

def print_matr(M):
    for line in M:
        print(''.join(line))
    print("---")

def stampa_bt(n, i=0, M=[]):
    if i == n:
        print_matr(M)
        return
    for x in ['a','b','c']:
        T = [x] * n
        M.append(T)
        stampa_bt(n,i+1,M)
        M.pop()

stampa_bt(3)
