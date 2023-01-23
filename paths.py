from pathlib import Path
import census


INPUT_DATA_FOLDER   = Path('in')

DISTRICT_CODES_DIR  = INPUT_DATA_FOLDER / Path('districts')
DISTRICT_CODES_FILE = Path( census.FILE['DISTRICT_CODES'] )
DISTRICT_CODES_PATH = DISTRICT_CODES_DIR / DISTRICT_CODES_FILE

PLACES_CODES_DIR    = INPUT_DATA_FOLDER / Path('places')
PLACES_CODES_FILE   = lambda filename: (PLACES_CODES_DIR / Path(filename)) 
PLACES_CODES_FILES  = PLACES_CODES_DIR.glob('*_place.zip')