@echo off
setlocal enabledelayedexpansion

echo Digite uma combinação de números de 1 a 4 para escolher os scripts a serem executados, ou 5 para todos:
echo 1: asr_trafo_noaug.py
echo 2: asr_trafo_aug.py
echo 3: asr_trafo_aug_prop.py
echo 4: asr_trafo_aug_plus_prop.py
echo 5: Todos os scripts

set /p opcao=

set "argumentos=M04 F03 M12 M01"

if "%opcao%"=="5" (
    echo Executando todos os scripts
    for %%a in (%argumentos%) do (
        python asr_trafo_noaug.py %%a
        python asr_trafo_aug.py %%a
        python asr_trafo_aug_prop.py %%a
        python asr_trafo_aug_plus_prop.py %%a
    )
) else (
    for /l %%x in (0,1,4) do (
        set "num=!opcao:~%%x,1!"
        if "!num!"=="1" (
            echo Executando asr_trafo_noaug.py
            for %%a in (%argumentos%) do (
                python asr_trafo_noaug.py %%a
            )
        )
        if "!num!"=="2" (
            echo Executando asr_trafo_aug.py
            for %%a in (%argumentos%) do (
                python asr_trafo_aug.py %%a
            )
        )
        if "!num!"=="3" (
            echo Executando asr_trafo_aug_prop.py
            for %%a in (%argumentos%) do (
                python asr_trafo_aug_prop.py %%a
            )
        )
        if "!num!"=="4" (
            echo Executando asr_trafo_aug_plus_prop.py
            for %%a in (%argumentos%) do (
                python asr_trafo_aug_plus_prop.py %%a
            )
        )
    )
)
