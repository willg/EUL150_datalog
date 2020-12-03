class eul_150:
    def __init__(self, dev):
        self.dev = dev

    def load_is_on(self):
        self.dev.write(b"LOAD:?\n")
        data = self.dev.read(20)
        return data

    def load_on(self):
        self.dev.write(b"LOAD:ON\n")

    def load_off(self):
        self.dev.write(b"LOAD:OFF\n")

    def action_mode_query(self):
        self.dev.write(b"AMODE:?")
        data = self.dev.read(20)
        return data

    def action_mode_current(self):
        self.dev.write(b"AMODE:C\n")

    def range_query(self):
        self.dev.write(b"RANG:?")
        data = self.dev.read(20)
        return data

    def range_set_0(self):
        self.dev.write(b"RANG:0\n")

    def range_set_1(self):
        self.dev.write(b"RANG:1\n")

    def range_set_2(self):
        self.dev.write(b"RANG:2\n")

    def reset(self):
        self.dev.write(b"REST"\n)

    def model_query(self):
        self.dev.write(b"MDEL:?\n")
        data = self.dev.read(20)
        return data

    def current_set(self, value):
        self.dev.write(b"CSET:"+str(value)+b"\n")

    def current_set_query(self):
        self.dev.write(b"CSET:?\n")
        data = self.dev.read(20)
        return data

    def measure_voltage(self):
        self.dev.write(b"MEAS:V?\n")
        data = self.dev.read(20)
        return data

    def measure_current(self):
        self.dev.write(b"MEAS:V?\n")
        data = self.dev.read(20)
        return data

    def measure_power(self):
        self.dev.write(b"MEAS:W?\n")
        data = self.dev.read(20)
        return data
