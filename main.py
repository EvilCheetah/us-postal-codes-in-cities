import re
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
    district_codes         = get_district_codes()
    postal_codes_dataframe = utils.load_dataframe_from_file(
        path      = get_postal_codes_file(), 
        filegroup = "Postal Codes"
    )

    p_data  = []
    for row in postal_codes_dataframe.itertuples():
        p_data.append({
            'postal_code': row.ZCTA5CE20,
            'latitude':    row.INTPTLAT20,
            'longitude':   row.INTPTLON20
        })

    utils.save_data_as_json(
        path      = paths.POSTAL_CODES_OUT_FILE,
        data      = p_data,
        filegroup = 'Postal Codes'
    )

    for place_file in sorted( get_places_files() ):
        state_abbr   = utils.get_state_abbreviation(place_file.name, district_codes)

        state_cities_dataframe = utils.load_dataframe_from_file(
            path      = place_file,
            filegroup = f'{state_abbr} - Cities'
        )

        state_cities = []

        # TODO: Refactor using MultiProcessing Module
        #       to increase performance
        for state_city_entry in progressbar(
            iterator  = state_cities_dataframe.itertuples(),
            max_value = len(state_cities_dataframe.index),
            widgets   = widgets.processing_intersections(state_abbr)
        ):
            postal_codes_in_city = utils.get_postal_codes_intersections(
                state_city_entry, postal_codes_dataframe
            )

            state_cities.append({
                'state_abbreviation': state_abbr,
                'city_name':          state_city_entry.NAME,
                'latitude':           state_city_entry.INTPTLAT,
                'longitude':          state_city_entry.INTPTLON,
                'postal_codes':       list(postal_codes_in_city)
            })

        utils.save_data_as_json(
            path = paths.PLACES_OUT_FILE(state_abbr),
            data = state_cities,
            filegroup = f'{state_abbr} - Cities'
        )
    


        

if __name__ == '__main__':
    try:
        main()
    
    except KeyboardInterrupt:
        print('Program was terminated...')