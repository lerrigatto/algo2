# Dato un vettore ordinato V di n interi distinti
# determinare se esiste un indice i tale che V[i]=i
# in tempo O(log n)


def indice(V, i=0):
    if len(V) == 0:
        return None
    m = int(len(V)/2)
    if V[m] == m:
       return m
    if i>0 and V[m] == i+1:
        return V[m]
    if V[m] > m:
        return indice(V[m+1:], i+m)


#  i [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
V1 = [4, 3, 2, 1, 0]
V2 = [0, 1, 2]
V3 = [1, 2, 3, 4, 5, 6]
V4 =[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
V5 = [6, 1]
V6 = [1]
V7 = [0]
V8 = [9, 5, 2]
V9 = [11,9, 7, 3]

print(f" 2 -> {indice(V1)}")
print(f" 1 -> {indice(V2)}")
print(f" None -> {indice(V3)}")
print(f" 5 -> {indice(V4)}")
print(f" 1 -> {indice(V5)}")
print(f" None -> {indice(V6)}")
print(f" 0 -> {indice(V7)}")
print(f" 2 -> {indice(V8)}")
print(f" 3 -> {indice(V9)}")
