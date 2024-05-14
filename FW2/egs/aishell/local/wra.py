def calculate_wra(ref_file, hyp_file):
    """
    Calcula o Word Recognition Accuracy (WRA) entre os arquivos de referência e hipótese.

    Args:
        ref_file (str): Caminho para o arquivo de referência (transcrição correta).
        hyp_file (str): Caminho para o arquivo de hipótese (transcrição gerada pelo ASR).

    Returns:
        float: O WRA como uma porcentagem.
    """
    with open(ref_file, 'r') as ref, open(hyp_file, 'r') as hyp:
        ref_lines = ref.readlines()
        hyp_lines = hyp.readlines()

    total_lines = len(ref_lines)
    error_count = sum(1 for ref, hyp in zip(ref_lines, hyp_lines) if ref.strip() != hyp.strip())

    wra = ((total_lines - error_count) / total_lines) * 100

    return wra

# Exemplo de uso
ref_file_path = '../exp/train_m4_n3_in80_elayer5_head8_k64_v64_model512_inner2048_drop0.1_pe5000_emb512_dlayer3_share1_ls0.1_epoch100_shuffle1_bs64_bf15000_mli800_mlo150_k0.2_warm4000/decode_test_beam5_nbest1_ml100/ref.trn'
hyp_file_path = '../exp/train_m4_n3_in80_elayer5_head8_k64_v64_model512_inner2048_drop0.1_pe5000_emb512_dlayer3_share1_ls0.1_epoch100_shuffle1_bs64_bf15000_mli800_mlo150_k0.2_warm4000/decode_test_beam5_nbest1_ml100/hyp.trn'

wra_resultado = calculate_wra(ref_file_path, hyp_file_path)
print(f"O WRA calculado é de {wra_resultado:.2f}%")
