# GitHub Repo: "https://github.com/supermando7/Week12-utility.git" 
# Armando Ocampo
# CSCI 102 – Section B
# Week 12 - Part B

def PrintOutput(string):
    print("OUTPUT", string)
    
def LoadFile(path):
    lines = []
    iFile = open(path, "r")
    for line in iFile:
        lines.append(line.rstrip("\n\r"))
    return(lines)

def UpdateString(str1, str2, index):
    listStr = list(str1)
    listStr[index] = str2
    finalStr = ""
    for chars in listStr:
        finalStr += chars
    PrintOutput(finalStr)

def FindWordCount(lines, s):
    counter = 0
    for line in lines:
        line = line.split(" ")
        for word in line:
            if word == s:
                counter += 1
    return counter

def ScoreFinder(players, scores, targetName):
    index = 0
    for tempName in players:
        if(tempName.lower() == targetName.lower()):
            PrintOutput(str(players[index]) + " got a score of " + str(scores[index]))
            return
        index += 1
    PrintOutput("player not found")

def Union(lst1, lst2):
    bigList = lst1 + lst2
    #removes duplicates
    bigUnique = []
    for element in bigList:
        if element not in bigUnique:
            bigUnique.append(element)
    return bigUnique

def Intersection(lst1, lst2):
    intersection = []
    for element in lst1:
        if element in lst2:
            intersection.append(element)
    return(intersection)

def NotIn(lst1, lst2):
    notin = []
    for element in lst1:
        if element not in lst2:
            notin.append(element)
    return(notin)

#TESTS
#PrintOutput(LoadFile("../sample_file.txt"))
#UpdateString("Hello World", "a", 3)
#a = LoadFile("../sample_file.txt")
#PrintOutput(str(FindWordCount(a, "How")))
#players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
#scores = [5, 8, 10, 6, 10, 4]
#ScoreFinder(players, scores, "jill")
#ScoreFinder(players, scores, "Manuel")
#players2 = ["Melvin", "Martian", "Baka", "Xai", "Cody"]
#PrintOutput(Union(scores, players2))
#PrintOutput(Intersection(players, players2))
#PrintOutput(NotIn(players2, players))
