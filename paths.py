from pathlib import Path
import census


DISTRICT_CODES_DIR  = Path('in') / Path('districts')
DISTRICT_CODES_FILE = Path( census.FILE['DISTRICT_CODES'] )
DISTRICT_CODES_PATH = DISTRICT_CODES_DIR / DISTRICT_CODES_FILE