import librosa
import numpy as np
import os
import random
import soundfile as sf

def segment_audio(input_folder, output_folder, filename, n_cuts=2):
    # Carregar o arquivo de áudio
    y, sr = librosa.load(os.path.join(input_folder, filename))

    # Calcular a STFT do áudio
    D = librosa.stft(y)

    # Calcular a energia do áudio
    energy = np.abs(D)

    # Identificar as regiões de fala que têm entre 75% e 100% da energia máxima
    max_energy = np.max(energy)
    speech_regions = (energy > 0.75 * max_energy) & (energy <= max_energy)

    # Selecionar aleatoriamente pontos de corte dentro das regiões de fala
    speech_indices = np.nonzero(speech_regions.any(axis=0))[0]
    if len(speech_indices) < n_cuts:
        print(f"Warning: Not enough high-energy speech regions in {filename} to make {n_cuts} cuts.")
        return

    cut_points = random.sample(list(speech_indices), k=n_cuts)

    # Aplicar os cortes ao áudio
    for cut in cut_points:
        # Gerar um cut_length_ratio aleatório entre 2% e 10%
        cut_length_ratio = random.uniform(0.02, 0.1)
        cut_length = int(cut_length_ratio * D.shape[1])
        D[:, cut:cut+cut_length] = 0

    # Converter de volta para o domínio do tempo
    y = librosa.istft(D)

    # Salvar o áudio segmentado com sufixo "_aug.wav"
    output_filename = os.path.splitext(filename)[0] + "_aug.wav"
    sf.write(os.path.join(output_folder, output_filename), y, sr)

def process_audio_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.wav'):
                # Criar o diretório de saída, se não existir
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                # Segmentar o áudio
                segment_audio(root, output_dir, file)

if __name__ == "__main__":
    input_folder = "/home/gracelli/databases/uaspeech/dysarthric/wavs/original"
    output_folder = "/home/gracelli/databases/uaspeech/dysarthric/wavs/aug_prop"

    process_audio_folder(input_folder, output_folder)
    print("Arquivos transformados com sucesso!")
