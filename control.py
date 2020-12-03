import serial

def init_gpib():
    print("configuring GPIB controller")
    print("")
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=0.1)
    ser.write(b'++ver\n')
    data = ser.read(100)
    print(data)
    ser.write(b'++auto 2\n')

    ser.write(b'++auto \n')
    data = ser.read(100)
    print("auto: " + str(data))

    return ser

def main():
    ser = init_gpib()
    ser.write(b"LOAD:?\n")
    data = ser.read(100)
    print(data)

    ser.write(b"MEAS:V?\n")
    data = ser.read(100)
    print("voltage: " + str(data))

    ser.write(b"MEAS:C?\n")
    data = ser.read(100)
    print("current: " + str(data))

    ser.close()

if __name__ == "__main__":
    main()
