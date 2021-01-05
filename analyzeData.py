import argparse

def main(input_filename):

    t = input_filename.split('.')
    output_filename = t[0] + '_withWhAh' + '.' + t[1]
    print("Input File: " + input_filename)
    print("Output File: " + output_filename)

    f_in = open(input_filename, 'r')
    f_out = open(output_filename, 'w')

    amp_seconds_total = 0
    watt_seconds_total = 0

    for line in f_in.readlines():
        line = line.strip()
        data = line.split(',')

        try:
            v = float(data[0])
            i = float(data[1])
            t = float(data[2])

            # skip the first sample
            if t == 0:
                t_last = 0
                pass

            # calculate how many seconds elapsed in last step
            t_step = t - t_last

            amp_seconds_step = t_step * i
            watt_seconds_step = amp_seconds_step * v

            amp_seconds_total += amp_seconds_step
            watt_seconds_total += watt_seconds_step

            t_last = t

            outline = line
            outline += ", " + str(amp_seconds_total)
            outline += ", " + str(amp_seconds_total / 3600)
            outline += ", " + str(watt_seconds_total)
            outline += ", " + str(watt_seconds_total/ 3600)
            outline += "\n"
            f_out.write(outline)

        except ValueError:
            f_out.write(line + '\n')
            pass


    f_in.close()
    f_out.close()

    amp_hours = amp_seconds_total / 3600
    watt_hours = watt_seconds_total / 3600
    print("Amp Hours: " + str(amp_hours) )
    print("Watt Hours: " + str(watt_hours) )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file')

    args = parser.parse_args()
    main(args.file)
