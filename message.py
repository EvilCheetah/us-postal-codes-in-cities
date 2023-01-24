from color import Color


def MISSING_FILE(filegroup: str):
    '''
    Structure:
        One or more files in {filegroup} are MISSING\n
        Downloading...
    '''
    return (
       f'{Color.BOLD}One or more files{Color.END} in '
       f'{Color.RED}{filegroup}{Color.END} '
       f'are {Color.RED}{Color.BOLD}MISSING{Color.END}\n'
       f'{Color.GREEN}{Color.BOLD}Downloading...{Color.END}'
    )


def CORRUPT_FILE(filegroup: str):
    '''
    Structure:
        One or more files in {filegroup} seems to be CORRUPTED\n
        Re-downloading...
    '''
    return (
       f'{Color.BOLD}One or more files{Color.END} in '
       f'{Color.RED}{filegroup}{Color.END} '
       f'seems to be {Color.RED}{Color.BOLD}CORRUPTED{Color.END}\n'
       f'Re-downloading...'
    )