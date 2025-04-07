import serial
import serial.tools.list_ports

ports_list = list(serial.tools.list_ports.comports())
if len(ports_list) <= 0:
    print("No COM")
else:
    print("COM")
    for comport in ports_list:
        print(list(comport)[0], list(comport)[1])