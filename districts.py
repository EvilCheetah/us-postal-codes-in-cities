import re
import census
import logger
import paths
import utils
from type import Row, Districts


def get_district_codes(
    url: str = census.FTP_URI
) -> Districts:
    '''
    Obtains `.txt` either from 
        - `local storage` specified in 'paths.INPUT_DATA_FOLDER'
        - `Census` ftp-server
    and parses it using custom parser.

    Cusom parser is used due to the issues working with pandas
    For some strange reason, header was shifted. Probably because
    default delimeter is r'\s'.
    '''
    logger.INITIATE_INTEGRITY_CHECK('District Codes')
    utils.create_folder_if_not_exist( paths.DISTRICT_CODES_DIR )
    utils.check_file_presence(
        url       = url,
        path      = census.DATA_URL['DISTRICT_CODES'],
        filename  = census.FILE['DISTRICT_CODES'],
        filegroup = 'District Codes',
        save_to   = paths.DISTRICT_CODES_PATH
    )
    logger.FINISH_INTEGRITY_CHECK('District Codes')
    
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