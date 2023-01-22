import re
from ftplib import FTP
from pathlib import Path
from typing import NamedTuple, List

import census
import paths
import utils


Header = List[str]

class Row(NamedTuple):
    STATE:    str
    STATEFP:  str
    CD113FP:  str
    NAMELSAD: str

class Districts(NamedTuple):
    header: Header
    data:   List[Row]


def get_district_codes(
    url: str = census.FTP_URI
) -> Districts:
    '''
    Obtains `.txt` from Census website and customly parses it

    Used a custom parser, due to the issues working with pandas
    For some strange reason, header was shifted. Probably because
    default delimeter is r'\s'.
    '''
    if ( not (paths.DISTRICT_CODES_DIR).is_dir() ):
        (paths.DISTRICT_CODES_DIR).mkdir(parents = True, exist_ok = True)

    if ( not (paths.DISTRICT_CODES_PATH).is_file() ):
        utils.ftp_download_file(
            url      = url,
            path     = census.DATA_URL['DISTRICT_CODES'],
            filename = census.FILE['DISTRICT_CODES'],
            save_to  = paths.DISTRICT_CODES_PATH
        )
    
    with open( paths.DISTRICT_CODES_PATH, 'r' ) as fin:
        data   = fin.readlines()
    
    header = data[0].split()
    rows   = [
        re.split(r'\s{2,}', row) 
        for row in data[1:]
    ]
    
    return Districts(
        header,
        [
            Row(
                STATE    = state,
                STATEFP  = fp,
                CD113FP  = cd113fp,
                NAMELSAD = namelsad
            )
            for [state, fp, cd113fp, namelsad] in rows
        ]
    )


if __name__ == '__main__':
    try:
        get_district_codes()

    except KeyboardInterrupt:
        print('Program was terminated')
    
    except Exception as e:
        print(e)