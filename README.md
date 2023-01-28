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