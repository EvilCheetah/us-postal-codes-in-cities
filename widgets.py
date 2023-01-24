from progressbar import (
    Bar,
    ETA,
    Percentage,
    FileTransferSpeed,
)

from color import Color


def ftp_download(filename: str):
    return [
        f'Downloading {Color.GREEN}{Color.BOLD}{filename}{Color.END}: ', 
        Percentage(), ' ',
        Bar(marker = '#', left = '[', right = ']'), ' ',
        ETA(), ' ', FileTransferSpeed()
    ]


def integrity_check(filegroup: str):
    return [
        f'Checking Integrity of '
        f'{Color.GREEN}{Color.BOLD}{filegroup}{Color.END}: ',
        Percentage(), ' ',
        Bar(marker = '#', left = '[', right = ']'), ' ',
        ETA()
    ]