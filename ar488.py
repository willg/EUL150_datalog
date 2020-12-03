class ar488:
    def __init__(self, dev):
        self.dev = dev

    def get_version(self):
        self.dev.write("++ver\n")
        ver = self.dev.read(60)
        return ver

    def auto_mode_2(self):
        """auto is set to "on-query".  controller will auto read afer ?"""
        self.dev.write("++auto 2\n")

    def auto_query(self):
        self.dev.write("++auto\n")
        data = self.dev.read(20)
        return data

