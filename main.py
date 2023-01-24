import json
import geopandas
from progressbar import progressbar
from pathlib import Path
from shapely import (
    Polygon,
    MultiPolygon,
    GeometryCollection
)

import paths
import utils
import logger
import widgets
from places import get_places_files
from districts import get_district_codes
from postal_codes import get_postal_codes_file


def main():
    # Store Postal Codes
    # districts         = get_district_codes()
    # places_files      = get_places_files()

    p_codes = utils.load_dataframe_from_file(
        path      = get_postal_codes_file(), 
        filegroup = "Postal Codes"
    )

    p_data  = []
    
    for row in p_codes.itertuples():
        p_data.append({
            'postal_code': row.ZCTA5CE20,
            'latitude':    row.INTPTLAT20,
            'longitude':   row.INTPTLON20
        })
        
    with open( paths.POSTAL_CODES_OUT_FILE, 'w') as fout:
        json.dump(p_data, fout)
        logger.SUCCESSFUL_FILE_SAVE('Postal Codes')

#     print('Saving Postal Codes...')
#     with open( Path('out') / Path('postal-codes') / Path('postal-codes.json'), 'w' ) as fout:
#         json.dump(postal_codes, fout, indent = 4)
#     print('Postal Codes Saved!')

#     for state_folder in [
#         entry 
#         for entry in Path('in').iterdir()
#         if entry.is_dir()
#     ]:
#         for shx_file in state_folder.glob('*.shx'):
#             state_cities = geopandas.read_file( shx_file )

#             cities = []

#             for row in state_cities.itertuples():
#                 postal_codes = []

#                 for p_row in zips.itertuples():
#                     if row.geometry.intersects(p_row.geometry):
#                         intersection = type(row.geometry.intersection(p_row.geometry))

#                         if (intersection is Polygon)      or   \
#                            (intersection is MultiPolygon) or   \
#                            (intersection is GeometryCollection):

#                             postal_codes.append(p_row.ZCTA5CE20)
#                             print('{')
#                             print(f"    'city_name':   {row.NAME},\n".encode('utf8'))
#                             print(f"    'postal_code': {p_row.ZCTA5CE20},\n".encode('utf8'))
#                             print(f"    'state':       {STATES[row.STATEFP]},\n".encode('utf8'))
#                             print(f"    'geometry':    {type(row.geometry.intersection(p_row.geometry))},\n".encode('utf8'))
#                             print('}\n')
                
#                 cities.append({
#                     'state_abbreviation': STATES[row.STATEFP],
#                     'city_name':          row.NAME,
#                     'latitude':           row.INTPTLAT,
#                     'longitude':          row.INTPTLON,
#                     'postal_codes':       list(postal_codes)
#                 })

#             with open(
#                 Path('out') / Path('cities') / Path(f'{STATES[row.STATEFP]}_cities.json'),
#                 'w',
#                 encoding = 'utf-8'
#             ) as fout:
#                 json.dump(cities, fout, indent = 4, ensure_ascii = False)
    
    


        

if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was terminated...')