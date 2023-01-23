from io import BufferedWriter
from ftplib import FTP
from pathlib import Path
from progressbar import ProgressBar

import widgets
from type import Filenames


def ftp_download_file(
    url:      str,
    path:     str,
    filename: str,
    save_to:  Path
) -> None:
    with FTP( url ) as ftp:
        ftp.login()
        ftp.cwd( path )

        with open( save_to, 'wb' ) as file:
            _ftp_download_file_with_progress_bar(
                ftp      = ftp,
                filename = filename,
                writer   = file
            )


def get_files_list(
    url:    str,
    path:   str
) -> Filenames:
    with FTP( url ) as ftp:
        ftp.login()
        ftp.cwd( path )

        return ftp.nlst()


def _ftp_download_file_with_progress_bar(
    ftp: FTP,
    filename: str,
    writer: BufferedWriter,
) -> int:
    size = ftp.size( filename )

    pbar = ProgressBar(widgets = widgets.ftp_download(filename), max_value = size)
    pbar.start()

    def write_file(data):
        writer.write(data)
        nonlocal pbar
        pbar += len(data)

    ftp.retrbinary(f'RETR {filename}', write_file)
    pbar.finish()