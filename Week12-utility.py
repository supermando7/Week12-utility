def PrintOutput(string):
    print("OUTPUT", string)
    
def LoadFile(path):
    lines = []
    iFile = open(path, "r")
    for line in iFile:
        lines.append(line.rstrip("\n\r"))
    return(lines)

#PrintOutput(LoadFile("../sample_file.txt"))
