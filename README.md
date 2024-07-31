# MAX6675-Temperature-Logger
## Overview
This project aims to measure temperature using MAX6675 and a K-type thermocouple as an external sensor add-on with ExpEYES. In this case we have used Serial Peripheral Interface (SPI) communication protocol between the thermocouple module MAX6675 and ExpEYES. 
Download the "MAX6675.py" file and run to measure temperature. 

## Required Apparatus :
1. ExpEYES latest model (SEELAB 3.0, with SPI expansion bus)
2. Thermocouple module (MAX6675)
3. Temperature Sensor (PT1000)
4. K-type thermocouple 
5. Jumper wires (with alligator clips, optional)

## Procedure:
### Experimental Setup
1. **Connections**:
   - Connect K-type thermocouple with MAX6675 thermocouple module
   - Connect ExpEYES (5V, GND, SCK, CS1, SDO) to MAX6675 (VCC, GND, SCK, CS, SO).
   - Place the K-type thermocouple probe at required position.
2. **Data Acquisition**:
   - Connect ExpEYES to PC via USB.
   - Download and run the provided "MAX6675.py" script.
   - Data [time(s), temperature(C)] will be saved to "Max6675.dat".
> ### NOTES :
> - Don't forget to delete the existing data file "Max6675.dat", if you are running the "MAX6675.py" script multiple times.

## Special thanks to:

- Wholehearted thanks to the entire Inter-University Accelerator Centre (IUAC), New Delhi, India team especially Er. V.V.V. Satyanarayana, Mr. Abhijit Sarkar, and Dr. Ajith Kumar B. P. for developing the device and conducting the training program.
  
- Heartfelt thanks to Dr. Jithin B.P. from CSpark Research for his invaluable assistance and support. His expertise and guidance were instrumental in the successful completion of this project. Dr. Jithin, your unwavering help and dedication are deeply appreciated.

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
![CC BY 4.0](https://i.creativecommons.org/l/by/4.0/88x31.png)

## Author
  - Dr. Ujjwal Ghanta

Thanks
