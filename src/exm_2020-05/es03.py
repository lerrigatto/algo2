# Stampa le sequenze di lunghezza n sull'alfabeto {0,1,2} in cui non appaiono
# cifre pari adiacenti.

def stampa_even(n,T, i=0, sum=0):
    if n==i:
        print(''.join(str(x) for x in T))
        return sum
    for x in [0,1,2,3,4,5,6,7,8,9]:
        if i > 0 and T[i-1]%2==0 and x%2 == 0:
            continue
        T[i] = x
        stampa_even(n,T,i+1,sum+1)

n = 2
T = [None] * n
print(stampa_even(n,T))
