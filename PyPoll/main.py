# make python script that calculates
    # total number votes casted
    # list of candidates whp recieved votes
    # % vote each candidate won
    # number of votes each candidate won
    # winner of election based on vote
    # python3 main.py
    #import libraries
import os
import csv
#join to create path to directory
path = os.path.join("Resources", "election_data.csv")
#open and read CSV
with open(path) as elData:
    csvFile = csv.reader(elData, delimiter = ",")
    voteCount = 0
    next(csvFile)
    genXList = []
    #build column lists
    for row in csvFile:
        genXList.append(row[2])
        voteCount = voteCount + 1
    candyList = []
    percentLS = []
    #stage candidate list
    candyList.append(genXList[0]) 
    #find unique candidates
    for i in genXList: 
        if i not in candyList:

            candyList.append(i)
    votesLS = []
    # nested forloop, staging percent calculation and counting votes
    for i in candyList:
        candyCount = 0
        for j in genXList:
            if i == j:
                candyCount += 1
        votesLS.append(candyCount)
        percentLS.append(candyCount)
        #calculating percent
    for i in range(0, len(percentLS)):
        percentLS[i] = percentLS[i] / voteCount * 100
        percentLS[i] = round(percentLS[i], 3)
        #setting win (This is set after seeing that each result is different via votesLS)
    winrar = ""
    if percentLS[0] > percentLS[1] > percentLS[2]:
        winrar = candyList[0]
    elif percentLS[1] > percentLS[0] > percentLS[2]:
        winrar = candyList[1]
    else:
        winrar = candyList[2]
    #print in terminal 
    print("Election Results")
    print("")
    print("------------------------")
    print("")
    print(f"Total Votes {voteCount}")
    print("")
    print("------------------------")
    print("")
    print(f"{candyList[0]}: {percentLS[0]}% ({votesLS[0]})")
    print(f"{candyList[1]}: {percentLS[1]}% ({votesLS[1]})")
    print(f"{candyList[2]}: {percentLS[2]}% ({votesLS[2]})")
    print("\n")
    print("------------------------")
    print(f"Winner: {winrar}")
    print("\n")
    print("------------------------")
#write to .txt file
    pathtxt = os.path.join('analysis', 'electionResults.txt')
    with open(pathtxt, "w") as txtfile:
        txtfile.write("Election Results \n")
        txtfile.write("\n")
        txtfile.write("------------------------ \n")
        txtfile.write("\n")
        txtfile.write(f"Total Votes {voteCount} \n")
        txtfile.write("\n")
        txtfile.write("------------------------ \n")
        txtfile.write("\n")
        txtfile.write(f"{candyList[0]}: {percentLS[0]}% ({votesLS[0]}) \n")
        txtfile.write(f"{candyList[1]}: {percentLS[1]}% ({votesLS[1]}) \n")
        txtfile.write(f"{candyList[2]}: {percentLS[2]}% ({votesLS[2]}) \n")
        txtfile.write("\n")
        txtfile.write("------------------------ \n")
        txtfile.write(f"Winner: {winrar} \n")
        txtfile.write("\n")
        txtfile.write("------------------------ \n")
