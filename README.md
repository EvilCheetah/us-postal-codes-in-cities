# Description
This project was created in order to find the connections between cities and postal indexes.  
This program uses the data provided by `US Census Bureau` from their official FTP Server; however, the data can be manually downloaded.  
Following program `creates necessary folders`, `downloads essential files` from US Census via FTP, `checks their integrity` and `saves data` in `.json` format.


# US Census Documentation
- `Information on` how to access US Census Data via `FTP` - **[ACS Data via FTP](https://www.census.gov/programs-surveys/acs/data/data-via-ftp.html)**
- `Shapefiles` used in the project - **[118th Congressional District Shapefiles](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html)**
- `Technical Documentation` on Shapefiles - **[Shapefiles and Line Files Technical Documentation Page](https://www.census.gov/programs-surveys/geography/technical-documentation/complete-technical-documentation/tiger-geo-line.html)** or **[Full PDF](https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp_rd18/TGRSHPRD18_TechDoc.pdf)**
- Places shapefile uses `STATEFP` number column for State Names, which can be accessed on - **[ANSI and FIPS Codes](https://www.census.gov/library/reference/code-lists/ansi.html)**


# Configuration
- To edit input and output folders, look into `paths` file, which holds following information.
- In case, US Census publishes new information, look into `census` file and edit necessary variables.


# Requirements
- Python `3.8 or above`
- Python PIP
- Python `venv` library
- Internet connection or pre-downloaded Census files


# Installation
1. Clone Repository  
`git clone https://github.com/EvilCheetah/us-postal-codes-in-cities.git`
2. Create and Activate Virtual  Environment  
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)

3. Install Dependencies  
`pip install -r requirements.txt`
4. Run Main File  
`python main.py`


# Output Data

## Postal Code
**Description**:
- `postal_code` - *string*. Postal Code Value
- `latitude` - *string*. Center latitude coordinate of specified Postal Code
- `longitude` - *string*. Center longitude coordinate of specified Postal Code

**TypeScript Interface**:
```ts
interface PostalCode
{
    postal_code: string;
    
    latitude:    string;

    longitude:   string;
}
```

**Example**: 
```json
{
    "postal_code": "35592",
    "latitude": "+33.7427261",
    "longitude": "-088.0973903"
}
```

___

## City
**Description**:
- `state_abbreviation` - *string*. State abbreviation which city is located in.
- `city_name` - *string*. City name
- `latitude` - *string*. Center latitude coordinate of specified City
- `longitude` - *string*. Center longitude coordinate of specified City
- `postal_codes` - *List[string]*. A set of postal codes located in City

**TypeScript Interface**:
```ts
type PostalCode = string;


interface City
{
    state_abbreviation: string;
    
    city_name:          string;

    latitude:           string;

    longitude:          string;

    postal_codes:       Array<PostalCode>;
}
```

**Example**: 
```json
{
    "state_abbreviation": "CA",
    "city_name": "South Lake Tahoe",
    "latitude": "+38.9392299",
    "longitude": "-119.9822156",
    "postal_codes": [
        "96150",
        "89449"
    ]
}
```


# Known Issues

## Side Location Conflict
In intersection calculations, I have spotted that Michigan shapefile throws an error on one of the geometries in the Postal Codes. The error message:  
`GEOSIntersects: TopologyException: side location conflict at ...`  
This error is getting catched in `utils -> _intersects`. Following method checks if two geometries intersect with each other; on error, returns `false`.

## SSL Certificate for Mac Users
In case you face `SSL: Certificate Verify Failed` error, please, review the following **StackOverflow Solution**:
[Scraping: SSL - kkCERTIFICATE_VERIFY_FAILED error](https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org)


# For Future Me
There are is only one thing left to do - increase performance, which can be achieved using `MultiProcessing` module. 