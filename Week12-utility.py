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

def FindWordCount(lst, s):
    counter = 0
    for line in lst:
        line = line.split(" ")
        for word in line:
            if word == s:
                counter += 1
    return counter

#PrintOutput(LoadFile("../sample_file.txt"))
#UpdateString("Hello World", "a", 3)
#a = LoadFile("../sample_file.txt")
#PrintOutput(str(FindWordCount(a, "How")))
