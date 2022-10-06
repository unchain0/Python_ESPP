# coding: utf-8

import os
import zipfile
import sys


def extrair(path: str):
    if not os.path.exists(path):
        print(f'Arquivo {path} não existe')
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print('\033[32mArquivos extraídos\033[m')
