import serial
import ar488
import eul_150
import time
import argparse

def setup(dev):
    print("connecting AR488 on " + dev)
    ser = serial.Serial(dev, 115200, timeout=0.1)

    gpib = ar488.ar488(ser)
    print("Version: " + gpib.get_version() )
    gpib.auto_mode_2()

    return gpib

def main(filename, serial_port, term_voltage, discharge_current):
    gpib = setup(serial_port)
    load = eul_150.eul_150(gpib)
    print("Model: " + load.model_query())

    load.range_set_0()
    time.sleep(0.1)
    load.current_set(discharge_current)
    time.sleep(0.1)
    load.load_on()
    time.sleep(0.1)
    f = open(filename, "w")
    f.write("termination voltage: {} V\n".format(term_voltage))
    f.write("discharge current: {} A\n".format(discharge_current))
    f.write("voltage, current, time, amp-hour, watt-hour\n")
    notes = input("Test Notes:")
    f.write("Notes: " + notes + "\n")
    f.flush()

    t = 0
    t_step = 1 # seconds

    amp_seconds_total = 0
    watt_seconds_total = 0

    while(True):
        v = load.measure_voltage()
        i = load.measure_current()
        amp_seconds = t_step * i
        watt_seconds = amp_seconds * v

        amp_seconds_total += amp_seconds
        watt_seconds_total += watt_seconds
        AHr = amp_seconds_total / 3600
        WHr = watt_seconds_total / 3600
        # print("Voltage: " + str(v))
        # print("Current: " + str(i))
        log = "{}, {}, {}, {}, {}\n".format(v, i, t, AHr, WHr)
        print(log.strip())
        f.write(log)
        f.flush()

        if v <= term_voltage:
            break
        time.sleep(t_step)
        t += t_step

    load.load_off()
    gpib.close()
    print("Data written to: " + filename)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('serial_port')
    parser.add_argument('term_voltage')
    parser.add_argument('discharge_current')

    args = parser.parse_args()
    main(args.filename,
            args.serial_port,
            float(args.term_voltage),
            float(args.discharge_current))
