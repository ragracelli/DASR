# split metadata.csv into two files -- train_filelist.txt and val_filelist.txt
# val_filelist.txt should randomly have 20% of the lines of text while train_filelist.txt should have about 80%

# O código original somente particionava a base de dados em treino e validação e não particionava os arquivos
# de áudio. Esta implementação particiona os audios em treino, validação e testes e armazena cada
# estrutura em um arquivo zip.

import csv
import random
import os
import subprocess
#input_path_metadata_csv = '/home/gracelli/databases/uaspeech/dysarthric/metadata.csv'
#input_path_wavs = './wavs/original/'
#output_path_train = '~/databases/uaspeech/dysarthric/data_split/train/'
#output_path_val = '~/databases/uaspeech/dysarthric/data_split/dev/'
#output_path_test = '~/databases/uaspeech/dysarthric/data_split/test/'

def make_dataset():
    # read in the metadata.csv file
    with open('/home/gracelli/databases/uaspeech/dysarthric/metadata.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\n')
        data = list(reader)
        print("Número de arquivos totais: ",len(data))
        # split the lines into three different arrays -- train test val
        # randomly select 20% of the lines to be in the val array
        train = []
        val = []
        val_tmp = []
        test = []
        tx = 0.2
        data_tmp = data.copy()
        for line in data:
            #if ((random.random() * tx) < tx) or (len(val_tmp) < len(data) * tx):
            if random.random() < tx:
                val_tmp.append(line[0].replace('./wavs/original/', ''))
            else:
                train.append(line[0].replace('./wavs/original/', ''))
                data_tmp.remove(line)
        print('Número de arquivos para treino: ', len(train))
        for line in data_tmp:
            if random.random() < 0.5:
                test.append(line[0].replace('./wavs/original/', ''))
            else:
                val.append(line[0].replace('./wavs/original/', ''))
        print('Número de arquivos para validação: ',len(val))
        print('Número de arquivos para teste: ',len(test))
        # save the files
        with open('trainfiles.txt', 'w') as f:
            for line in train:
                f.write(line + '\n')
        with open('valfiles.txt', 'w') as f:
            for line in val:
                f.write(line + '\n')
        with open('testfiles.txt', 'w') as f:
            for line in test:
                f.write(line + '\n')

    # zip all the wavs in the wavs folder into a zip file and save as train.zip and val.zip
    files = []
    #dir = []
    
    for line in train:
        #os.system(f'zip -r train.zip wavs/{line[0:10]}.wav')
        #print(line.split(',')[1])
        #files = list(os.system(f'find . -type f -name *{line.split(",")[1]}*'))
        ls_output = subprocess.check_output(["ls", "-1", "-R"])
        #grep_output = subprocess.check_output(["grep", line.split(",")[1]], input=ls_output)
        p = subprocess.Popen(["grep", line.split(",")[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        grep_output, _ = p.communicate(input=ls_output)
        if p.returncode == 1:
            grep_output = b""  # Define a saída como uma sequência de bytes vazia
        file_paths = grep_output.decode("utf-8").splitlines()
        #print(file_paths)
        for file in file_paths:
            dir = file.split("_")[0]
            voice = file.split("_")[1]
            if not os.path.isdir(f'~/databases/uaspeech/dysarthric/data_split/train/{dir}'):
                os.system(f'mkdir ~/databases/uaspeech/dysarthric/data_split/train/{dir}')
            else:
                print('Pasta já existe! Continuando...')
            if voice != 'B3':
                os.system(f'cp -v ~/databases/uaspeech/dysarthric/wavs/original/{dir}/{file} ~/databases/uaspeech/dysarthric/data_split/train/{dir}')
        #print(line[0:10])

    for line in val:
        # os.system(f'zip -r train.zip wavs/{line[0:10]}.wav')
        # print(line.split(',')[1])
        # files = list(os.system(f'find . -type f -name *{line.split(",")[1]}*'))
        ls_output = subprocess.check_output(["ls", "-1", "-R"])
        #grep_output = subprocess.check_output(["grep", line.split(",")[1]], input=ls_output)
        p = subprocess.Popen(["grep", line.split(",")[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        grep_output, _ = p.communicate(input=ls_output)
        if p.returncode == 1:
            grep_output = b""  # Define a saída como uma sequência de bytes vazia
        file_paths = grep_output.decode("utf-8").splitlines()
        # print(file_paths)
        for file in file_paths:
            dir = file.split("_")[0]
            voice = file.split("_")[1]
            if not os.path.isdir(f'~/databases/uaspeech/dysarthric/data_split/dev/{dir}'):
                os.system(f'mkdir ~/databases/uaspeech/dysarthric/data_split/dev/{dir}')
            else:
                print('Pasta já existe! Continuando...')
            if voice != 'B3':
                os.system(
                    f'cp -v ~/databases/uaspeech/dysarthric/wavs/original/{dir}/{file} ~/databases/uaspeech/dysarthric/data_split/dev/{dir}')
        #print(line[0:10])
    
    for line in test:
        # os.system(f'zip -r train.zip wavs/{line[0:10]}.wav')
        # print(line.split(',')[1])
        # files = list(os.system(f'find . -type f -name *{line.split(",")[1]}*'))
        ls_output = subprocess.check_output(["ls", "-1", "-R"])
        #grep_output = subprocess.check_output(["grep", line.split(",")[1]], input=ls_output)
        p = subprocess.Popen(["grep", line.split(",")[1]], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        grep_output, _ = p.communicate(input=ls_output)
        if p.returncode == 1:
            grep_output = b""  # Define a saída como uma sequência de bytes vazia
        file_paths = grep_output.decode("utf-8").splitlines()
        # print(file_paths)
        for file in file_paths:
            dir = file.split("_")[0]
            voice = file.split("_")[1]
            if not os.path.isdir(f'~/databases/uaspeech/dysarthric/data_split/test/{dir}'):
                os.system(f'mkdir ~/databases/uaspeech/dysarthric/data_split/test/{dir}')
            else:
                print('Pasta já existe! Continuando...')
            if voice == 'B3':
                os.system(
                    f'cp -v ~/databases/uaspeech/dysarthric/wavs/original/{dir}/{file} ~/databases/uaspeech/dysarthric/data_split/test/{dir}')
        # print(line[0:10])
    #os.system('zip -r train.zip wavs trainfiles.txt')
    #os.system('zip -r val.zip wavs valfiles.txt')

if __name__ == "__main__":
    make_dataset()
    print('done')