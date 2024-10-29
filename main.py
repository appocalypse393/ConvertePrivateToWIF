import hashlib
import base58

def convert_to_wif(private_key_hex):
    # Passo 1: Adiciona prefixo para chave privada
    prefix = '80' + private_key_hex

    # Passo 2: Adiciona 0x01 para compactar
    prefix_compact = prefix + '01'

    # Passo 3: Cria o checksum
    hash1 = hashlib.sha256(bytes.fromhex(prefix_compact)).hexdigest()
    hash2 = hashlib.sha256(bytes.fromhex(hash1)).hexdigest()
    checksum = hash2[:8]

    # Passo 4: Cria o WIF completo
    wif = prefix_compact + checksum

    # Passo 5: Codifica em Base58
    wif_encoded = base58.b58encode(bytes.fromhex(wif)).decode('utf-8')

    return wif_encoded

def convert_keys_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        private_keys = file.readlines()

    with open(output_file, 'w') as file:
        for key in private_keys:
            key = key.strip()  # Remove espaços em branco e quebras de linha
            if len(key) == 64:  # Verifica se o formato da chave está correto
                wif_key = convert_to_wif(key)
                file.write(wif_key + '\n')
            else:
                file.write(f"Chave inválida: {key}\n")

# Exemplo de uso
input_file = 'private_keys.txt'  # Arquivo de entrada com as chaves privadas
output_file = 'wif_keys.txt'     # Arquivo de saída para as chaves WIF

convert_keys_from_file(input_file, output_file)
print(f"Conversão completa. Chaves WIF salvas em {output_file}.")
