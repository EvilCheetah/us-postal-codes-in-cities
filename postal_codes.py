import census
import message
import paths
import utils
from type import Filename


def get_postal_codes_file(
    url: str = census.FTP_URI
) -> Filename:
    '''
    Obtains shapefile either from 
        - `local storage` specified in 'paths.INPUT_DATA_FOLDER'
        - `Census` ftp-server
    '''
    print( message.INITIATE_INTEGRITY_CHECK('Postal Codes') )
    utils.create_folder_if_not_exist( paths.POSTAL_CODES_DIR )
    utils.check_file_presence(
        url       = url,
        path      = census.DATA_URL['POSTAL_CODES'],
        filename  = census.FILE['POSTAL_CODES'],
        filegroup = 'Postal Codes',
        save_to   = paths.POSTAL_CODES_PATH
    )
    print( message.FINISH_INTEGRITY_CHECK('Postal Codes') )
    
    return paths.POSTAL_CODES_FILE


if __name__ == '__main__':
    try:
        get_postal_codes_file()

    except KeyboardInterrupt:
        print('Program was terminated')
    
    except Exception as e:
        print(e)