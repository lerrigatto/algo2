# Si stampino tutte le sequenze di lunghezza n composte dagli interi {1,2,3,4}
# tali che due numeri adiacenti distino almeno 2
# L'algoritmo deve avere costo O(nS(n))

def seq_dist(n, i=0, T=[]):
    if i == n:
        print(T)
        return
    for c in [1,2,3,4]:
        if i>0:
            if abs(T[i-1]-c) >=2:
                T.append(c)
                seq_dist(n,i+1,T)
                T.pop()
        else:
            T.append(c)
            seq_dist(n,i+1,T)
            T.pop()

seq_dist(4)
