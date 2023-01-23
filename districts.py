import re
import census
import message
import paths
import utils
from type import Row, Districts


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
        print(message.MISSING_FILE('District Codes'))
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