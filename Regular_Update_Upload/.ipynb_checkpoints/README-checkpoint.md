# Updates

Assumes that there are 8 files in the [SF_Account_Info](../Login_Credentials/SF_Account_Info.txt) file.

Takes the 8th file and updates all of the tables accordingly, including the predictions and the Dashboard.

The only difference between this notebook and the initial upload is that the SQL statements are different for creating the Total tables from the Excel sheets.

This is also assuming that the call center is using [iCarol](https://www.icarol.com/) as their CRM database and is only able to recieve data from them monthly.  Therefore [Upload_Updates_Forecasts.ipynb](Upload_Updates_Forecasts.ipynb) only needs to be ran once a month after the updated 2021 file is replaced in the dir that was provided in the [SF_Account_Info](../Login_Credentials/SF_Account_Info.txt) file.

![](../Images/iCarol.jpg)

## Make sure to reopen the [PBI_Dashboard.pbix](../PBI_Dashboard/PBI_Dashboard.pbix) and click on `Update` after the notebook has updated Snowflake!