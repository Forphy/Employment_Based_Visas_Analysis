"""
This is a script for course project in CMPS263, UCSC 2017 Winter.
We analyse the PERM_Disclosure_Data_FY16.csv in this script.

Author:
Yanzhong Li     yli185@ucsc.edu

"""

# from __future__ import print_function
import csv
import sys

US_STATES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
US_STATE_SHORT_dic = {'WA': 'Washington', 'DE': 'Delaware', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'HI': 'Hawaii', 'FL': 'Florida', 'WY': 'Wyoming', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'TX': 'Texas', 'LA': 'Louisiana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'TN': 'Tennessee', 'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California', 'NV': 'Nevada', 'VA': 'Virginia', 'CO': 'Colorado', 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'VT': 'Vermont', 'IL': 'Illinois', 'GA': 'Georgia', 'IN': 'Indiana', 'IA': 'Iowa', 'OK': 'Oklahoma', 'AZ': 'Arizona', 'ID': 'Idaho', 'CT': 'Connecticut', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts', 'OH': 'Ohio', 'UT': 'Utah', 'MO': 'Missouri', 'MN': 'Minnesota', 'MI': 'Michigan', 'RI': 'Rhode Island', 'KS': 'Kansas', 'MT': 'Montana', 'MS': 'Mississippi', 'SC': 'South Carolina', 'KY': 'Kentucky', 'OR': 'Oregon', 'SD': 'South Dakota'}


# select useful columns out of source dataset
def simplifyDataset():
    # Useful column nums
    usefulCol = [0,2,8,13,17,24,25,33,34,35,36,37,40,47,107,108,109,110,112,113]
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

# count how many lines and how many h1b
def getCount(permData):
    # first we get the column number for CLASS_OF_ADMISSION
    CLASS_OF_ADMISSION_idx = getColNum(permData, "CLASS_OF_ADMISSION")
    # now we count the h1b cases as well as all cases
    totalCount = 0
    h1bCount = 0
    for row in permData:
        if row[CLASS_OF_ADMISSION_idx] == "H-1B":
            h1bCount += 1
        totalCount += 1
    print "h1bCount: ", h1bCount, "\ttotalCount: ", totalCount, "\t", float(h1bCount)/float(totalCount)
    return totalCount

def getCertifiedRatio(permData):
    # first we get the column number for CLASS_OF_ADMISSION
    CASE_STATUS_idx = getColNum(permData, "CASE_STATUS")
    count = 0.0
    certifiedCount = 0.0
    for row in permData:
        if (row[CASE_STATUS_idx] == "Certified" or row[CASE_STATUS_idx] == "Certified-Expired"):
            certifiedCount += 1
        elif (row[CASE_STATUS_idx] == "Denied"):
            count += 1
    if (certifiedCount+count != 0):
        # print "% of certified:\t", certifiedCount / (certifiedCount+count)
        return certifiedCount / (certifiedCount+count)
    else:
        print "ERROR!!! certifiedCount+count is zero"
        return 0.0


def getColNum(permData, columnName):
    for idx, colName in enumerate(permData[0]):
        if (colName == columnName):
            return idx

def getH1B(permData):
    CLASS_OF_ADMISSION_idx = getColNum(permData, "CLASS_OF_ADMISSION")
    print "We just got all H1B cases from Dataset"
    permData_nonH1B = [row for row in permData if row[CLASS_OF_ADMISSION_idx] == "H-1B"]
    permData_nonH1B.insert(0, permData[0])
    return permData_nonH1B

def getComputerMajor(permData):
    FOREIGN_WORKER_INFO_MAJOR_idx = getColNum(permData, "FOREIGN_WORKER_INFO_MAJOR")
    print "We just got all Computer Major cases from Dataset"
    permData_ComputerMajor = [row for row in permData if "COMPUTER" in row[FOREIGN_WORKER_INFO_MAJOR_idx]]
    permData_ComputerMajor.insert(0, permData[0])
    return permData_ComputerMajor

def getHighDegrees(permData):
    FOREIGN_WORKER_INFO_EDUCATION_idx = getColNum(permData, "FOREIGN_WORKER_INFO_EDUCATION")
    print "We just got all Bachelor's, Master's, Doctorate cases from Dataset"
    permData_HighDegrees = [row for row in permData if not (row[FOREIGN_WORKER_INFO_EDUCATION_idx] == "Other" and row[FOREIGN_WORKER_INFO_EDUCATION_idx] == "High School")]
    return permData_HighDegrees

def getCompany(permData, comName):
    EMPLOYER_NAME_idx = getColNum(permData, "EMPLOYER_NAME")
    # print "We just got all Company: " + str(comName) + " cases from Dataset"
    permData_Company = [row for row in permData if row[EMPLOYER_NAME_idx] == comName]
    permData_Company.insert(0, permData[0])
    return permData_Company

def getState(permData, workState):
    JOB_INFO_WORK_STATE_idx = getColNum(permData, "JOB_INFO_WORK_STATE")
    print "We just got all cases in state: " + str(workState) + " from Dataset"
    permData_State = [row for row in permData if row[JOB_INFO_WORK_STATE_idx] == workState]
    permData_State.insert(0, permData[0])
    return permData_State

def getMoneyStr(moneyStr):
    if moneyStr != '':
        moneyStr = moneyStr.split('.')
        moneyStr = moneyStr[0].replace(',','')
    return moneyStr

# output to a csv file
def outputCsv(filename, listOfList):
    with open(filename, 'wb') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(listOfList)

def q1(permData_original):
    # Do you know your peers(people major in CS or CE)?
    # what are their highest degree? (pie chart)
    # how long have they been graduated? (bar chart)
    # how experienced are they in CS/CE field? (bar chart)
    # where do they come from?
    permData_ComputerMajor = getComputerMajor(permData_original)
    permData_HighDegree_ComputerMajor = getHighDegrees(permData_ComputerMajor)
    FOREIGN_WORKER_INFO_EDUCATION_idx = getColNum(permData_HighDegree_ComputerMajor, "FOREIGN_WORKER_INFO_EDUCATION")
    masCount = 0
    docCount = 0
    bachCount = 0
    for row in permData_HighDegree_ComputerMajor:
        degree = row[FOREIGN_WORKER_INFO_EDUCATION_idx]
        if (degree == "Master's"):
            masCount += 1
        elif (degree == "Doctorate"):
            docCount += 1
        elif (degree == "Bachelor's"):
            bachCount += 1
    # print "bachCount= ", bachCount, "\tmasCount= ", masCount, "\tdocCount= ", docCount
    outputCsv('./output/queries/q1_1.csv', [["Bachelor's","Master's","Doctorate"],[bachCount,masCount,docCount]])

    FW_INFO_YR_REL_EDU_COMPLETED_idx = getColNum(permData_HighDegree_ComputerMajor, "FW_INFO_YR_REL_EDU_COMPLETED")
    year_count_dic = {}
    for row in permData_HighDegree_ComputerMajor[1:]:
        gdYear = int(row[FW_INFO_YR_REL_EDU_COMPLETED_idx])
        if gdYear >= 1973: #exclude outliers
            if not gdYear in year_count_dic:
                year_count_dic[gdYear] = 1
            else:
                year_count_dic[gdYear] += 1
    year_count_list = []
    for year,count in year_count_dic.iteritems():
        if count >= 50: #exclude outliers
            year_count_list.append([year, count])
    year_count_list.sort(key=lambda x: x[0])
    # print year_count_list
    year_count_list.insert(0, ["Graduation_year", "count"])
    outputCsv('./output/queries/q1_2.csv', year_count_list)

    JOB_INFO_EXPERIENCE_NUM_MONTHS_idx = getColNum(permData_HighDegree_ComputerMajor, "JOB_INFO_EXPERIENCE_NUM_MONTHS")
    numMonth_count_dic = {}
    for row in permData_HighDegree_ComputerMajor[1:]:
        if row[JOB_INFO_EXPERIENCE_NUM_MONTHS_idx] == "":
            numMonth = 0
        else:
            numMonth = int(row[JOB_INFO_EXPERIENCE_NUM_MONTHS_idx])
        if not numMonth in numMonth_count_dic:
            numMonth_count_dic[numMonth] = 1
        else:
            numMonth_count_dic[numMonth] += 1
    numMonth_count_list = []
    for numMonth,count in numMonth_count_dic.iteritems():
        if (count > 40): #exclude outliers
            numMonth_count_list.append([numMonth, count])
    numMonth_count_list.sort(key=lambda x: x[0])
    # print numMonth_count_list
    numMonth_count_list.insert(0, ["Months_of_Experience", "count"])
    outputCsv('./output/queries/q1_3.csv', numMonth_count_list)

    COUNTRY_OF_CITIZENSHIP_idx = getColNum(permData_HighDegree_ComputerMajor, "COUNTRY_OF_CITIZENSHIP")
    country_count_dic = {}
    for row in permData_HighDegree_ComputerMajor[1:]:
        country = row[COUNTRY_OF_CITIZENSHIP_idx]
        if not country in country_count_dic:
            country_count_dic[country] = 1
        else:
            country_count_dic[country] += 1
    country_count_list = []
    for country,count in country_count_dic.iteritems():
        country_count_list.append([country, count])
    country_count_list.sort(key=lambda x: x[1], reverse=True)
    # print country_count_list
    country_count_list.insert(0, ["Country_of_Citizenship", "count"])
    outputCsv('./output/queries/q1_4.csv', country_count_list)

def q2(permData_original):
    # What are the top 30 foreign-worker-friendly U.S. companies?
    # how good do they paid?
    # what kind of jobs they are offering the most for foreign workers? top30
    # how likely does each of them help you get PERM certified?
    EMPLOYER_NAME_idx = getColNum(permData_original, "EMPLOYER_NAME")
    company_count_dic = {}
    for row in permData_original[1:]:
        comName = row[EMPLOYER_NAME_idx]
        if not comName in company_count_dic:
            company_count_dic[comName] = 1
        else:
            company_count_dic[comName] += 1
    company_count_list = []
    for comName,count in company_count_dic.iteritems():
        company_count_list.append([comName, count])
    company_count_list.sort(key=lambda x: x[1], reverse=True)
    # print company_count_list[:30]
    company_count_list.insert(0, ["Company", "new_foreign_worker_count"])
    outputCsv('./output/queries/q2_1.csv', company_count_list)
    company_count_list.pop(0)


    WAGE_OFFER_FROM_9089_idx = getColNum(permData_original, "WAGE_OFFER_FROM_9089")
    WAGE_OFFER_TO_9089_idx = getColNum(permData_original, "WAGE_OFFER_TO_9089")
    WAGE_OFFER_UNIT_OF_PAY_9089_idx = getColNum(permData_original, "WAGE_OFFER_UNIT_OF_PAY_9089")
    wageUnit_count_dic = {}
    wageCount = 0
    avgRate = 0.0
    maxRate = 0.0
    minRate = sys.float_info.max
    for row in permData_original[1:]:
        comName = row[EMPLOYER_NAME_idx]
        if comName in [x[0] for x in company_count_list[:30]]:
            wageCount += 1
            wageUnit = row[WAGE_OFFER_UNIT_OF_PAY_9089_idx]
            wageFrom = getMoneyStr(row[WAGE_OFFER_FROM_9089_idx])
            wageTo = getMoneyStr(row[WAGE_OFFER_TO_9089_idx])
            if wageFrom != '' and float(wageFrom) != 0:
                if wageTo != '':
                    wageFrom = float(wageFrom) + float(wageTo) / 2.0
                else:
                    wageFrom = float(wageFrom)
                # normalized to yearly wage
                if wageUnit == 'Hour':
                    wageFrom = wageFrom * 40 * 52
                elif wageUnit == 'Week':
                    wageFrom = wageFrom * 52
                elif wageUnit == 'Bi-Weekly':
                    wageFrom = wageFrom * 52 / 2
                avgRate = (avgRate *(wageCount-1) + wageFrom) / wageCount
                maxRate = max(maxRate, wageFrom)
                minRate = min(minRate, wageFrom)
    # print "avgRate: ", avgRate, "\tmaxRate: ", maxRate, "\tminRate: ", minRate
    outputCsv('./output/queries/q2_2.csv', [["In the top 30 foreign-worker-friendly companies",],["Average_Annual_Wage","Maximum_Annual_Wage","Minimum_Annual_Wage"],[avgRate, maxRate, minRate]])

    occu_count_dic = {}
    PW_SOC_TITLE_idx = getColNum(permData_original, "PW_SOC_TITLE")
    for row in permData_original:
        comName = row[EMPLOYER_NAME_idx]
        if comName in [x[0] for x in company_count_list[:30]]:
            occu = row[PW_SOC_TITLE_idx]
            if not occu in occu_count_dic:
                occu_count_dic[occu] = 1
            else:
                occu_count_dic[occu] += 1
    occu_count_list = []
    for occu,count in occu_count_dic.iteritems():
        occu_count_list.append([occu, count])
    occu_count_list.sort(key=lambda x: x[1], reverse=True)
    # for row in occu_count_list[:30]:
    #     print row
    occu_count_list.insert(0, ["Job_title", "counts"])
    outputCsv('./output/queries/q2_3.csv', occu_count_list)

    for row in company_count_list[:100]:
        comName = row[0]
        permData_Company = getCompany(permData_original, comName)
        row.append(100*getCertifiedRatio(permData_Company))
    # for row in company_count_list[:30]:
    #     print row
    company_count_list.insert(0, ["Job_title", "1","Percentage of employees got certified"])
    outputCsv('./output/queries/q2_4.csv', [ [x[0],x[2]] for x in company_count_list[:100]])

def q3(permData_original):
    # Where are the most popular state your peers like to work?
    # How is each of them likely to get certified?
    # what are the companies in top 10 state that most likely to get your PERM certified?
    JOB_INFO_WORK_STATE_idx = getColNum(permData_original, "JOB_INFO_WORK_STATE")
    workState_count_dic = {}
    for row in permData_original[1:]:
        workState = row[JOB_INFO_WORK_STATE_idx]
        if workState != "":
            if not workState in workState_count_dic:
                workState_count_dic[workState] = 1
            else:
                workState_count_dic[workState] += 1
    workState_count_list = []
    for workState,count in workState_count_dic.iteritems():
        workState_count_list.append([workState, count])
    workState_count_list.sort(key=lambda x: x[1], reverse=True)
    # print workState_count_list

    for row in workState_count_list:
        workState = row[0]
        permData_State = getState(permData_original, workState)
        row.append(100*getCertifiedRatio(permData_State))
    # for each in workState_count_list:
    #     print each
    workState_count_list.insert(0, ["State", "new_foreign_worker_count", "Percentage of workers got certified"])
    outputCsv('./output/queries/q3_1.csv', workState_count_list)

def viz(permData_original):
    # what are the top 30 foreign-worker-friendly companies in each state?
    # How many foreign wokers did each of these company supported for EB visa in 2016?
    JOB_INFO_WORK_STATE_idx = getColNum(permData_original, "JOB_INFO_WORK_STATE")
    EMPLOYER_NAME_idx = getColNum(permData_original, "EMPLOYER_NAME")
    for workState in US_STATES :
        permData_State = getState(permData_original, workState)
        company_count_dic = {}
        for row in permData_State[1:]:
            comName = row[EMPLOYER_NAME_idx]
            if not comName in company_count_dic:
                company_count_dic[comName] = 1
            else:
                company_count_dic[comName] += 1
        company_count_list = []
        for comName,count in company_count_dic.iteritems():
            company_count_list.append([comName, count])
        company_count_list.sort(key=lambda x: x[1], reverse=True)
        # print company_count_list[:30]
        company_count_list.insert(0, ["Company", "new_foreign_worker_count"])
        outputCsv('./output/viz/PERM_Companies/' + workState +'.csv', company_count_list[:30])

    # What are the top 30 foreign-worker-friendly companies across the U.S.?
    # How many foreign wokers did each of these company supported for EB visa in 2016?
    # Which state is each of them from?
    company_count_dic = {}
    for row in permData_original[1:]:
        comName = row[EMPLOYER_NAME_idx]
        if not comName in company_count_dic:
            company_count_dic[comName] = 1
        else:
            company_count_dic[comName] += 1
    company_count_list = []
    for comName,count in company_count_dic.iteritems():
        company_count_list.append([comName, count])
    company_count_list.sort(key=lambda x: x[1], reverse=True)
    for outputRow in company_count_list[:30] :
        company_name = outputRow[0]
        offices_states = []
        for row in permData_original[1:] :
            if row[EMPLOYER_NAME_idx] == company_name:
                curWorkState = row[JOB_INFO_WORK_STATE_idx]
                if not curWorkState in offices_states:
                    offices_states.append(curWorkState)
        outputRow.append(offices_states)
    company_count_list.insert(0, ["Company", "new_foreign_worker_count", "offices_states"])
    outputCsv('./output/viz/PERM_Companies/_US.csv', company_count_list[:30])


    # How many foreign-workers applying for EB2/3 in each state?
    state_caseCount_dic = {}
    for state_name in US_STATES:
        state_caseCount_dic[state_name] = 0
    for row in permData_original[1:]:
        cur_workState = row[JOB_INFO_WORK_STATE_idx]
        if cur_workState in state_caseCount_dic:
            state_caseCount_dic[cur_workState] += 1;
    # print state_caseCount_dic
    state_caseCount_list = []
    for workState,count in state_caseCount_dic.iteritems():
        state_caseCount_list.append([workState, count])
    state_caseCount_list.sort(key=lambda x: x[1], reverse=True)
    for row in state_caseCount_list:
        row.append(US_STATE_SHORT_dic[row[0]])
    state_caseCount_list.insert(0, ["State", "applicants_count", "FullStateName"])
    outputCsv('./output/viz/PERM_Companies/_PERM_StateByCase.csv', state_caseCount_list)

if (len(sys.argv) > 1):
    if (sys.argv[1] == 'simplify'):
        simplifyDataset()
    else:
        # Load csv contents
        with open('simplified_data.csv', 'rb') as csvfile:
            permData = list(csv.reader(csvfile))
        if (sys.argv[1] == 'query'):
            q1(permData)
            q2(permData)
            q3(permData)
        elif (sys.argv[1] == 'q1'):
            q1(permData)
        elif (sys.argv[1] == 'q2'):
            q2(permData)
        elif (sys.argv[1] == 'q3'):
            q3(permData)
        elif (sys.argv[1] == 'viz'):
            viz(permData)

######## TESTING CODE ###############
# getCount(permData)
# getCertifiedRatio(permData)
# print "*" * 70
# permData_nonH1B = getNonH1B(permData)
# getCount(permData_nonH1B)
# getCertifiedRatio(permData_nonH1B)
# print "*" * 70
# permData_ComputerMajor = getComputerMajor(permData)
# getCount(permData_ComputerMajor)
# getCertifiedRatio(permData_ComputerMajor)
# print "*" * 70






pass
