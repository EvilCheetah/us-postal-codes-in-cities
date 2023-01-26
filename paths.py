from pathlib import Path
import census


INPUT_DATA_DIR        = Path('in')
OUTPUT_DATA_DIR       = Path('out') 

DISTRICT_CODES_DIR    = INPUT_DATA_DIR / Path('districts')
DISTRICT_CODES_FILE   = Path( census.FILE['DISTRICT_CODES'] )
DISTRICT_CODES_PATH   = DISTRICT_CODES_DIR / DISTRICT_CODES_FILE

PLACES_DIR            = INPUT_DATA_DIR / Path('places')
PLACES_FILE           = lambda filename: (PLACES_DIR / Path(filename)) 
PLACES_FILES          = PLACES_DIR.glob('*_place.zip')

POSTAL_CODES_DIR      = INPUT_DATA_DIR / Path('postal-codes')
POSTAL_CODES_FILE     = Path( census.FILE['POSTAL_CODES'] )
POSTAL_CODES_PATH     = POSTAL_CODES_DIR / POSTAL_CODES_FILE

POSTAL_CODES_OUT_FILE = OUTPUT_DATA_DIR / Path('postal-codes.json')

PLACES_OUT_DIR        = OUTPUT_DATA_DIR / Path('places')
PLACES_OUT_FILE       = lambda state_abbr: (
    PLACES_OUT_DIR / Path(f'{state_abbr}_cities.json')
)