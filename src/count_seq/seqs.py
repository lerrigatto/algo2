import math

# Siano 3 interi positivi x1, x2, x3 e n intero
# Si scriva un algoritmo che in tempo O(n) restituisca il numero di sequenze
# composte dai 3 interi la cui somma sia n.

def seq(n, x1, x2, x3, sum=0, i=0):
    if sum == n:
        return 1
    elif sum > n:
        return 0
    else:
        return  seq(n, x1, x2, x3, sum+x1) + \
                seq(n, x1, x2, x3, sum+x2) + \
                seq(n, x1, x2, x3, sum+x3)

def main():
    n=10
    x1=2
    x2=4
    x3=8

    print(seq(n, x1, x2, x3))

main()
