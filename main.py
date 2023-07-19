# Atividade 1 do 2o Bimestre de Segurança da Informação
# FCT-UNESP, 2023
# Autor: Daniel Serezane

# Programa principal

from sombra import master_encrypt, master_decrypt

f = open('texto.txt', 'r')
message = f.read()
f.close()

print('Mensagem original: ', message)
print()

f = open('chave.txt', 'r')
key = f.read()
f.close()

print('Chave: ', key)
print()

encrypted_message = master_encrypt(message, key)

print('Mensagem criptografada: ', encrypted_message)
print()

decrypted_message = master_decrypt(encrypted_message, key)

print('Mensagem descriptografada: ', decrypted_message)