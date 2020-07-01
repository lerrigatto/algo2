# Data una matrice quadratra binaria M di dimensione nXn
# si trovi il massimo m per cui la matrice quadrata mXm
# composta di soli uno risulti sottomatrice di M


def matrix(M):
    return '\n'.join([' '.join([str(i) for i in row]) for row in M])

def max_sub(M, m):
    # print(f"{matrix(M)} - {m}")
    # creo una matrice di appoggio in cui mi salvo la dimensione della
    # sottomatrice per ogni cella.
    # Un elemento [i,j] della sottomatrice e` 1+diag-prec se i verticali sono
    # entrambi 1
    # [i,j] = 1 + [i-1, j-1] se [i,j], [i-1,j], [i,j-1]!=0 altrimenti 1

    sub_max = 0

    prev_row = M[0]
    cur_row = [0] * len(prev_row)
    cur_row[0] = M[1][0]

    for i in range(1, len(M[0])):
        for j in range(1,len(M[0])):
            if M[i][j] == 1:
                cur_row[j] = 1
                if cur_row[j-1] > 0 and prev_row[j] > 0:
                    cur_row[j] = 1 + prev_row[j-1]
                    if cur_row[j] > sub_max:
                        sub_max = cur_row[j]
            else:
                cur_row[j] = 0
        prev_row = cur_row
        cur_row = [0] * len(prev_row)
        cur_row[0] = M[i][0]

    return sub_max

test_arrays = [
    ([[1,0,1,1,1],
      [1,1,1,1,1],
      [1,1,1,0,1],
      [1,1,1,1,1],
      [0,1,0,1,1]
    ],3),
    ([[1,0,1,1,0,1],
      [1,0,1,1,1,1],
      [0,1,1,1,1,1],
      [1,0,1,1,1,1],
      [1,1,1,1,1,1],
      [0,0,1,0,1,1]
    ],4),
    ([[1,0,1,1,0,1],
      [1,1,0,1,1,1],
      [1,1,0,1,1,1],
      [1,1,0,1,1,1],
      [1,1,0,1,0,1],
      [1,0,0,0,0,0]
    ],3),
    ([[1,0,1,1,0,1],
      [1,1,0,1,1,1],
      [1,1,0,1,0,1],
      [1,1,1,0,0,1],
      [1,1,0,1,1,1],
      [1,1,0,1,0,1]
    ],2),
]


for i in range(len(test_arrays)):
    risultato = max_sub(test_arrays[i][0], test_arrays[i][1])
    if not risultato:
        print(f"{matrix(test_arrays[i][0])} No submatrix of size {test_arrays[i][1]}")
    else:
        print(f"****** {risultato} -> {test_arrays[i][1]}")
