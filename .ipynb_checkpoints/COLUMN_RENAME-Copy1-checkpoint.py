# Make sure to pip the connector and install the dependencies:
# https://docs.snowflake.com/en/user-guide/python-connector-install.html
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import os
import pandas as pd

f = open("SF_Account_Info.txt", "r")

usr = f.readline()
usr = usr.replace('\n', '')
psswrd = f.readline()
psswrd = psswrd.replace('\n', '')
accnt = f.readline()
accnt = accnt.replace('\n', '')
dbName = f.readline()
dbName = dbName.replace('\n', '')
path = f.readline()
path = path.replace('\n', '')
file1 = f.readline()
file1 = file1.replace('\n', '')
file2 = f.readline()
file2 = file2.replace('\n', '')
file3 = f.readline()
file3 = file3.replace('\n', '')
file4 = f.readline()
file4 = file4.replace('\n', '')
file5 = f.readline()
file5 = file5.replace('\n', '')
file6 = f.readline()
file6 = file6.replace('\n', '')
file7 = f.readline()
file7 = file7.replace('\n', '')
f.close()

print(usr,'\n', psswrd,'\n', accnt,'\n', dbName, '\n', path, '\n', file1,'\n', file2,'\n', file3)

f1 = open("SHARED_SF_Account_Info.txt", "r")

shareName = f1.readline()
shareName = shareName.replace('\n', '')

sharedAccnt1 = f1.readline()
sharedAccnt1 = sharedAccnt1.replace('\n', '')
sharedAccnt2 = f1.readline()
sharedAccnt2 = sharedAccnt2.replace('\n', '')
sharedAccnt3 = f1.readline()
sharedAccnt3 = sharedAccnt3.replace('\n', '')
sharedAccnt4 = f1.readline()
sharedAccnt4 = sharedAccnt4.replace('\n', '')
sharedAccnt5 = f1.readline()
sharedAccnt5 = sharedAccnt5.replace('\n', '')
sharedAccnt6 = f1.readline()
sharedAccnt6 = sharedAccnt6.replace('\n', '')
sharedAccnt7 = f1.readline()
sharedAccnt7 = sharedAccnt7.replace('\n', '')
sharedAccnt8 = f1.readline()
sharedAccnt8 = sharedAccnt8.replace('\n', '')
sharedAccnt9 = f1.readline()
sharedAccnt9 = sharedAccnt9.replace('\n', '')
sharedAccnt10 = f1.readline()
sharedAccnt10 = sharedAccnt10.replace('\n', '')
sharedAccnt11 = f1.readline()
sharedAccnt11 = sharedAccnt11.replace('\n', '')
sharedAccnt12 = f1.readline()
sharedAccnt12 = sharedAccnt12.replace('\n', '')
sharedAccnt13 = f1.readline()
sharedAccnt13 = sharedAccnt13.replace('\n', '')
sharedAccnt14 = f1.readline()
sharedAccnt14 = sharedAccnt14.replace('\n', '')
sharedAccnt15 = f1.readline()
sharedAccnt15 = sharedAccnt15.replace('\n', '')

f1.close()

print('The Following Accounts Will Be Granted Share Access:\n' + sharedAccnt1, sharedAccnt2, sharedAccnt3, sharedAccnt4, sharedAccnt5, sharedAccnt6, sharedAccnt7, sharedAccnt8, sharedAccnt9, sharedAccnt10, sharedAccnt11, sharedAccnt12, sharedAccnt13, sharedAccnt14, sharedAccnt15)

accountList = [sharedAccnt1, sharedAccnt2, sharedAccnt3, sharedAccnt4, sharedAccnt5, sharedAccnt6, sharedAccnt7, sharedAccnt8, sharedAccnt9, sharedAccnt10, sharedAccnt11, sharedAccnt12, sharedAccnt13, sharedAccnt14, sharedAccnt15]
ACCOUNT_LIST = []
for i in accountList:
    if len(i) != 0:
        ACCOUNT_LIST.append(i)

aSQLstatement = 'USE database {};'.format(dbName)
sqlScript = 'create share {};'.format(shareName)
sqlScript1 = 'grant usage on database {} to share {};'.format(dbName, shareName)
sqlScript2 = 'grant usage on schema {}.public to share {};'.format(dbName, shareName)
sqlScript3 = 'grant select on all tables in schema {}.public to share {};'.format(dbName, shareName)

# Connect to SF
conn = snowflake.connector.connect(
    user=usr,
    password=psswrd,
    account=accnt,
    role='ACCOUNTADMIN',
    warehouse='COMPUTE_WH',
    #database='TWO_ELEVEN_OC_SAMPLE_DATA',
    #table='FORMATTED_REPORTS',
    #schema='PUBLIC'
                                    )
print("Connected to Snowflake using " + usr + " " + accnt)

os.chdir(path)
print("\tUsing files from dir " + path)


def uploadExcel(fileName):
    # Returns Year of File Passed to Method
    def fileYear():
        aYear = fileName[-7:-5]
        return '20' + aYear

    # Creates String to Pass to SF Python Connector for Table Creation
    def moreFormat(theInput):

        anthrList = []
        stringList = []
        o = 0

        for i in theInput:
            if i.startswith(' '):
                theInput[o] = i.strip()
            o = o + 1

            if len(i) > 255:
                i = i[:255]

            splChar = [
                '(', ')', '[', ']', '/', '\\', '-', '.', ':', '\t', '<', '>', '"', '?',
                '!', '`', "'", '&', '^', ' ', '{', '}', '+', '=', '~', '|', ';', '%', '#']
            for x in splChar:
                i = i.replace(x, '_')
            anthrList.append(i)
            stringList.append(i)

        stringList = str(stringList)
        stringList = stringList.replace("'", '"')
        stringList = stringList.replace(",", ' varchar,\n')
        stringList = stringList.strip("[]")
        stringList = stringList + " varchar"

        return anthrList, stringList

    # Convert to Pandas DF
    def makePandas():
        if fileName != '':
            dfSheet1 = pd.read_excel(fileName, sheet_name=0)
            dfSheet2 = pd.read_excel(fileName, sheet_name=1)
            dfSheet3 = pd.read_excel(fileName, sheet_name=2)
            dfSheet1.convert_dtypes(), dfSheet2.convert_dtypes(), dfSheet3.convert_dtypes()

            # Call moreFormat to pass string to SF Python Connector & Change DF Column Names to Match
            thisVar1 = dfSheet1.columns.tolist()
            dfSheet1.columns, stringList1 = moreFormat(thisVar1)
            thisVar2 = dfSheet2.columns.tolist()
            dfSheet2.columns, stringList2 = moreFormat(thisVar2)
            thisVar3 = dfSheet3.columns.tolist()
            dfSheet3.columns, stringList3 = moreFormat(thisVar3)

            # Create Cursor Object
            conn.cursor().execute("CREATE DATABASE IF NOT EXISTS {}".format(dbName.upper()))
            conn.cursor().execute("USE DATABASE {}".format(dbName.upper()))

            # Create Snowflake Table and Columns & Upload the DF to SF
            conn.cursor().execute(
                "CREATE OR REPLACE TABLE "
                "NEEDSMETANDUNMET{}({})".format(fileYear(), stringList1))
            success, nchunks, nrows, _ = write_pandas(conn, dfSheet1, 'NEEDSMETANDUNMET{}'.format(fileYear()))

            conn.cursor().execute(
                "CREATE OR REPLACE TABLE "
                "CALLREPORTS{}({})".format(fileYear(), stringList2))
            success, nchunks, nrows, _ = write_pandas(conn, dfSheet2, 'CALLREPORTS{}'.format(fileYear()))

            conn.cursor().execute(
                "CREATE OR REPLACE TABLE "
                "REFERRALS{}({})".format(fileYear(), stringList3))
            success, nchunks, nrows, _ = write_pandas(conn, dfSheet3, 'REFERRALS{}'.format(fileYear()))

            return print(fileName + ' Uploaded Succesfully To Snowflake!')
        else:
            return print('Nothing More to Upload.')

    return makePandas()


print("Uploading " + file1 + "\nThis will take several minutes.")
uploadExcel(file1)

print("Uploading " + file2 + "\nThis will take several minutes.")
uploadExcel(file2)

print("Uploading " + file3 + "\nThis will take several minutes.")
uploadExcel(file3)

print("Uploading " + file4 + "\nThis will take several minutes.")
uploadExcel(file4)

print("Uploading " + file5 + "\nThis will take several minutes.")
uploadExcel(file5)

print("Uploading " + file6 + "\nThis will take several minutes.")
uploadExcel(file6)

print("Uploading " + file7 + "\nThis will take several minutes.")
uploadExcel(file7)

print("All Files Provided in SF_Account_Info.txt have been uploaded now.")

try:
    conn.cursor().execute(aSQLstatement)
    conn.cursor().execute(sqlScript)
    print('Share Created!')
except:
    print("This share already esixts in your Snowflake account.")

try:
    conn.cursor().execute(aSQLstatement)
    conn.cursor().execute(sqlScript1)
    conn.cursor().execute(sqlScript2)
    conn.cursor().execute(sqlScript3)
except:
    print("There was an error in the grant usage on... SQL.")

try:
    for x in ACCOUNT_LIST:
        sqlScript4 = 'alter share {} add accounts={};'.format(shareName, x)
        conn.cursor().execute(aSQLstatement)
        try:
            conn.cursor().execute(sqlScript4)
        except:
            print('Account {} Could Not be Added.'.format(x))
    print("Accounts Successfully Added to {}!".format(shareName))
except:
    print("There was an error in the alter share {} add accounts=... SQL.".format(shareName))

conn.cursor().close()
print("Connection to Snowflake has been closed.")


# ## Check your Snowflake account to see if the Database & Table are created and filled

# ## *IMPORTANT*: This only works with accounts that are from the same region and cloud!

# Alternative Method
# from snowflake.connector.pandas_tools import pd_writer


# # Specify that the to_sql method should use the pd_writer function
# # to write the data from the DataFrame to the table named "customers"
# # in the Snowflake database.
# dfTotal.to_sql('FORMATTED_REPORTS', conn, index=False, method=pd_writer)

