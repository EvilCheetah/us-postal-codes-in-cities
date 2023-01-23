from color import Color


def MISSING_FILE(filegroup: str):
    '''
    Structure:
        Several {filegroup} file(s) are MISSING\n
        Downloading...
    '''
    return (
       f'{Color.BOLD}Several{Color.END} '
       f'{Color.RED}{filegroup}{Color.END} '
       f'file(s) are {Color.RED}{Color.BOLD}MISSING{Color.END}\n'
       f'{Color.GREEN}{Color.BOLD}Downloading...{Color.END}'
    )