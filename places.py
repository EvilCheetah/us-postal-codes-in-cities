import census
import message
import paths
import utils


def get_places_files(
    url: str = census.FTP_URI
) -> None:
    if ( not (paths.PLACES_DIR).is_dir() ):
        paths.PLACES_DIR.mkdir(parents = True, exist_ok = True)
    
    if not (
        len( list(paths.PLACES_FILES) ) == 
        len( utils.get_files_list(url, census.DATA_URL['PLACES']) )
    ):
        print(message.MISSING_FILE('Places'))
        _download_places(url)
    
    return paths.PLACES_FILES


def _download_places(url: str):
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