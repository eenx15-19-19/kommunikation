

def Rx(sLast):
    data=[]
    mottagenData=[0, 1, 1, 1, 1, 1, 1, 0, 1, 0] #fakedata, ta bort är kör skarpt
    #sätt mottagardata=[] för att nollställa
    #Ta emot mottagardata
    mottagenData=ser.read(8)
    if len(mottagenData)>1:
        sekvens=mottagenData[0]# Sekvensnummer blir aktuella paketets nummer
        if sLast!=sekvens:
            sLast=sekvens #Uppdaterar sLast pga ok paket
            ser.write(sekvens) #skickar ack ok
            data=mottagenData[:]
            print('Inget fel')
            return data
        else:
            mottagenData[-1]=0 #Sätter paritybit för att fakedata ej ska ge oändlig loop
            ser.write(sLast) #Skickar ACK NOK
            mottagenData[-1]=0
            print('Ett fel har upptackts')
            #om data inte uppdateras så hämtas nytt paket

def tx(sLast,algData):
    if sLast == 1:
        algData=[0, algData]
    else :
        algData=[1, algData]
    ser.write(algData)
# Här ska allt sändas:)


def main():
    sLast=1
    finish=False
    i=0
    while(finish==False):
        information=Rx(sLast)
        if (information[0]=='sLast' and sLast==1):
            sLast=0
        elif (information[0]=='sLast' and sLast==0):
            sLast=1
        #upp daterar sLast
        data=information[1:-1]
        algDataFake=[0, 1, 0, 0]
        sLast= tx(sLast, algDataFake)
        #Skricka data vidare till algoritm.
        #Loop för att köra i antal gånger
        i=1+i
        if i==2:
            print(information)
            print(data)
            finish=True


import time
import serial

ser = serial.Serial(
    port='/dev/serial0',
    baudrate=115200
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)


main()


