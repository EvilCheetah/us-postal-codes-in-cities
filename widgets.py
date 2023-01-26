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

def processing_file(filegroup: str):
    return [
        f'Processing '
        f'{Color.GREEN}{Color.BOLD}{filegroup}{Color.END}: ',
        Percentage(), ' ',
        Bar(marker = '#', left = '[', right = ']'), ' ',
        ETA()
    ]


def processing_intersections(state_abbr: str):
    return [
        f'Processing '
        f'{Color.GREEN}{Color.BOLD}{state_abbr} - Cities{Color.END}: ',
        Percentage(), ' ',
        Bar(marker = '#', left = '[', right = ']'), ' ',
        ETA()
    ]