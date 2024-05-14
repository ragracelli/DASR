import os
import shutil
import argparse

# Configurar o analisador de argumentos
parser = argparse.ArgumentParser(description='Processar um diretório de arquivos WAV.')
parser.add_argument('diretorio', type=str, help='O diretório a ser processado')
args = parser.parse_args()

# Pasta raiz contendo os arquivos de áudio WAV
pasta_raiz = args.diretorio

# Ler o arquivo de texto ua_transcript.txt
def ler_transcricao(arquivo_transcricao):
    with open(arquivo_transcricao, "r") as f:
        linhas = f.readlines()
        return {linha.split()[0]: linha.strip() for linha in linhas}

# Criar um dicionário para associar cada arquivo WAV ao texto correspondente
arquivos_texto_relacionados = {}

# Percorrer os arquivos WAV na pasta e subpastas
for raiz, _, arquivos in os.walk(pasta_raiz):
    for arquivo_wav in arquivos:
        if arquivo_wav.lower().endswith(".wav"):
            # Extrair a chave do nome do arquivo WAV (assumindo que a chave está no formato "_C1_")
            chave = arquivo_wav.split("_")[2]

            # Ler o arquivo de transcrição
            transcricao = ler_transcricao(os.path.join(pasta_raiz, "/home/gracelli/databases/uaspeech/dysarthric/wavs/original/transcript/ua_vocab.txt"))

            # Verificar se a chave existe na transcrição
            if chave in transcricao:
                # Adicionar o arquivo WAV e o texto relacionado ao dicionário
                arquivos_texto_relacionados[arquivo_wav] = transcricao[chave]

# Criar o arquivo de saída "saida_txt.txt"
nome_arquivo_saida = "transcript/ua_transcript.txt"
with open(nome_arquivo_saida, "w") as f_saida:
    for arquivo_wav, texto in arquivos_texto_relacionados.items():
        texto = texto.split(' ')
        # Omitir a extensão ".wav" dos arquivos
        nome_arquivo_sem_extensao = os.path.splitext(arquivo_wav)[0]
        f_saida.write(f"{nome_arquivo_sem_extensao}{'|'}{texto[1]}\n")
    print(f"Arquivo de saída criado: {nome_arquivo_saida}")
