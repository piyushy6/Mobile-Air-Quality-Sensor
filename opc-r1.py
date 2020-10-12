import serial, time, struct, csv, datetime, os
import pandas as pd
from usbiss.spi import SPI
from opc import OPCR1
from opc.exceptions import SpiConnectionError, FirmwareVersionError
from time import sleep

def logfilename():
    now = datetime.datetime.now()
    return 'OPC_R1_%0.4d-%0.2d-%0.2d_%0.2d-%0.2d-%0.2d.csv' % \
                (now.year, now.month, now.day,
                 now.hour, now.minute, now.second)


#try:
#    path = str(os.environ['outputPath_opc'])
#except:
#    print("could not find env variable ")
#    path = ""
  
interval = 10

spi = SPI("/dev/ttyACM0",mode=1, max_speed_hz=500000)

alpha = OPCR1(spi)

writeLog = 1

print("create csv file")

path= 'OPC CSV'   #To save CSV in OPC CSV folder
if writeLog:

    csv_file = os.path.join(path, logfilename())
    csv_file = open(csv_file, mode='w')

    fieldnames = ["time","PM2.5","Temp."]


    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    csv_file.flush()

#Turns on OPC-R1
alpha.on()
sleep(1)

print("--------------")
print("starting reading loop")
print("--------------")



try:
    while True:
        data = alpha.histogram()

        print("PM2.5 Value", data["PM2.5"]) 

        writer.writerow({'time':str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                         'PM2.5':int(data["PM2.5"]),"Temp.":(data['Temperature'])})            
        
        sleep(1) # THIS Sleep is used to Vary the "Sampling Rate"
        
        
 #Use this when you want to  run opc for fixed time
#        if index == 50:
#            readLoop = False
        

except KeyboardInterrupt:
    print("Press Ctrl-C to terminate while statement")
    pass        
# Turn the device off
alpha.off()





