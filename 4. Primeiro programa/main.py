# coding: utf-8

import os
from download_dados_copa import main as download
from extrai_zip import extrair

path = 'saida.zip'
url = 'http://livropython.com.br/dados.zip'  # Apenas http :)

if not os.path.exists(path):
    download(url=url)
    extrair(path)
else:
    print('\033[32mFinished\033[m')
