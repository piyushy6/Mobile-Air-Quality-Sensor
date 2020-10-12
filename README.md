# Rpi-Air-Quality-Sensor

py-opc is the python library for connecting Alphasense Optical Particle Counter to Raspberry Pi.

https://py-opc.readthedocs.io/en/latest/

I am connecting OPC-R1 to Rpi using SPI-USB connector. So I use pyusbiss library

Installation :

1.) For adding py-opc on RPi :

!wget https://github.com/FlorentinBulotUoS/py-opc

2.) For pyusbiss :

$ pip3 install pyusbiss

Running this save PM data as a CSV file in OPC CSV folder in RPi:

$ python3 opc-r1.py

License for using the py-opc Library is added at Library file
