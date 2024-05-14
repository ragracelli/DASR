<<<<<<< HEAD
# Speech Recognition Pipelines

This repository contains the pipelines for Speech Recognition implemented in Keras and PyTorch frameworks and used in the paper 
"Exploring Alternative Data Augmentation Methods in Dysarthric Automatic Speech Recognition"

## Database Preparation

Download the Databases: LJSpeech and UA-Speech (contact with the University of Illinois is needed);

After decompressing and creating a local repository for the databases, run:
- `DataAugCode/data_aug.py` to create files with noise injection and time-stretch
- `DataAugCode/data_aug_prop.py` to create files with Spectral Occlusion
- `DataAugCode/data_aug_plus_prop.py` to create the combined augmentation
- `utils/make_dataset.py` to create the directory structure for the FW2

## For the FW1

The pipeline FW1 is the Speech Recognition System based on Transformer which uses 4 encoder and 1 decoder blocks.

After organizing the local databases repositories and editing the code `FW1/asr_trafo.py`, run this file to execute the training routines and tests. The routine tests are based on the Shahamiri paper. Please, consult this literature for freezing layers.

The checkpoints to control and dysarthric bases were manually implemented in the code.

The installation process can be consulted at this link <https://keras.io/examples/audio/transformer_asr/>

Obs: For greater automation, one can use the file 'asr_trafo_argparse.py' (still in implementation)

## For the FW2

ST: Modified Speech-Transformer according to Shahamiri et al. (2023)[1]. 
Dysarthric Speech Transformer: A Sequence-to-Sequence Dysarthric Speech Recognition System.

The modifications for this pipeline consist of 5 encoders and 3 decoders

### Installation
- Python3 (recommend Anaconda)
- PyTorch 0.4.1+
- Kaldi (Only for feature extraction)
- pip install -r requirements.txt
- cd tools; make KALDI=/path/to/kaldi

Databases used: LJSpeech, for pre-training and UA-Speech to supply dysarthric speech data.
The databases must be downloaded and adjusted according to the “aishell” base (http://www.openslr.org/33/)
To execute `egs/aishell/run.sh`

### Usage
#### Quick Start
```bash
$ cd egs/aishell
# Modify the path to point to the database within the run.sh script (In this implementation keep the structure of the aishell base, pointing to this same folder)
$ bash run.sh

For each dysarthric speaker, the bases were deleted and rewritten using the script 'del_cp.sh [speaker base]'

After the full copy of each dysarthric speech base, run 'audio_to_transcript.py' to create the file that relates the audio file to its transcription.

For copy the augmentation files, edit the utils/aug_copy.py to select the augment data to train and run the file. 

More information for Speech-Transformer can be found at here: https://github.com/kaituoxu/Speech-Transformer

The file 'example_tree_database.txt', shows an example of how the directory tree can be structured.

```bash

#
The file 'example_tree_database.txt', shows an example of how the directory tree can be structured.
=======
# Speech Recognition Pipelines

This repository contains the pipelines for Speech Recognition implemented in Keras and PyTorch frameworks and used in the paper 
"Exploring Alternative Data Augmentation Methods in Dysarthric Automatic Speech Recognition"

## Database Preparation

Download the Databases: LJSpeech and UA-Speech (contact with the University of Illinois is needed);

After decompressing and creating a local repository for the databases, run:
- `DataAugCode/data_aug.py` to create files with noise injection and time-stretch
- `DataAugCode/data_aug_prop.py` to create files with Spectral Occlusion
- `DataAugCode/data_aug_plus_prop.py` to create the combined augmentation
- `utils/make_dataset.py` to create the directory structure for the FW2

## For the FW1

The pipeline FW1 is the Speech Recognition System based on Transformer which uses 4 encoder and 1 decoder blocks.

After organizing the local databases repositories and editing the code `FW1/asr_trafo.py`, run this file to execute the training routines and tests. The routine tests are based on the Shahamiri paper. Please, consult this literature for freezing layers.

The checkpoints to control and dysarthric bases were manually implemented in the code.

The installation process can be consulted at this link <https://keras.io/examples/audio/transformer_asr/>

Obs: For greater automation, one can use the file 'asr_trafo_argparse.py' (still in implementation)

## For the FW2

ST: Modified Speech-Transformer according to Shahamiri et al. (2023)[1]. 
Dysarthric Speech Transformer: A Sequence-to-Sequence Dysarthric Speech Recognition System.

The modifications for this pipeline consist of 5 encoders and 3 decoders

### Installation
- Python3 (recommend Anaconda)
- PyTorch 0.4.1+
- Kaldi (Only for feature extraction)
- pip install -r requirements.txt
- cd tools; make KALDI=/path/to/kaldi

Databases used: LJSpeech, for pre-training and UA-Speech to supply dysarthric speech data.
The databases must be downloaded and adjusted according to the “aishell” base (http://www.openslr.org/33/)
To execute `egs/aishell/run.sh`

### Usage
#### Quick Start
```bash
$ cd egs/aishell
# Modify the path to point to the database within the run.sh script (In this implementation keep the structure of the aishell base, pointing to this same folder)
$ bash run.sh

For each dysarthric speaker, the bases were deleted and rewritten using the script 'del_cp.sh [speaker base]'

After the full copy of each dysarthric speech base, run 'audio_to_transcript.py' to create the file that relates the audio file to its transcription.

For copy the augmentation files, edit the utils/aug_copy.py to select the augment data to train and run the file. 

More information for Speech-Transformer can be found at here: https://github.com/kaituoxu/Speech-Transformer

The file 'example_tree_database.txt', shows an example of how the directory tree can be structured.

```bash
## hint
The file 'example_tree_database.txt', shows an example of how the directory tree can be structured.
>>>>>>> 48b7a6836988c0e66c10e14c2132bf57822751ff
