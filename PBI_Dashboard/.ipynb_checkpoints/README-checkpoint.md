# Dashboard Instructions

>[Download Microsoft Power BI](https://www.microsoft.com/en-us/download/details.aspx?id=58494) if you don't have it installed already.

![https://www.microsoft.com/en-us/download/details.aspx?id=58494](../Images/PBI_dl.png)

## Open [PBI_Dashboard.pbix](../PBI_Dashboard/PBI_Dashboard.pbix)

>When prompted with login info fill in with your Snowflake user name and password (this isn't the same exact prompt.  It is from `Get Data`->`Databases`->`Snowflake` if you wanted to rebuild your won).

![](../Images/PBI_Setup1.png)

>For the Server field enter in this section of your Snowflake web app URL.

![](../Images/PBI_Setup.png)

>Once the dashboard is ready to be linked to a website, click `Publish`:

![](../Images/PBI_Setup7.png)

>Then click `Select`

![](../Images/PBI_Setup2.png)

>Click on the blue text to go to your Power BI web portal.

![](../Images/PBI_Setup3.png)

>Click on the `gear symbol`->`Admin Portal` 
>>***Note this will only work with a Power BI Pro account!** (~=$10:month)

![](../Images/PBI_Setup6.png)

# |Put screen shot here|

>Return to the PBI Report and click `File`->`Embed Report`->`Publish to Web (Public)`

![](../Images/PBI_Setup8.png)

>Copy the URL with the IFRAM html tag and place it onto the website you want to put it on.

# Updates

## Once the [Upload_Updates_Forecasts.ipynb](..Regular_Update_Upload/Upload_Updates_Forecasts.ipynb) has run, reopn the [PBI_Dashboard.pbix](../PBI_Dashboard/PBI_Dashboard.pbix) and click on `Publish` once again.  Respond affirmative to all prompts.  The dashboard will then be updated.