# Dashboard Instructions

>[Download Microsoft Power BI](https://www.microsoft.com/en-us/download/details.aspx?id=58494) if you don't have it installed already.

![https://www.microsoft.com/en-us/download/details.aspx?id=58494](../Images/PBI_dl.png)

## Open [PBI_Dashboard.pbix](PBI_Dashboard.pbix)

Click on `Get Data`->`Databases`->`Snowflake` to rebuild the dashobard with your own Snowflake data that was uploaded.).

![](../Images/PBI_setup1.png)

For the Server field enter in this section of your Snowflake web app URL.

![](../Images/PBI_setup.png)

## Recreating the Dashboard with Other Uploaded Snowflake Data

For each visual that is linked to the Snowflake data, ***uncheck*** the column in the `fields` menu and ***check*** the corresponding table and column name from the uploaded Snowflake data from the notebooks:

![](../Images/PBI_setup9.png)

Make any additional changes that you deem appropriate.

Once the dashboard is ready to be linked to a website, click `Publish`:

![](../Images/PBI_setup7.png)

Then click `Select`

![](../Images/PBI_setup2.png)

Click on the blue text to go to your Power BI web portal.

![](../Images/PBI_setup3.png)

Click on the `gear symbol`->`Admin Portal` 

***Note this will only work with a Power BI Pro account!** (~=10USDT:month)

![](../Images/PBI_setup6.png)

Click on `Publish to web`->`Allow existing and new codes`->`Apply`

![](../Images/Power_BI_Pro.png)

Return to the PBI Report and click `File`->`Embed Report`->`Publish to Web (Public)`

![](../Images/PBI_setup8.png)

Copy the URL with the `IFRAME` html tag and place it onto the website you want to put it on.

# Updates

## Once the [Upload_Updates_Forecasts.ipynb](..Regular_Update_Upload/Upload_Updates_Forecasts.ipynb) has run, reopn the [PBI_Dashboard.pbix](../PBI_Dashboard/PBI_Dashboard.pbix) and click on `Refresh` then on `Publish` once again.  Respond affirmative to all prompts.  The dashboard will then be updated.
