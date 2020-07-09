# Sia n un intero, si stampi il numero di sequenze di interi lunghe n
# tali che non vi appaiano due cifre pari adiacenti.
# L'algoritmo deve avere tempo O(n)

def even_seqs(n):
    sum = 0
    T = [[0] * int(n+1) for _ in range(10)]
    for i in range(1,n+1):
        for j in range(10):
            if i > 0 and j%2 == 0:
                if T[j][i-1] % 2 == 0:
                    continue
                else:
                    T[j][i] = j
                    sum = sum +1
            else:
                T[j][i] = j
                sum = sum + 1
            print(i," ",j)
    print(T)
    return sum


print(even_seqs(1))
print(even_seqs(2))
print(even_seqs(3))
