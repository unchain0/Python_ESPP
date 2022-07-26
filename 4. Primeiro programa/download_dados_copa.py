# coding: utf-8

import io
import urllib.error
import urllib.request as request

BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print(f'Downloading => {(time * BUFF_SIZE / length * 100):.1f}%')


def download(response, output):
    total_download = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_download += len(data)
        if not data:
            break
        output.write(data)
        print(f'Downloading => {int(total_download)}%')


def main(url):
    try:
        response = request.urlopen(url)
        out_file = io.FileIO('saida.zip', mode='w')

        content_length = response.getheader('Content-Length')
        if content_length:
            length = int(content_length)
            download_length(response, out_file, length)
        else:
            download(response, out_file)

        response.close()
        out_file.close()
        print('\033[32mDownload completed\033[m')
    except urllib.error.URLError:
        print('\033[31mInvalid url\033[m')
