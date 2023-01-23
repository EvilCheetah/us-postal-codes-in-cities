import census
import message
import paths
import utils
from type import Filename


def get_postal_codes(
    url: str = census.FTP_URI
) -> Filename:
    '''
    Obtains shapefile either from 
        - `local storage` specified in 'paths.INPUT_DATA_FOLDER'
        - `Census` ftp-server
    '''
    utils.create_folder_if_not_exist( paths.POSTAL_CODES_DIR )

    if ( not (paths.POSTAL_CODES_FILE).is_file() ):
        print(message.MISSING_FILE('Postal Codes'))
        utils.ftp_download_file(
            url      = url,
            path     = census.DATA_URL['POSTAL_CODES'],
            filename = census.FILE['POSTAL_CODES'],
            save_to  = paths.POSTAL_CODES_PATH
        )
    
    return paths.POSTAL_CODES_FILE


if __name__ == '__main__':
    try:
        get_postal_codes()

    except KeyboardInterrupt:
        print('Program was terminated')
    
    except Exception as e:
        print(e)