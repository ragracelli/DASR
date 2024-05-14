import os
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample
import soundfile as sf

def add_white_noise(audio, factor=10):
    try:
        sample_rate, data = wavfile.read(audio)
    except ValueError:
        print(f"Erro ao ler o arquivo {audio}. Ignorando.")
        return None, None

    noise = np.random.normal(0, 1, len(data))
    noisy_data = data + factor * noise
    return sample_rate, noisy_data

def apply_time_stretch(audio, stretch_factor=0.9):
    try:
        sample_rate, data = wavfile.read(audio)
    except ValueError:
        print(f"Erro ao ler o arquivo {audio}. Ignorando.")
        return None, None

    num_samples = len(data)
    new_num_samples = int(num_samples / stretch_factor)
    stretched_data = resample(data, new_num_samples)
    return sample_rate, stretched_data

def normalize_audio(data):
    max_amplitude = np.max(np.abs(data))
    normalized_data = data / max_amplitude
    return normalized_data

def process_audio_folder(input_folder, output_folder):
    for foldername in os.listdir(input_folder):
        input_subfolder = os.path.join(input_folder, foldername)
        print(input_subfolder)
        if os.path.isdir(input_subfolder):
            output_subfolder = os.path.join(output_folder, foldername)
            os.makedirs(output_subfolder, exist_ok=True)

            for filename in os.listdir(input_subfolder):
                if filename.endswith(".wav"):
                    input_path = os.path.join(input_subfolder, filename)
                    output_path = os.path.join(output_subfolder, filename.replace(".wav", "_aug.wav"))

                    sample_rate, noisy_data = add_white_noise(input_path)
                    if sample_rate is None:
                        continue

                    sample_rate, stretched_data = apply_time_stretch(input_path)
                    if sample_rate is None:
                        continue

                    normalized_noisy_data = normalize_audio(noisy_data)
                    normalized_stretched_data = normalize_audio(stretched_data)

                    sf.write(output_path, normalized_noisy_data, sample_rate)
                    sf.write(output_path, normalized_stretched_data, sample_rate)

if __name__ == "__main__":
    input_folder = "/home/gracelli/databases/uaspeech/dysarthric/wavs/aug_prop"
    output_folder = "/home/gracelli/databases/uaspeech/dysarthric/wavs/aug_plus_prop"

    process_audio_folder(input_folder, output_folder)
    print("Arquivos transformados com sucesso!")
