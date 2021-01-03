class eul_150:
    def __init__(self, dev):
        self.dev = dev

    def load_is_on(self):
        self.dev.write('LOAD:?')
        data = self.dev.read(20)
        return data

    def load_on(self):
        self.dev.write('LOAD:ON')

    def load_off(self):
        self.dev.write('LOAD:OFF')

    def action_mode_query(self):
        self.dev.write('AMODE:?')
        data = self.dev.read(20)
        return data

    def action_mode_current(self):
        self.dev.write('AMODE:C')

    def range_query(self):
        self.dev.write('RANG:?')
        data = self.dev.read(20)
        return data

    def range_set_0(self):
        self.dev.write('RANG:0')

    def range_set_1(self):
        self.dev.write('RANG:1')

    def range_set_2(self):
        self.dev.write('RANG:2')

    def reset(self):
        self.dev.write('REST')

    def model_query(self):
        self.dev.write('MDEL:?')
        data = self.dev.read(20)
        return data

    def current_set(self, value):
        data = 'CSET:'+"{:.3e}".format(value)
        self.dev.write(data)

    def current_set_query(self):
        self.dev.write('CSET:?')
        data = self.dev.read(20)
        return data

    def measure_voltage(self):
        self.dev.write('MEAS:V?')
        data = float(self.dev.read(20))
        return data

    def measure_current(self):
        self.dev.write('MEAS:C?')
        data = float(self.dev.read(20))
        return data

    def measure_power(self):
        self.dev.write('MEAS:W?')
        data = float(self.dev.read(20))
        return data
