#!/bin/bash

# Verifica se foi fornecido um diretório como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <diretorio>"
    exit 1
fi

# Pergunta ao usuário se deseja excluir os arquivos
read -p "Deseja excluir os arquivos com a extensão .wav? (S/N): " resposta

if [[ "$resposta" == "S" || "$resposta" == "s" ]]; then
    # Exclui todos os arquivos .wav no diretório de origem
    find -type f -name "*.wav" -exec rm {} \;
    echo "Arquivos .wav excluídos."
else
    echo "Nenhum arquivo foi excluído."
fi

# Diretório de origem (pasta1)
dir_origem="/home/gracelli/databases/uaspeech/dysarthric/wavs_split"

# Diretório de destino (pasta2)
dir_destino="/home/gracelli/databases/uaspeech/dysarthric/data_split/wav"

# Copia o conteúdo do diretório de origem para os diretórios train, dev e test no diretório de destino
#cp -r "$dir_origem/train/$1" "$dir_destino/train"
#cp -r "$dir_origem/dev/$1" "$dir_destino/dev"
#cp -r "$dir_origem/test/$1" "$dir_destino/test"

find "$dir_origem/train/$1" -type f -execdir cp "{}" "$dir_destino/train" \;
find "$dir_origem/dev/$1" -type f -execdir cp "{}" "$dir_destino/dev" \;
find "$dir_origem/test/$1" -type f -execdir cp "{}" "$dir_destino/test" \;

echo "Conteúdo de $1 copiado para $dir_destino com sucesso!"