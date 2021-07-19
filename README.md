# SnowFlake_Upload
Go to:
```https://www.snowflake.com/```
Click on "START FOR FREE" on top right corner.
Fill in required fields (can make multiple trial accounts with same email address).
Click "CONTINUE"
Select "Enterprise" (Any should work really).
Select "Microsoft Azure" (Windows symbol on right).
Select East US 2 (Virginia) [Need to work on this part].
Click "GET STARTED"
Fill in capcha.
Open email you provided in previous field.
Open email from sent from Snowflake (may take a min.), click "CLICK TO ACTIVATE".
Type in a Username and Password...be sure to make a note of this somewhere.
In the top right corner click on your Username and then clikc on "Switch Role", then click "ACCOUNTADMIN" (need this to do most things).
Click in the top corner on your Username again and copy the alph-numeric string under log out (i.e.: L00000) this is your account name.
Click in the top corner on your Username again and copy the alph-numeric string labeled "Organization" (i.e.: VZZZZZ)

In the folder that contains this INSTRUCTIONS.txt file, open "SF_Account_Info.txt" and paste the following info on a new line and then save "SF_Account_Info.txt":
USERNAME
Password
account_name.east-us-2.azure
adbnamehere
C:\\some_path_name\to_your\excel\documents\
FormattedCallReports_year 2016.xlsx
FormattedCallReports_year 2017.xlsx
FormattedCallReports_year 2018.xlsx
FormattedCallReports_year 2019.xlsx
FormattedCallReports_year 2020.xlsx
FormattedCallReports_year 2021.xlsx

================================================================================================================================
If you don't have pandas installed for python execute the following in a python base ```pip install pandas``` (may also need: ```pip install openpyxl```).
Also you will need to execute this command in a python base to install the python connector:
```pip install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.4.6/tested_requirements/requirements_36.reqs``

And then this command after the previous command has ran:
```pip install snowflake-connector-python==2.4.6```
```pip install snowflake-connector-python[pandas]```

Open whatever promt you have that can open a python (base).
Type "```python ```" (may be ```py ```or ```conda ```) and then drag and drop or paste the full path to "C:\...\snowFlakeMethod.py"
Now just sit back and wait for the files to upload!
After each file is uploaded you can check them on your snowflake account under "Databases" or "Worksheets".
Once the first file is uploaded you can use Power BI to direct query the data from Snowflake!
