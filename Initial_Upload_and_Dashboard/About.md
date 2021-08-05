# About

Reads Snowflake user credentials and shares, as well as the file name of excel documents and their directory path, From two sperate text files.
> - `SF_Account_Info.txt`
> - `SHARED_SF_Account_Info.txt`

Excel documents assumed to have 3 sheets within them.

Reformats the column names to an accepted format in compliance with the Snowflake documentation.

Uploads excel files to a database specified in `SF_Account_Info.txt` and shares all tables with the Snowflake account listed in `SHARED_SF_Account_Info.txt`.

`SQL_SCRIPT.txt` can then be executed in the Snowflake web app worksheet, merging the sheetes in a specific manner.

This repo, can be recoded for other Snowflake uploads with data sets that are not in the correct format.

As well as for pre-processing purposes. 
