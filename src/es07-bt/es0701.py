# Dato un interno n
# Si stampino tutte le stringhe di lunghezza n con simboli {a,b}
# tali che i blocchi di simboli a di lunghezza massima siano pari

# Per n=3:
# Tutte le stringhe (2^n):
# aaa,aab,aba,abb,baa,bab,bba,bbb
# Stringhe di output:
# aab,aba,baa,abb

def stampa_ab_naive(max_len, i=0, abstr=[]):
    # ricorsivamente
    # se la lista non e` di lunghezza n
    #   aggiungi a, ricorri
    #   rimuovi a, aggiungi b, ricorri
    # se la lista e` di lunghezza n
    #   stampala
    if i == max_len:
        # Conta le a ?!
        str = ''.join(abstr)
        if str.count('a') % 2 == 0:
            print(f"{str}")
        return
    else:
        abstr.append('a')
        stampa_ab_naive(max_len, i+1, abstr)
        abstr.pop()
        abstr.append('b')
        stampa_ab_naive(max_len,i+1, abstr)
        abstr.pop()

def stampa_ab_bt(max_len, i=0, count_a=0, abstr=[]):
    # Come il naif ma sfronda prima della ricorsione fa il conto delle a
    # Passa variabile di appoggio per il numero di a

    return

def main():
    n = 3
    stampa_ab_naive(n)
    stampa_ab_bt(n)

main()
