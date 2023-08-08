import serial

ser = serial.Serial('COM6', 9600, timeout=1)

for i in range(1):
    data = int.from_bytes(ser.readline().decode('utf-8'))
    

