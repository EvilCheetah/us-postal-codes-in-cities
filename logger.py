from color import Color


def MISSING_FILE(filegroup: str, filename: str) -> None:
    '''
    Structure:
        {filename} in {filegroup} found to be MISSING
    '''
    print(
       f'{Color.RED}{filename}{Color.END} in '
       f'{Color.RED}{filegroup}{Color.END} '
       f'{Color.BOLD}found to be{Color.END} '
       f'{Color.RED}{Color.BOLD}MISSING{Color.END}'
    )


def CORRUPT_FILE(filegroup: str, filename: str) -> None:
    '''
    Structure:
        {filename} in {filegroup} found to be CORRUPTED
    '''
    print(
       f'{Color.RED}{filename}{Color.END} in '
       f'{Color.RED}{filegroup}{Color.END} '
       f'{Color.BOLD}found to be{Color.END} '
       f'{Color.RED}{Color.BOLD}CORRUPTED{Color.END}'
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
        Begin processing {filegroup}
    '''
    print(
        f'Begin processing {Color.GREEN}{filegroup}{Color.END}'
    )


def LOAD_FILE_IN(filegroup: str) -> None:
    '''
    Structure:
        Loading in {filegroup} file...
    '''
    print(
        f'Loading in '
        f'{Color.YELLOW}{filegroup}{Color.END} '
        f'file... ',
        end   = '',
        flush = True
    )


def SAVING_DATA(filegroup: str) -> None:
    '''
    Structure
        Saving {filegroup} data...
    '''
    print(
        f'Saving     '
        f'{Color.GREEN}{Color.BOLD}{filegroup}{Color.END} '
        f'data... ',
        end   = '',
        flush = ''
    )


def SUCCESS_MESSAGE(add_new_line: bool = False) -> None:
    '''
    Structure:
        SUCCESS!
    '''
    print(f'{Color.GREEN}{Color.BOLD}SUCCESS!{Color.END}')

    if (add_new_line):
        print()


def SIDE_LOCATION_CONFLICT(first_item: str, second_item: str) -> None:
    '''
    Structure:
        Found side location conflict between {first_item} and {second_item}
    '''
    print(
        f'Found {Color.RED}{Color.UNDERLINE}side location conflict{Color.END} '
        f'between {Color.YELLOW}{Color.BOLD}{first_item}{Color.END} '
        f'and {Color.PURPLE}{Color.BOLD}{second_item}{Color.END}'
    )