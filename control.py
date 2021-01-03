import serial
import ar488
import eul_150
import time

def setup(dev):
    print("connecting AR488 on " + dev)
    ser = serial.Serial(dev, 115200, timeout=0.1)

    gpib = ar488.ar488(ser)
    print("Version: " + gpib.get_version() )
    gpib.auto_mode_2()

    return gpib

def main():
    term_voltage = 20
    discharge_current = 2.0
    gpib = setup("/dev/ttyACM0")
    load = eul_150.eul_150(gpib)
    print("Model: " + load.model_query())

    load.range_set_0()
    time.sleep(0.1)
    load.current_set(discharge_current)
    time.sleep(0.1)
    load.load_on()
    time.sleep(0.1)
    f = open("data.txt", "w")
    f.write("termination voltage: {} V\n".format(term_voltage))
    f.write("discharge current: {} A\n".format(discharge_current))
    f.write("time, voltage, current\n")
    f.flush()

    t = 0

    while(True):
        v = load.measure_voltage()
        i = load.measure_current()
        print("Voltage: " + str(v))
        print("Current: " + str(i))
        log = "{}, {}, {}\n".format(v, i, t)
        f.write(log)
        f.flush()

        if v <= term_voltage:
            break
        time.sleep(1)
        t += 1

    load.load_off()
    gpib.close()

if __name__ == "__main__":
    main()
