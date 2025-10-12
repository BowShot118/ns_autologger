# NationStates Autologin Script
# Author: BowShot118 / bowshottoerana@gmail.com
# Created with Python 3.13
# Libraries
import xml.etree.ElementTree as ET
import time
import requests
import csv
import os

# Setting variables
userAgent = ""
filePath = r"C://NationStates"
passwordFile = "nationPasswords.csv"
cteFile = "cteList.csv"
failedFile = "failedList.csv"
passwordPath = os.path.join(filePath,passwordFile)
ctePath = os.path.join(filePath,cteFile)
failedPath = os.path.join(filePath,failedFile)
errorPath = os.path.join(filePath,"error.txt")

# Other Variables
nationsList = []
cteList = [["nation","password"]]
failedList = [["nation","password"]]

# Function to interact with the API's private shards
def passLoginApi(userAgent: str, nation: str, password: str):
    headers = {'User-Agent': userAgent, 'X-Password': password}
    query = f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation.lower().replace(" ","_")}&q=ping"
    callResults = requests.get(query, headers=headers)
    return callResults.status_code

try:
    # Reads the CSV File
    with open(passwordPath,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            nationsList.append(row)

    if nationsList[0][0] == "nation":
        nationsList.pop(0)

    for row in nationsList:
        callResults = passLoginApi(userAgent,row[0],row[1])
        match callResults:
            case 200:
                print(f"{row[0]} logged into successfully")
            case 403:
                print(f"{row[0]} failed to log in due to incorrect password or a lack of set useragent")
                failedList.append(row)
            case 404:
                print(f"{row[0]} has ceased to exist")
                cteList.append(row)
            case 409:
                print(f"{row[0]} has failed to log in as the last login was too recent")
                failedList.append(row)
            case _:
                print(f"{row[0]} has not been logged into. Unusual or uncommon error. HTTPS Error Code {callResults}")
                failedList.append(row)
        time.sleep(1)

    if len(cteList) > 1:
        print(f"{(len(cteList)-1)} nations have CTE'd and must be revived manually. The list of those nations can be found in the \'cteNations.csv\' file in this program's file directory")
        with open(ctePath,"w+",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(cteList)
    if len(failedList) > 1:
        print(f"{(len(failedList)-1)} nations failed to be logged into. The list of those nations can be found in the \'failedNations.csv\' file in this program's file directory")
        with open(failedPath,"w+",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(cteList)

    print("Autologger Complete")
    time.sleep(10)
except Exception as e:
    print(e)
    try:
        with open(errorPath,"w") as file:
            file.write(f"{e}")
    except Exception as e:
        print(f"{e}")
    time.sleep(100)
