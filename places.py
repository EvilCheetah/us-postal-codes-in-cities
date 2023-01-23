import census
import message
import paths
import utils
from type import Filenames


def get_places_files(
    url: str = census.FTP_URI
) -> Filenames:
    '''
    Obtains shapefiles either from 
        - `local storage` specified in 'paths.INPUT_DATA_FOLDER'
        - `Census` ftp-server
    '''
    utils.create_folder_if_not_exist( paths.PLACES_DIR )
    
    if not (
        len( list(paths.PLACES_FILES) ) == 
        len( utils.get_files_list(url, census.DATA_URL['PLACES']) )
    ):
        print(message.MISSING_FILE('Places'))
        _download_places(url)
    
    return paths.PLACES_FILES


def _download_places(url: str) -> None:
    files = utils.get_files_list(url, census.DATA_URL['PLACES'])

    for file in files:
        utils.ftp_download_file(
            url      = url,
            path     = census.DATA_URL['PLACES'],
            filename = file,
            save_to  = paths.PLACES_FILE(file)
        )


if __name__ == '__main__':
    try:
        get_places_files()
    
    except KeyboardInterrupt:
        print('Program was terminated...')
    
    except Exception as e:
        print(e)