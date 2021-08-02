# Instructions

Modifications to these files apply to all Snowflake Credentials used all files in this repository.

## Snowflake Login Credentials and Uploaded Execel Files
---
In [SF_Account_Info.txt](SF_Account_Info.txt), each line corresponds to:

1. Snowflake User Name
2. Snowflake Password
3. Snowflake Account + [cloud & region suffix](https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#snowflake-region-ids)
4. Snowflake Database Name (creates one if it doesn't exist)
5. Path to Excel files
6. Name of the Excel File(s) 

![](../Images/SF_Instructions.png)

---
## If you want to share the database with more than one account on Snowflake.
---
In [SHARED_SF_Account_Info.txt](SHARED_SF_Account_Info.txt), each line corresponds to:

1. Snowflake Share Name (Will be created with this name)
2. Snowflake Account    
    * ***MUST BE FROM SAME CLOUD AND REGION*** 
---
### Using a Shared Snowflake Database
Just Follow this picture.

![](../Images/SF_Sharing.png)