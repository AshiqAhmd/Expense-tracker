from datetime import datetime
import csv
dt= datetime.today()
dt= dt.strftime("%c")
filename= "Test.csv"
exp=[]
stopped = False
with open(filename,'a',newline="") as file:
    csvwriter = csv.writer(file)
    while not stopped:
        xp = int(input("What is the expense (type 0 to stop): "))
        if xp == 0:
            stopped = True
        else:
            csvwriter.writerow([dt,xp])
            exp.append(xp)
file.close()
print("Your expenses today are", exp)
print("your total is", sum(exp))