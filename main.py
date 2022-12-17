import subprocess
import time
from Parser import Parser

def mitigateCryptojacker():

    # We need to update the db to locate the actual target file
    subprocess.Popen("rm nethogs.txt", shell=True, stdout=subprocess.PIPE)
    subprocess.Popen("updatedb", shell=True, stdout=subprocess.PIPE)

    print("started networktracking")
    startNetworkTracking()
    print("finished networktracking")

    maliciousPrograms = Parser("whitelist.txt", "nethogs.txt").parse()
    if len(maliciousPrograms) > 0:
        for i in maliciousPrograms:
            # cpu limit 'cpulimit -p PID -l 10'
            print(maliciousPrograms[i])
            print(i)
            subprocess.Popen("cpulimit -p " + maliciousPrograms[i] + " -l 10 -b", shell=True, stdout=subprocess.PIPE)
            time.sleep(10)
            subprocess.Popen("kill -9 " + maliciousPrograms[i], shell=True, stdin=subprocess.PIPE)
            print("killed process: " + i + " with PID: " + maliciousPrograms[i])

            # subprocess.Popen('kill -9' + str(i), shell=True, stdout=subprocess.PIPE)
    else:
        print("no sus task found")

    # temp = subprocess.Popen('locate brew', shell=True, stdout=subprocess.PIPE)
    # get the output as a string
    # for i in temp.stdout:
    #    outputlist.append(str(i.strip(), "utf-8"))
    # store the output in the list


def startNetworkTracking():
    outputFileName = "nethogs.txt"
    process = subprocess.Popen("nethogs -t -v 2 > " + outputFileName, shell=True, stdin=subprocess.PIPE)
    time.sleep(60)
    subprocess.Popen("pkill -f nethogs", shell=True, stdin=subprocess.PIPE)
    print("--- output saved in " + outputFileName)


if __name__ == '__main__':
    mitigateCryptojacker()