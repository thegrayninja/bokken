import threading
from queue import Queue
import time
import socket
import sys

# a print_lock is what is used to prevent "double" modification of shared variables.
# this is used so while one thread is using a variable, others cannot access
# it. Once done, the thread releases the print_lock.
# to use it, you want to specify a print_lock per thing you wish to print_lock.
print_lock = threading.Lock()
q = Queue()
Ports = 443


def main():
    Hosts = CommandlineArgs()
    print(type(Hosts))
    if "<class 'list'>" == type(Hosts):
        for i in Hosts:
            PortThreading(i.strip())
            print(i)
    else:
        for i in Hosts:
            PortThreading(i.strip())
            print(i)

def OpenFile(FileName):
    FileName = open(FileName, "r")
    Data = FileName.readlines()
    FileName.close()
    print(Data)
    return(Data)

def CommandlineArgs():
    HostName = ""
    FileName = ""
    global Ports
    if len(sys.argv) == 2:  #ie, no switches given. just 1 argument
        if sys.argv[1][0] == "-":  #currently, only switches are prefixed with "-"
            HelpMenu()
        else:
            HostName = sys.argv[1]
            print("Hostname to test is {}".format(sys.argv[1]))
    elif len(sys.argv) == 1:  #ie, no args given
        print("""
        Help Menu
    
        you did something wrong.
        """)
    else:
        for i in range(len(sys.argv)):  #ie, looking for switches and the associated file
                if "-f" == sys.argv[i]:
                    print("yes, we will import a file...")
                    FileName = sys.argv[i+1]
                    print("Filename to be imported is {}".format(FileName))
                elif "-p" == sys.argv[i]:
                    Ports = sys.argv[i+1]
                elif "-s" == sys.argv[i]:
                    print("shutup fool")
    if FileName != "":
        Hosts = OpenFile(FileName)
        return(Hosts)
    else:
        return(HostName)




target = 'operationecho.com'


# ip = socket.gethostbyname(target)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open!')
        con.close()
    except:
        pass
        #print('port', port, 'is closed :(')


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        portscan(worker)

        # completed with the job
        q.task_done()


# Create the queue and threader

def PortThreading(target):

    print("\n\n**********\nWorking on target {}\n".format(target))
    # how many threads are we going to allow for
    for x in range(30):
        t = threading.Thread(target=threader)

        # classifying as a daemon, so they will die when the main dies
        t.daemon = True

        # begins, must come after daemon definition
        t.start()

    start = time.time()

    # 100 jobs assigned.
    #Ports = [80, 443, 22]
    #for worker in range(1, 450):
    try:
        worker = int(Ports)
        q.put(worker)
    except:
        for worker in Ports:
            print(int(worker))
            q.put(int(worker))

    # wait until the thread terminates.
    q.join()

if __name__ == main():
    main()