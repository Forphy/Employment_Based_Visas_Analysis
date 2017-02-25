"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We analyse the PERM_Disclosure_Data_FY16.csv in this script.

Author:
Yanzhong Li     yli185@ucsc.edu

"""

# from __future__ import print_function
import csv
import sys

# select useful columns out of source dataset
def simplifyDataset():
    # Useful column nums
    usefulCol = [0,2,8,13,17,24,25,36,37,40,47,107,108,109,110,112,113]
    print "There're " + str(len(usefulCol)) + " columns left."

    # Load csv contents
    with open('PERM_Disclosure_Data_FY16.csv', 'rb') as csvfile:
        permData = list(csv.reader(csvfile))

    simCsv = []
    for row in permData:
        thisRow = []
        for colNum in usefulCol:
            thisRow.append(row[colNum])
        simCsv.append(thisRow)

    # output to a csv file
    with open('simplified_data.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(simCsv)

if (len(sys.argv) > 1 and sys.argv[1] == 'simplify'):
    simplifyDataset()

# Load csv contents
with open('simplified_data.csv', 'rb') as csvfile:
    permData = list(csv.reader(csvfile))

# count how many lines and how many h1b
def getCount(permData):
    count = 0
    h1bCount = 0
    for row in permData:
        if row[13] == "H-1B":
            h1bCount += 1
        count += 1
    print "h1bCount: ", h1bCount, "\ttotalCount: ", count, "\t", float(h1bCount)/float(count)

def deleteNonH1B():
    permData[:] = [row for row in permData if row[13] == "H-1B"]
    print "Now we've just delte all Non-H1B cases from Dataset"

def getCertifiedRatio(permData):
    count = 0.0
    certifiedCount = 0.0
    for row in permData:
        if (row[1] == "Certified" or row[1] == "Certified-Expired"):
            certifiedCount += 1
        elif (row[1] == "Denied"):
            count += 1
    print "% of certified:\t", certifiedCount / (certifiedCount+count)

getCount(permData)
getCertifiedRatio(permData)
deleteNonH1B()
getCount(permData)
getCertifiedRatio(permData)















pass
