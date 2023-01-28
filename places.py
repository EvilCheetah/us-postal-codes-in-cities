from progressbar import progressbar

import census
import paths
import utils
import logger
import widgets
from type import Filenames


def get_places_files(
    url: str = census.FTP_URI
) -> Filenames:
    '''
    Obtains shapefiles either from 
        - `local storage` specified in 'paths.INPUT_DATA_FOLDER'
        - `Census` ftp-server
    '''
    logger.INITIATE_INTEGRITY_CHECK('Places')
    utils.create_folder_if_not_exist( paths.PLACES_DIR )
    utils.create_folder_if_not_exist( paths.PLACES_OUT_DIR )
    
    files = utils.get_files_list(url, census.DATA_URL['PLACES'])

    for file in files:
        utils.download_file_if_not_exist(
            url       = url,
            path      = census.DATA_URL['PLACES'],
            filename  = file,
            filegroup = 'Places',
            save_to   = paths.PLACES_FILE(file)
        )

    for file in files:
        utils.download_file_if_corrupt(
            url       = url,
            path      = census.DATA_URL['PLACES'],
            filename  = file,
            filegroup = 'Places',
            save_to   = paths.PLACES_FILE(file) 
        )

    logger.FINISH_INTEGRITY_CHECK('PLACES')
    
    return paths.PLACES_FILES


if __name__ == '__main__':
    try:
        get_places_files()
    
    except KeyboardInterrupt:
        print('Program was terminated...')
    
    except Exception as e:
        print(e)