from progressbar import (
    Bar,
    ETA,
    Percentage,
    FileTransferSpeed,
)

from color import Color


def ftp_download(filename: str):
    return [
        f'Downloading {Color.BOLD}{Color.GREEN}{filename}{Color.END}: ', 
        Percentage(), ' ',
        Bar(marker = '#', left = '[', right = ']'), ' ',
        ETA(), ' ', FileTransferSpeed()
    ]