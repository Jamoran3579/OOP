import operator

def getDataList(fileName):
    dataFile = open(fileName, "r")
    dataList = []
    for line in dataFile:
        # strip end-of-line, split on commas, and append items to list
        dataList.append(line.strip().split(','))
    return dataList


# find monthly average
def getMonthlyAverage(dataList):
    m = '08'
    n = '2008'
    monthlyAverageList = []
    numerator = 0.0
    denominator = 0.0

    for i in dataList:
        # print i
        a_list = []
        month = i[0].split('-')[1]
        year = i[0].split('-')[0]
        close = float(i[6])
        volume = float(i[5])
        if month != m:
            average = numerator / (denominator - 1)
            a_list = [month, year, average]
            monthlyAverageList.append(a_list)

        numerator += close * volume
        denominator += volume
        m = month
        n = year
    return monthlyAverageList


def printInfo(monthlyAverageList):
    monthlyAverageList.sort(key=operator.itemgetter(-1), reverse=True)
    print_list = []
    print('The 6 best averages for google are:')
    print(monthlyAverageList[0:6])

    monthlyAverageList.reverse()

    print('The 6 worst averages for google are:')
    print(monthlyAverageList[0:6])


fileName = 'GOOG.csv'
dataList = getDataList(fileName)
dataList.pop(0)
monthlyAverageList = getMonthlyAverage(dataList)
# print monthlyAverageList
printInfo(monthlyAverageList)
