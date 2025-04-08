import sys
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def cifrar(arquivo_entrada, chave):
    chave = chave.encode("utf-8").ljust(32, b'\0')[:32]
    iv = get_random_bytes(16)

    with open(arquivo_entrada, 'rb') as f:
        dados = f.read()

    cipher = AES.new(chave, AES.MODE_CBC, iv)
    dados_cifrados = cipher.encrypt(pad(dados, AES.block_size))

    arquivo_saida = arquivo_entrada + ".enc"
    with open(arquivo_saida, 'wb') as f:
        f.write(iv + dados_cifrados)

    print(f"Arquivo cifrado salvo como: {arquivo_saida}")

def decifrar(arquivo_entrada, chave):
    chave = chave.encode("utf-8").ljust(32, b'\0')[:32]

    with open(arquivo_entrada, 'rb') as f:
        iv = f.read(16)
        dados_cifrados = f.read()

    cipher = AES.new(chave, AES.MODE_CBC, iv)
    dados = unpad(cipher.decrypt(dados_cifrados), AES.block_size)

    arquivo_saida = arquivo_entrada.replace(".enc", ".dec")
    with open(arquivo_saida, 'wb') as f:
        f.write(dados)

    print(f"Arquivo decifrado salvo como: {arquivo_saida}")

def main():
    if len(sys.argv) != 4:
        print("Uso: python AES.py <cifrar|decifrar> <caminho_arquivo> <chave>")
        sys.exit(1)

    operacao, caminho_arquivo, chave = sys.argv[1], sys.argv[2], sys.argv[3]

    if not os.path.isfile(caminho_arquivo):
        print("Arquivo não encontrado!")
        sys.exit(1)

    if operacao == "cifrar":
        cifrar(caminho_arquivo, chave)
    elif operacao == "decifrar":
        decifrar(caminho_arquivo, chave)
    else:
        print("Operação inválida! Use 'cifrar' ou 'decifrar'.")

if __name__ == "__main__":
    main()
