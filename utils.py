import json
import geopandas
from io import BufferedWriter
from ftplib import FTP
from pathlib import Path
from progressbar import ProgressBar

import logger
import widgets
from type import Filenames


def load_dataframe_from_file(path: Path, filegroup: str):
    '''
    Loads dataframe in from the provided `.zip` file
    '''
    logger.LOAD_FILE_IN(filegroup)
    dataframe = geopandas.read_file(path)
    logger.SUCCESS_MESSAGE()

    return dataframe


def save_data_as_json(
    path:      Path,
    data:      dict,
    filegroup: str
) -> None:
    '''
    Saves dictionary as `.json` file
    '''
    logger.SAVING_DATA(filegroup)
    with open( path, 'w' ) as fout:
        json.dump(data, fout)
    logger.SUCCESS_MESSAGE()


def create_folder_if_not_exist(path: Path) -> None:
    '''
    Checks if provided path exists,
    If not creates it
    '''
    if ( not path.is_dir() ):
        path.mkdir(parents = True, exist_ok = True)


def check_file_presence(
    url:       str,
    path:      str,
    filename:  str,
    filegroup: str,
    save_to:   Path
) -> None:
    '''
    Wraps checking existence of the file and
    its integrity(via file volume)
    '''
    download_file_if_not_exist(url, path, filename, filegroup, save_to)
    download_file_if_corrupt(url, path, filename, filegroup, save_to)


def download_file_if_not_exist(
    url:       str,
    path:      str,
    filename:  str,
    filegroup: str,
    save_to:   Path
) -> None:
    '''
    Check if file exists,
    If not downloads it from FTP server using params
    '''
    if ( not save_to.is_file() ):
        logger.MISSING_FILE(filegroup)
        ftp_download_file(
            url      = url,
            path     = path,
            filename = filename,
            save_to  = save_to
        )


def download_file_if_corrupt(
    url:       str,
    path:      str,
    filename:  str,
    filegroup: str,
    save_to:   Path
) -> None:
    '''
    Checks if file in the local storage is not corrupted
    (now via the volume), if so, re-downloads it from
    FTP server
    '''
    if ( not is_same_volume(url, path, filename, save_to) ):
        logger.CORRUPT_FILE(filegroup)
        ftp_download_file(
            url      = url,
            path     = path,
            filename = filename,
            save_to  = save_to
        )


def ftp_download_file(
    url:      str,
    path:     str,
    filename: str,
    save_to:  Path
) -> None:
    '''
    Downloads file from FTP server using provided information
    '''
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
    '''
    Obtains a list of files in the desired folder
    on FTP server
    '''
    with FTP( url ) as ftp:
        ftp.login()
        ftp.cwd( path )

        return ftp.nlst()


def is_same_volume(
    url:      str,
    path:     str,
    filename: str,
    file:     Path
) -> bool:
    '''
    Checks whether the file in the local storage
    is the same volume as on FTP server
    '''
    with FTP( url ) as ftp:
        ftp.login()
        ftp.cwd( path )

        return ( ftp.size(filename) == file.stat().st_size )


def _ftp_download_file_with_progress_bar(
    ftp: FTP,
    filename: str,
    writer: BufferedWriter,
) -> int:
    '''
    Downloads the file with Progress Bar
    '''
    size = ftp.size( filename )

    pbar = ProgressBar(widgets = widgets.ftp_download(filename), max_value = size)
    pbar.start()

    def write_file(data):
        '''
        Callback function that provides updates to ProgressBar
        '''
        writer.write(data)
        nonlocal pbar
        pbar += len(data)

    ftp.retrbinary(f'RETR {filename}', write_file)
    pbar.finish()