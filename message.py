from color import Color


def MISSING_FILE(filegroup: str) -> str:
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


def CORRUPT_FILE(filegroup: str) -> str:
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


def INITIATE_INTEGRITY_CHECK(filegroup: str) -> str:
    '''
    Structure:
        Initiating integrity check for {filegroup}...
    '''
    return (
        f'{Color.BOLD}Initiating file-check for{Color.END} '
        f'{Color.GREEN}{filegroup}{Color.END}...'
    )


def FINISH_INTEGRITY_CHECK(filegroup: str) -> str:
    '''
    Structure:
        All files for {filegroup} are up-to-date!
    '''
    return (
        f'All files for {Color.YELLOW}{filegroup}{Color.END} '
        f'{Color.GREEN}{Color.BOLD}are up-to-date!{Color.END}'
         '\n'
    )