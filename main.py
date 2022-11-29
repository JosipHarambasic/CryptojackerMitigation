topOutput = open("nethogs.txt", "r")
whitelist = open("whitelist.txt", "r")
check = open("check.txt", "r")
outputWhitelist = []
for i in whitelist:
    if i != "?":
        outputWhitelist.append(i.strip())

output = []
for i in check:
    var = (" ".join(i.split()).split(" "))
    if var[0] != "?":
        value = " ".join(i.split()).split(" ")
        output.append(value)

checkedTasks = []
for i in output:
    checkedTasks.append(i[2])

unknownTasks = list(set(checkedTasks)-set(outputWhitelist))
print(output)
print(outputWhitelist)
print(unknownTasks)

getCorrespondingPID = {}
for i in unknownTasks:
    for j in output:
        if i == j[2]:
            getCorrespondingPID[i] = j[0]
print(getCorrespondingPID)
