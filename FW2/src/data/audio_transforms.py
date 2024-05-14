import torch
import torchaudio
from torchaudio.transforms import AddNoise, TimeStretch

class AudioTransforms:
    def __init__(self, snr=10.0, stretch_factor=0.9):
        self.add_noise_transform = AddNoise()
        self.time_stretch_transform = TimeStretch()

        self.snr = torch.tensor([snr])
        self.stretch_factor = stretch_factor

    def apply_transforms(self, waveform, noise):
        # Apply AddNoise transformation
        noisy_waveform = self.add_noise_transform(waveform, noise, self.snr)

        # Apply TimeStretch transformation
        stretched_waveform = self.time_stretch_transform(noisy_waveform, self.stretch_factor)

        return stretched_waveform