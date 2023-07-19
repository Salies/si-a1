# Atividade 1 do 2o Bimestre de Segurança da Informação
# FCT-UNESP, 2023
# Autor: Daniel Serezane

# Biblioteca para cifragem de strings

import numpy as np

# Técnica de Substituição
def subs(string):
    # Rotaciona cada caractere da string em 7 posições à esquerda
    # Exemplo: 'a' -> 't'
    for i in range(len(string)):
        val = ord(string[i]) - 7
        if val < 0:
            # Além de prevenir negativos, isso também ajuda a ficar dentro dos ASCII, facilitando a escrita do arquivo
            val += 256
        string = string[:i] + chr(val) + string[i+1:]
    return string
# Reversa
def rev_subs(string):
    # Rotaciona cada caractere da string em 7 posições à direita,
    # assim revertendo a cifragem por substituição
    # Exemplo: 't' -> 'a'
    for i in range(len(string)):
        val = ord(string[i]) + 7
        if val > 255:
            val -= 256
        string = string[:i] + chr(val) + string[i+1:]
    return string

# Técnica de Transposição
# Usando tranposição de colunas
def trans(string, key):
    matrix = []
    k = 0
    breaker = False
    # Cria uma matriz com o número de colunas igual à chave
    # A matriz não pode ser irregular, para mantermos os espaços
    while not breaker:
        matrix.append([])
        for _ in range(len(key)):
            if k < len(string):
                matrix[-1].append(string[k])
                k += 1
                continue
            breaker = True
            break

    if len(matrix[-1]) < len(key):
        for _ in range(len(key) - len(matrix[-1])):
            matrix[-1].append(' ')

    # Ordena as colunas da matriz de acordo com a ordem alfabética da chave
    # Exemplo: 'ezran' -> '1 4 3 0 2'
    key_ords = [ord(i) for i in key]
    key_ords_sorted = sorted(key_ords)
    for i in range(len(key)):
        val = key_ords_sorted[i]
        idx = key_ords.index(val)
        key_ords[idx] = i
    
    matrix = np.array(matrix)
    
    # Embaralha as colunas da matriz
    matrix = matrix[:, key_ords]
    
    # Retorna a matriz como uma string
    return ''.join(matrix.flatten('F'))

def rev_trans(string, key):
    # Calcula o tamanho da matriz
    n_cols = len(key)
    n_rows = len(string) // n_cols
    n_rows += 1 if len(string) % n_cols != 0 else 0

    # Recupera a matriz a partir da string
    matrix = np.array([i for i in string]).reshape(n_cols, n_rows).T

    # Calcula a ordenação proporcionada pela chave
    key_ords = [ord(i) for i in key]
    key_ords_sorted = sorted(key_ords)
    for i in range(len(key)):
        val = key_ords_sorted[i]
        idx = key_ords.index(val)
        key_ords[idx] = i

    # Desembaralha as colunas da matriz
    aux_matrix = np.empty_like(matrix)
    for i in range(len(key)):
        aux_matrix[:, key_ords[i]] = matrix[:, i]

    return ''.join(aux_matrix.flatten()).rstrip()

# Máquina de rotor único
class RotorMachine:
    def __init__(self, key):
        self.reset(key)

    def reset(self, key):
        # Inicializa o rotor
        self.rotor = [i for i in range(256)]
        # Embaralha o rotor de acordo com a chave
        for i in range(len(key)):
            np.random.seed(ord(key[i]))
            np.random.shuffle(self.rotor)

    def encrypt_char(self, char):
        out = chr(self.rotor.index(ord(char)))
        # Rotaciona o rotor
        self.rotor = self.rotor[1:] + self.rotor[:1]
        return out
    
    def decrypt_char(self, char):
        out = chr(self.rotor[ord(char)])
        # Rotaciona o rotor
        self.rotor = self.rotor[1:] + self.rotor[:1]
        return out


f = open('texto.txt', 'r')
msg = f.read()
f.close()
f = open('chave.txt', 'r')
key = f.read()
f.close()

t = trans(msg, key)
print(t)
r = rev_trans(t, key)
print(r)

rotor_machine = RotorMachine(key)

teste = []
for char in 'batata':
    teste.append(rotor_machine.encrypt_char(char))
print(''.join(teste))

rotor_machine.reset(key)

for char in teste:
    print(rotor_machine.decrypt_char(char))