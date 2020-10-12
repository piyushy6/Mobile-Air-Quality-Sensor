# Rpi-Air-Quality-Sensor

py-opc
It is the python library for connetcing Alphasense Optical Particle Counter to Raspberry Pi.

https://py-opc.readthedocs.io/en/latest/

I am connecting OPC-R1 to Rpi using SPI-USB connector. So I use pyusbiss library

Installation :

1.) For py-opc on RPi :

$ pip install py-opc 

To get OPC-R1 class, fork FlorentinBulotUoS/py-opc 
This will add the OPC-R1 class, which is not currently present in py-opc

2.) For pyusbiss :

$ pip3 install pyusbiss

Running this save PM data as a CSV file OPC CSV folder:

$ python3 opc-r1.py

License for using the py-opc Library is added at Library file
