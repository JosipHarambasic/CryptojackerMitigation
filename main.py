import subprocess


# sudo /usr/libexec/locate.updatedb

def ping():
    outputlist = []
    # Iterate over all the servers in the list and ping each server
    sudo_password = '1230'
    command = 'updatedb'
    command = command.split()

    #cmd1 = subprocess.Popen(['echo', sudo_password], stdout=subprocess.PIPE)
    #subprocess.Popen(['sudo', '-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)
    temp = subprocess.Popen('locate brew', shell=True, stdout=subprocess.PIPE)
    # get the output as a string
    for i in temp.stdout:
        outputlist.append(i)
    # store the output in the list

    return outputlist


if __name__ == '__main__':

    # Get the list of servers from the text file
    servers = ["www.google.com", "www.facebook.com"]
    # Iterate over all the servers that we read from the text file
    # and remove all the extra lines. This is just a preprocessing step

    outputlist = ping()

    # Uncomment the following lines to print the output of successful servers
    print(outputlist)
    for i in outputlist:
        print(i)
