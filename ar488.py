class ar488:
    def __init__(self, dev):
        self.dev = dev

    def write(self, data):
       string = data + '\n'
       string = str.encode(string)
       self.dev.write(string)

    def read(self, length):
        return str( self.dev.read(length).strip(), 'utf-8')

    def close(self):
        self.dev.close()

    def get_version(self):
        self.write('++ver')
        ver = self.read(60)
        return ver

    def auto_mode_2(self):
        """auto is set to "on-query".  controller will auto read afer ?"""
        self.write('++auto 2')

    def auto_query(self):
        self.write('++auto')
        data = self.read(20)
        return data
