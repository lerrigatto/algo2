# Dato un intero n, stampa tutte le stringhe palindromi lunghe 2n con valori
# {a,b}. L'algoritmo deve avere complessita' O(n2^n)

def specular(T):
    l = len(T)*2
    S = [None] * l
    for i,v in enumerate(T):
        S[i] = v
        j = l-i-1
        S[j] = v
    return S

def palindrome(n, i=0, T=[]):

    # Una stringa palindroma e` formata da una testa e una coda speculari.
    # Per generare una stringa, data la lunghezza fissata, si posizionano i due
    # caratteri in testa e coda insieme. Quindi si generano tutte le
    # combinazioni possibili.

    if i == n:
        print(''.join(specular(T)))
        return
    for c in ['a','b']:
        T.append(c)
        palindrome(n,i+1, T)
        T.pop()

print(palindrome(2))
