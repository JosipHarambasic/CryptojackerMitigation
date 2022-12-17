class Parser:
    def __init__(self, whitelist, collectedDataFile):
        self.whitelist = whitelist
        self.collectedDataFile = collectedDataFile

    def parse(self):
        nethogs = open(self.collectedDataFile, "r")
        whitelistFile = open(self.whitelist, "r")

        for i in whitelistFile:
            whitelistFile = i.split(",")

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
                    runningT[i[check + 1:][::-1]] = i[left:check][::-1]
                    break
                check += 1

        for i in whitelistFile:
            if i in runningT:
                runningT.pop(i)
        return runningT
