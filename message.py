from color import Color


def MISSING_FILE(filegroup: str) -> None:
    '''
    Structure:
        One or more files in {filegroup} are MISSING\n
        Downloading...
    '''
    print(
       f'{Color.BOLD}One or more files{Color.END} in '
       f'{Color.RED}{filegroup}{Color.END} '
       f'are {Color.RED}{Color.BOLD}MISSING{Color.END}\n'
       f'{Color.GREEN}{Color.BOLD}Downloading...{Color.END}'
    )


def CORRUPT_FILE(filegroup: str) -> None:
    '''
    Structure:
        One or more files in {filegroup} seems to be CORRUPTED\n
        Re-downloading...
    '''
    print(
       f'{Color.BOLD}One or more files{Color.END} in '
       f'{Color.RED}{filegroup}{Color.END} '
       f'seems to be {Color.RED}{Color.BOLD}CORRUPTED{Color.END}\n'
       f'Re-downloading...'
    )


def INITIATE_INTEGRITY_CHECK(filegroup: str) -> None:
    '''
    Structure:
        Initiating integrity check for {filegroup}...
    '''
    print(
        f'{Color.BOLD}Initiating file-check for{Color.END} '
        f'{Color.GREEN}{filegroup}{Color.END}...'
    )


def FINISH_INTEGRITY_CHECK(filegroup: str) -> None:
    '''
    Structure:
        All files for {filegroup} are up-to-date!
    '''
    print(
        f'All files for {Color.YELLOW}{filegroup}{Color.END} '
        f'{Color.GREEN}{Color.BOLD}are up-to-date!{Color.END}'
         '\n'
    )


def BEGIN_PROCESSING(filegroup: str) -> None:
    '''
    Structure:
        Begin processing {filegroup}...
    '''
    print(
        f'Begin processing {Color.GREEN}{filegroup}{Color.END}...'
    )