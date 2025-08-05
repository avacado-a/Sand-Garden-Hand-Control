import serial
import time
ports = list(serial.tools.list_ports.comports())
found = False
for p in ports:
    if 'USB-SERIAL CH340' in p.description:
        found = True
        ser = serial.Serial(p.device,9600,timeout=0.5)
if not found:
    print("We couldn't find the Arduino Nano. Put the port name you see under the title on the Hack Pack IDE into the port_name variable")
    port_name = "We couldn't find the Arduino Nano. Put the port name you see under the title on the Hack Pack IDE right here"
    ser = serial.Serial(port_name, 9600, timeout=0.5)
def waitTillnRecieved(n:str):
    readLine = "" if n != "" else " "
    while readLine!=n:
        bs = ser.readline()
        readLine = bs.decode("utf-8").rstrip()
def printSerial(a):
    ser.write(str(a).encode('utf-8'))

waitTillnRecieved("colo")
printSerial("<n>")
waitTillnRecieved("confirming!")
angle = 0
position = 0
printSerial("<"+str(angle)+">")
waitTillnRecieved(str(angle))
printSerial("<"+str(position)+">")
waitTillnRecieved(str(position))
waitTillnRecieved("done")
x=0
while x<2000:
    printSerial("<"+str(angle)+">")
    waitTillnRecieved(str(angle))
    printSerial("<"+str(angle)+">")
    waitTillnRecieved(str(angle))
    printSerial("<"+str(position)+">")
    waitTillnRecieved(str(position))
    waitTillnRecieved("done")
    file = open("liveDrawComms.txt","r")
    a = file.read()
    file.close()
    a = a.split("\n")
    b = a[0].split(",")
    try:
        position=int(b[1])
        angle=int(b[0])
    except IndexError:
        pass
    print("Moving to {} mm at {} degrees".format(position,angle))
    with open("liveDrawComms.txt", 'r') as f:
        lines = f.readlines()
    with open("liveDrawComms.txt", 'w') as f:

        f.writelines(lines[1:])
