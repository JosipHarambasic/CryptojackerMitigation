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
            subprocess.Popen("cpulimit -p " + maliciousPrograms[i] + " -l 10 -b", shell=True, stdout=subprocess.PIPE)
            print("throttling the cpu usage to 10% of a CPU for 10 sec.")
            time.sleep(10)
            try:
                subprocess.Popen("kill -9 " + i, shell=True, stdin=subprocess.PIPE)
            except:
                print("Process: " + i + "already killed")
            try:
                subprocess.Popen("pkill -f" + maliciousPrograms[i], shell=True, stdin=subprocess.PIPE)
            except:
                print("Process: " + maliciousPrograms[i] + "already killed")

            print("killed process: " + maliciousPrograms[i] + " with PID: " + maliciousPrograms[i])
            output = subprocess.Popen("locate " + maliciousPrograms[i], shell=True, stdin=subprocess.PIPE)
            for j in output.stdout:
                print(j)
    else:
        print("no sus task found")

    # temp = subprocess.Popen('locate brew', shell=True, stdout=subprocess.PIPE)
    # get the output as a string
    # for i in temp.stdout:
    #    outputlist.append(str(i.strip(), "utf-8"))
    # store the output in the list


def startNetworkTracking():
    outputFileName = "nethogs.txt"
    subprocess.Popen("nethogs -t -v 2 > " + outputFileName, shell=True, stdin=subprocess.PIPE)
    time.sleep(60)
    subprocess.Popen("pkill -f nethogs", shell=True, stdin=subprocess.PIPE)
    print("--- output saved in " + outputFileName)


if __name__ == '__main__':
    mitigateCryptojacker()