''' Program for temperature measurement by MAX6675 and K-type thermocouple(SPI Communication)
    on 23/04/2024 
'''

# Establish Connection
import eyes17.eyes
p = eyes17.eyes.open()

# Import python library 
import time, math
import numpy as np

t0=time.time()                      # Time initialization
while True:
    p.SPI.start('CS1')
    val = p.SPI.send16(0xFFFF)
    t=time.time()-t0
    p.SPI.stop('CS1')        
    Temperature = (val>>3)*0.25
    if(val&0x4):
        print('Thermocouple not attached. : ')
        #return
    else:
        print('Temp: ',Temperature)
        file = open ("Max6675.dat", "a") # Appending file
        file.write("{0:4.2f} {1:4.2f}\n".format(t,Temperature))
    time.sleep(1)


