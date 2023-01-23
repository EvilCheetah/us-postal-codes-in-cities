from pathlib import Path
import census


INPUT_DATA_FOLDER   = Path('in')

DISTRICT_CODES_DIR  = INPUT_DATA_FOLDER / Path('districts')
DISTRICT_CODES_FILE = Path( census.FILE['DISTRICT_CODES'] )
DISTRICT_CODES_PATH = DISTRICT_CODES_DIR / DISTRICT_CODES_FILE

PLACES_DIR          = INPUT_DATA_FOLDER / Path('places')
PLACES_FILE         = lambda filename: (PLACES_DIR / Path(filename)) 
PLACES_FILES        = PLACES_DIR.glob('*_place.zip')

POSTAL_CODES_DIR    = INPUT_DATA_FOLDER / Path('postal-codes')
POSTAL_CODES_FILE   = Path( census.FILE['POSTAL_CODES'] )
POSTAL_CODES_PATH   = POSTAL_CODES_DIR / POSTAL_CODES_FILE