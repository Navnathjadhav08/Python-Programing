import psutil
import time
import schedule
import os
import sys

def CreateLog(FolderName = "x"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    FileName = os.path.join(FolderName,"x%s.log" %(time.ctime()))
    
    fd = open(FileName, "w")
    separator = "-"*70

    fd.write(separator + "\n")
    fd.write(" Process Log"+ "\n")
    fd.write("Log file created at : "+time.ctime() + "\n")
    fd.write(separator + "\n")
    
    Arr = GetProcessInfo()

    for data in Arr:
        fd.write("%s \n" %data)
    
    fd.write(separator + "\n")

    fd.close()

def GetProcessInfo():
    listprocess = []    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listprocess.append(proc.info)
    
    return listprocess
    
def main():

    schedule.every(int(sys.argv[1])).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()