# make python script that calculates
    # total month number
    # net profit/losses/period
    #change profit/losses/period and average of these
    # greatest increase in losses
    # greatest decrease in profits
# python3 main.py
#import libraries
import os
import csv
#join to create path to directory
file = os.path.join("Resources", "budget_data.csv")
#open and read CSV
with open(file) as csv1:
    csvreader = csv.reader(csv1, delimiter= ",")
    months = 0
    total = 0
    cashMoney = []
    avgList = []
    dateMon = []
    #skip header
    next(csvreader)
    #Create column lists, count months, count total
    for row in csvreader:
        months = months + 1
        total = total + int(row[1])
        cashMoney.append(int(row[1]))
        dateMon.append(str(row[0]))
    avgHolder = cashMoney[0]
    cash0riginal = 0
    dateMin = dateMon[0]
    dateMax = dateMon[0]
    minMan = cashMoney[1] - cashMoney[0]
    maxMan = cashMoney[1] - cashMoney[0]
    dateCount = 1
    #Finding max and min change, 
    for i in range(1, len(cashMoney)):
        avgList.append(cashMoney[i] - avgHolder)
        cash0riginal = cash0riginal + 1
        MAXIMUS = cashMoney[i] - avgHolder
        avgHolder = cashMoney[cash0riginal]
        if MAXIMUS >= maxMan:
            maxMan = MAXIMUS
            dateMax = dateMon[dateCount]
        if MAXIMUS <= minMan:
            minMan = MAXIMUS
            dateMin = dateMon[dateCount]
        dateCount = dateCount + 1
    avgCounter = 0
    for x in avgList:
        avgCounter = avgCounter + x
    #Calculate average change
    avgChange = -avgCounter / len(avgList)
    avgChange = round(-avgChange, 2)
    #Print in terminal
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: {avgChange}")
    print(f"Greatest Increase in Profits: {dateMax} (${maxMan})")
    print(f"Greatest Decrease in Profits: {dateMin} (${minMan})")
    #Write to txt file
    with open('analysis/financialAnalysis.txt', 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------------\n")
        file.write(f"Total Months: {months}\n")
        file.write(f"Total: ${total}\n")
        file.write(f"Average Change: {avgChange}\n")
        file.write(f"Greatest Increase in Profits: {dateMax} (${maxMan})\n")
        file.write(f"Greatest Decrease in Profits: {dateMin} (${minMan})\n")

        
    
