# ST: Speech-Transformer modificado conforme paper Shahamiri et al. (2023)[1]
Dysarthric Speech Transformer: A Sequence-to-Sequence Dysarthric Speech Recognition System.

## Instalação
- Python3 (recommend Anaconda)
- PyTorch 0.4.1+
- [Kaldi](https://github.com/kaldi-asr/kaldi) (Somente para extração de características)
- `pip install -r requirements.txt`
- `cd tools; make KALDI=/path/to/kaldi`
- Bases utilizadas: LJSpeech, para pre-treino e UA-Speech para suprir os dados de fala disártrica.
- as bases de dados devem ser baixadas e ajustadas conforme a base "aishell" (http://www.openslr.org/33/)
- Para executar `egs/aishell/run.sh`

## Uso
### Início rápido
```bash
$ cd egs/aishell
# Modifique o caminho para apontar para a base de dados dentro do script run.sh (Nesta implementação manter a estrutura da base aishell, apontando para esta mesma pasta)
$ bash run.sh
```
Pronto!

Os parâmetros podem ser alterados conforme segue: `$ bash run.sh --parameter_name parameter_value`, egs, `$ bash run.sh --stage 3`. Os nomes dos parâmetros podem ser encontrados em `egs/aishell/run.sh` antes de `. utils/parse_options.sh`.
### Fluxo de Trabalho
Workflow of `egs/aishell/run.sh`:
- Stage 0: Data Preparation
- Stage 1: Feature Generation
- Stage 2: Dictionary and Json Data Preparation
- Stage 3: Network Training
- Stage 4: Decoding
### Mais detalhes
`egs/aishell/run.sh` Exemplo de uso
```bash
# Set PATH and PYTHONPATH
$ cd egs/aishell/; . ./path.sh
# Train
$ train.py -h
# Decode
$ recognize.py -h
```
#### Como visualizar a perda?
Se quiser visualizar a perda pode usar [visdom](https://github.com/facebookresearch/visdom):
1. Abra um novo terminal em seu servidor remoto (recomendado tmux) e execute `$ visdom`.
2. Abra um novo terminal e rode `$ bash run.sh --visdom 1 --visdom_id "<any-string>"` or `$ train.py ... --visdom 1 --vidsdom_id "<any-string>"`.
3. Abra seu navegador e execute `<your-remote-server-ip>:8097`, egs, `127.0.0.1:8097`.
4. No sítio visdom, escolha `<any-string>` in `Environment` para ver sua perda.

#### Como resumir o treinamento?
```bash
$ bash run.sh --continue_from <model-path>
```
#### Como resolver falta de memória?
Se acontecer no treinamento, tente reduzir `batch_size`. `$ bash run.sh --batch_size <lower-value>`.

## Referências 
- [1] Shahamiri SR, Lal V, Shah D. Dysarthric Speech Transformer: A Sequence-to-Sequence Dysarthric Speech Recognition System. IEEE Trans Neural Syst Rehabil Eng. 2023;31:3407-3416. doi: 10.1109/TNSRE.2023.3307020. Epub 2023 Aug 29. PMID: 37603475.
