# 🔐 Criptografar com AES

Este programa permite **criptografar e descriptografar** arquivos usando o algoritmo **AES em modo CBC**.

## 📦 Requisitos

- Python 3.x
- Biblioteca `pycryptodome`

### Instalação da biblioteca

Execute o seguinte comando para instalar:

```bash
pip install pycryptodome
```

---

## 🚀 Como usar

O programa recebe **3 parâmetros** na linha de comando:

1. `cifrar` ou `decifrar`
2. Caminho do arquivo
3. Chave de criptografia (string)

### 🔒 Cifrar um arquivo

```bash
python AES.py cifrar <caminho_arquivo> <chave>
```

**Exemplo:**

```bash
python AES.py cifrar exemplo.txt minha_senha
```

- O arquivo criptografado será salvo como `exemplo.txt.enc`.

---

### 🔓 Decifrar um arquivo

```bash
python AES.py decifrar <caminho_arquivo_cifrado> <chave>
```

**Exemplo:**

```bash
python AES.py decifrar exemplo.txt.enc minha_senha
```

- O arquivo decifrado será salvo como `exemplo.txt.dec`.

---

## 🔐 Observações

- A chave é ajustada automaticamente para 32 bytes (AES-256). Se for menor, é preenchida com `\0`; se for maior, é cortada.
- O IV (vetor de inicialização) é gerado automaticamente e salvo junto com o arquivo criptografado (nos primeiros 16 bytes).
- O algoritmo usado é AES com modo CBC e padding padrão (PKCS7).

---

## 📄 Licença

Uso livre para fins educacionais, acadêmicos ou comerciais.
```
