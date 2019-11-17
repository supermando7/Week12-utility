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

#PrintOutput(LoadFile("../sample_file.txt"))
#UpdateString("Hello World", "a", 3)
#a = LoadFile("../sample_file.txt")
#PrintOutput(str(FindWordCount(a, "How")))
#players = ["Mary", "Cody", "Joe", "Jill", "Xai", "Bodo"]
#scores = [5, 8, 10, 6, 10, 4]
#ScoreFinder(players, scores, "jill")
#ScoreFinder(players, scores, "Manuel")
