# Atividade 1 do 2o Bimestre de Segurança da Informação
# FCT-UNESP, 2023
# Autor: Daniel Serezane

# Biblioteca para cifragem de strings

# Técnica de Substituição
def subs(string):
    # Rotaciona cada caractere da string em 7 posições à esquerda
    # Exemplo: 'a' -> 't'
    for i in range(len(string)):
        string = string[:i] + chr(ord(string[i]) - 7) + string[i+1:]
    return string
# Reversa
def rev_subs(string):
    # Rotaciona cada caractere da string em 7 posições à direita,
    # assim revertendo a cifragem por substituição
    # Exemplo: 't' -> 'a'
    for i in range(len(string)):
        string = string[:i] + chr(ord(string[i]) + 7) + string[i+1:]
    return string

# Técnica de Transposição
# Usando tranposição de colunas
def trans(string, key):
    n = len(string) / len(key)
    # arredonda n para cima
    if n % 1 != 0: n += 1
    n = int(n)
    # Cria uma matriz com o número de colunas igual à chave
    matrix = np.ndarray((n, len(key)), dtype='S1')
    print((n, len(key)))
    matrix.fill('')
    k = 0
    breaker = False
    for i in range(len(string)):
        if breaker: break
        for j in range(len(key)):
            if k == len(string):
                breaker = True
                break
            matrix[i][j] = string[k]
            k += 1

    # Ordena as colunas da matriz de acordo com a ordem alfabética da chave
    key_indexes = [ord(i) for i in key]
    key_indexes_sorted = sorted(key_indexes)
    col_idx = np.ndarray((len(key),), dtype='int')
    for i in range(len(key_indexes)):
        val = key_indexes_sorted[i]
        idx_val = key_indexes.index(val)
        col_idx[idx_val] = i

    # Embaralha as colunas da matriz
    matrix = matrix[:, col_idx]

    print(matrix)

    # to string
    out = matrix.flatten('F')
    out = [i.decode('utf-8') for i in out]
    out = ''.join(out)

    return out

def rev_trans(string, key):
    # Recuperando a matriz original...
    # Calculando as medidas
    n_cols = len(key)
    n_rows = len(string) // n_cols + int(len(string) % n_cols > 0)

    print((n_rows, n_cols))

    print(list(string[0:38]))

    # Cria uma matriz vazia
    matrix = np.ndarray((n_rows, n_cols), dtype='S1')
    matrix[0][0] = 'a'
    # Para cada coluna, acumula n_rows caracteres da string
    k = 0 # contador da string
    for i in range(n_cols):
        j = 0
        col = np.full((n_rows,), '', dtype='S1')
        while j < n_rows:
            if k == len(string): break
            col[j] = str(string[k])
            j += 1
            k += 1
        matrix[:,i] = col
    # Transforma a lista de arrays em uma matriz
    # cada elemento é uma coluna da matriz
    print(matrix)
    
    # Ordena as colunas da matriz de acordo com a ordem alfabética da chave
    # mas agora em ordem reversa
    '''key_indexes = [ord(i) for i in key]
    key_indexes_sorted = sorted(key_indexes, reverse=True)
    col_idx = np.ndarray((len(key),), dtype='int')
    for i in range(len(key_indexes)):
        val = key_indexes_sorted[i]
        idx_val = key_indexes.index(val)
        col_idx[idx_val] = i

    # Desembaralha as colunas da matriz
    matrix = matrix[:, col_idx]

    print(matrix)'''

    out = ''

    return out

msg = "Long ago, Xadia was one land rich in magic and wonder. In the old times, there were only the six Primal Sources of magic. The Sun. The Moon. The Stars. The Earth. The Sky. And the Ocean."
# remove espaços
#msg = msg.replace(' ', '')

t = trans(msg, 'ezran')

#print()

rev_trans(t, 'ezran')