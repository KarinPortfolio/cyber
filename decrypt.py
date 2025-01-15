import os
import pyaes

## abre o arquivo criptografado
file_name = "meuarquivo.txt.estearquivofoicriptografado"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave de descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover arquivo criptografado
os.remove(file_name)

## cria arquivo descriptografado
new_file = "meuarquivo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
