import re
from ftplib import FTP
from pathlib import Path
from typing import NamedTuple, List

import census
import paths


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
        (paths.Districts).mkdir(parents = True, exist_ok = True)

    with FTP( url ) as ftp:
        ftp.login()
        ftp.cwd( census.DATA_URL['DISTRICT_CODES'] )
        print(ftp.nlst())

        with open( paths.DISTRICT_CODES_PATH, 'wb' ) as file:
            ftp.retrbinary(f'RETR {census.FILE["DISTRICT_CODES"]}', file.write)

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

get_district_codes()