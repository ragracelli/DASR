import os
import shutil

# Defina os caminhos das pastas
pasta1 = r"/home/gracelli/databases/uaspeech/dysarthric/data_split/wav/train/"
pasta2 = r"/home/gracelli/databases/uaspeech/dysarthric/wavs/aug_plus_prop/M09/"

# Lista de arquivos na pasta 1
arquivos_pasta1 = os.listdir(pasta1)

# Lista de arquivos na pasta 2
arquivos_pasta2 = os.listdir(pasta2)

# Itera sobre os arquivos na pasta 2
for arquivo2 in arquivos_pasta2:
    if arquivo2.endswith("_aug.wav"):
        # Remove o sufixo "_aug.wav" para comparar com os arquivos na pasta 1
        nome_base = arquivo2[:-8]
        for arquivo1 in arquivos_pasta1:
            if arquivo1.startswith(nome_base):
                # Copia o arquivo da pasta 2 para a pasta 1 com o sufixo "_aug.wav"
                caminho_arquivo2 = os.path.join(pasta2, arquivo2)
                caminho_destino = os.path.join(pasta1, arquivo2)
                shutil.copy(caminho_arquivo2, caminho_destino)
                print(f"Arquivo {arquivo2} copiado para {caminho_destino}")
                break  # Para evitar copiar o mesmo arquivo várias vezes

print("Concluído!")