import subprocess

# sudo /usr/libexec/locate.updatedb
import time

from Parser import Parser


def mitigateCryptojacker():
    outputlist = []
    # Iterate over all the servers in the list and ping each server
    sudo_password = '1230'
    command = 'updatedb'
    command = command.split()

    # Parse the output file that could have malicious programs

    # We need to update the db to locate the actual target file
    cmd1 = subprocess.Popen(['echo', sudo_password], stdout=subprocess.PIPE)
    # subprocess.Popen(['sudo', '-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)

    maliciousPrograms = Parser("whitelist.txt", "nethogs.txt").parse()
    for i in maliciousPrograms:
        # cpu limit 'cpulimit -p PID -l 10'
        print(maliciousPrograms[i])
        subprocess.Popen("cpulimit -p " + maliciousPrograms[i] + " -l 10")
        # subprocess.Popen('kill -9' + str(i), shell=True, stdout=subprocess.PIPE)

    temp = subprocess.Popen('locate brew', shell=True, stdout=subprocess.PIPE)
    # get the output as a string
    for i in temp.stdout:
        outputlist.append(str(i.strip(), "utf-8"))
    # store the output in the list

    return outputlist


def startNetworkTracking():
    print("started network tracking")
    outputFileName = "nethogs.txt"
    process = subprocess.Popen("nethogs -t -v 2 > " + outputFileName, shell=True, stdin=subprocess.PIPE)
    time.sleep(20)
    process.kill()
    print("--- finished network tracking ---")
    print("--- output saved in " + outputFileName)


if __name__ == '__main__':
    output = mitigateCryptojacker()

    # Uncomment the following lines to print the output of successful servers
