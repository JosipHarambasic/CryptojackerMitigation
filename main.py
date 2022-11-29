nethogs = open("nethogs.txt", "r")
whitelistFile = open("whitelist.txt", "r")
runningTasks = open("check.txt", "r")

parsedFile = []
for i in nethogs:
    index = 0
    if not i.startswith("Refreshing:"):
        for j in i:
            if j.isalpha():
                i = i[index:].strip().replace('/(\r\n|\n|\r)/gm', "")
                break
            index += 1
        if len(i) > 1:
            file = (" ".join(i.split()).split(" ")[::-1])
            ind = 0
            for k in file[2]:
                if k.isalpha():
                    parsedFile.append(file[2][ind:])
                    break
                ind+=1
runningT = {}
for i in parsedFile:
    counter = 0
    check = 0
    left = 0
    i = i[::-1]
    flag = True
    temp = None
    for j in i:
        if j == "/":
            counter += 1
        if counter == 1 and flag:
            left = check + 1
            flag = False
        if counter == 2:
            runningT[i[check+1:][::-1]] = i[left:check][::-1]
            break
        check += 1
print(runningT)


whitelistTasks = []
for i in whitelistFile:
    if i != "?":
        whitelistTasks.append(i.strip())

output = []
for i in runningTasks:
    var = (" ".join(i.split()).split(" "))
    if var[0] != "?":
        value = " ".join(i.split()).split(" ")
        output.append(value)

checkedTasks = []
for i in output:
    checkedTasks.append(i[2])

unknownTasks = list(set(checkedTasks)-set(whitelistTasks))

getCorrespondingPID = {}
for i in unknownTasks:
    for j in output:
        if i == j[2]:
            getCorrespondingPID[i] = j[0]

