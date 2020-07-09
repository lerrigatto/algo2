# Pozzi
Ci sono n case, indicate con gli interi i = 0, 1, . . . , n − 1, ognuna delle quali necessita di una fornitura d’acqua.
La costruzione di un pozzo nella casa i costa P[i] e la costruzione di una tubazione fra le case i e j costa M[i][j]
(M[i][j] = +∞ se non c’è possibilità di stendere una tubazione tra i e j ).
Una casa risulta fornita d’acqua se vi è stato costruito un pozzo o l’acqua vi giunge da un pozzo di un altra casa tramite tubazioni.
Dare lo pseudo-codice di un algoritmo che determina le case in cui costruire i pozzi e le tubazioni da costruire per dare una fornitura d’acqua a tutte le case minimizzando il costo totale.
Il costo totale è dato dalla somma dei costi dei pozzi e delle tubature costruiti.
L’algoritmo deve avere complessità O(n2 + m log n). Motivare bene la correttezza dell’algoritmo.

# Pseudo

```
P[n] := Lista di nodi pesati
M[n,n] := Matrice simmetrica degli archi pesati
G := Graph(P, M) # Grafo indiretto con archi e nodi pesati (matrice vs liste adj?)
F := Kruskal(G) # Grafo contenente la foresta di MST generate da Kruskal
### kruskal costa O(m log n) se G e` con liste di adiacenza o O(n^2) se con matrici
### Inizializzare G con matrici costa O(1) mentre con liste costa O(n^2)
### Il costo di G ed F e` O(n^2)

discovederd[n] = False # Lista dei nodi visitati
### Costo O(n)

out_edges = [] # Lista delle tubature da costruire
total_cost = 0 # Costo finale di pozzi e tubature
built = [] # Lista dei pozzi da costruire

while MST in F:
### Al massimo possono esistere n MST (nessun arco)
### Costo O(n)

  e := min(cost(MST.edge))
  
  if e == null:
  # Se l'MST non ha archi, conterra' un solo nodo, che sara' un pozzo da costruire
    built.add(MST.v)
    total_cost += cost(MST.v)
    continue

  v := min(cost(F.adj(e))) # Il meno costoso dei nodi dell'arco e
  
  # Inizializzazioni
  candidate = v
  traverse_cost = cost(v) + cost(e)
  out_edges.add(e)
  
  # Visita dell'albero
  DFS(v, e, traverse_cost, candidate)
  ### Costo O(n+m)
  ### Ogni nodo attraversato nella DFS non verra' attraversato dal while esterno
  
  # Salvo i costi di ciascun albero
  # Aggiungo il pozzo candidato ai costruiti
  total_cost += traverse_cost
  total_cost += cost(candidate)
  built.add(candidate)

---

# Questa DFS visita tutti i pozzi del MST e taglia via gli alberi che possono essere raggiunti dal pozzo di costo minimo.
DFS(v, e, traverse_cost, candidate):
  discovered(v) = True
  if (cost(v) + cost(e)) <= traverse_cost:
  # Se il costo del pozzo e della tubazione sono inferiori o uguali al costo speso per arrivarci
  # Promuovo il pozzo che sto visitando a candidato per la costruzione
  # Suppongo la tubazione di arrivo gia' inserita nella lista delle tubazioni da utilizzare

    candidate = v
    total_cost += traverse_cost
    traverse_cost = 0
  
    if cost(v) < cost(e)
    # Se, inoltre, il costo del pozzo e` inferiore al costo della tubazione, posso rimuovere tutta la sezione dall'albero
    # Oltre questo pozzo non e` possibile ottenere costi inferiori o uguali, quindi va costruito in ogni caso.
    # Poiche` lo raggiungiamo con lo stesso costo, rimuovendo la tubazione che lo raggiunge creiamo un nuovo MST
    # Il loop iniziale su F ci assicura che visiteremo questo nodo in futuro
      F.remove(e)
  else
  # Se il costo di costruzione del pozzo e dell'arco sono superiori, si aggiunge l'arco/tubazione
    out_edges.add(e)
    traverse_cost += cost(e)

  # Si continua la visita sui pozzi
  for (f,w) in F.adj(v):
    if not discovered(f):
      DFS(w, f, traverse_cost, candidate)

```
