class Parser:
    def __init__(self, whitelist, collectedDataFile):
        self.whitelist = whitelist
        self.collectedDataFile = collectedDataFile

    def parse(self):
        nethogs = open(self.collectedDataFile, "r")
        whitelistFile = open(self.whitelist, "r")

        for i in whitelistFile:
            whitelistFile = i.split(",")

        countNetworkStamps = 0
        parsedFile = []
        for i in nethogs:
            index = 0
            if i.startswith("Refreshing:"):
                countNetworkStamps += 1
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
                        ind += 1
        runningT = {}
        for i in parsedFile:
            counter = 0
            check = 0
            left = 0
            i = i[::-1]
            flag = True
            for j in i:
                if j == "/":
                    counter += 1
                if counter == 1 and flag:
                    left = check + 1
                    flag = False
                if counter == 2:
                    runningT[i[left:check][::-1]] = i[check + 1:][::-1]
                    break
                check += 1


        maliciousTasks = {}
        for k,v in runningT.items():
            if v not in whitelistFile:
                maliciousTasks[k] = v
        print(maliciousTasks)
        return runningT


# TODO create a output which looks like this {PID: {name:xmrig, sendBytes:X, recvBytes:X}}
# TODO send and receive can be calculated with the first appearance of the task minus last one
a = Parser("whitelist.txt", "nethogs.txt").parse()
for i in a:
    print(i)