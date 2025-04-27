import ipaddress
class AddRegionInfo:
    def __init__(self, geo_file_name, in_log_file_name, out_log_file_name):
        self.geo_data = self.read_geo_data(geo_file_name)
        self.process_log(in_log_file_name, out_log_file_name)

    def read_geo_data(self, file_name):
        f = open(file_name, 'r', encoding='utf8')
        return f.readlines()

    def process_log(self, in_file_name, out_file_name):
        f = open(in_file_name, 'r', encoding='utf8')
        lines = f.readlines()

        f = open(out_file_name, 'w', encoding='utf8')
        for line in lines:
            fields = line.split()
            ip = fields[0]
            fields[-1] = fields[-1].strip()

            for geo in self.geo_data:
                gf = geo.split()
                if self.is_bigger(ip, gf[0]) and self.is_bigger(gf[1], ip) and len(gf) == 4:
                    fields = [gf[2].strip(), gf[3].strip()] + fields
                    f.write(' '.join(fields) + '\n')
                    break
                elif self.is_bigger(ip, gf[0]) and self.is_bigger(gf[1], ip) and len(gf) == 3:
                    fields = [gf[2].strip()] + fields
                    f.write(' '.join(fields) + '\n')
                    break
    def is_bigger(self, a1, a2):
        a1s = a1.split('.')
        a2s = a2.split('.')
        if len(a1s) < len(a2s) or a1s[0] < a2s[0]:
            return False
        if len(a1s) < len(a2s) or a1s[1] < a2s[1]:
            return False
        if len(a1s) < len(a2s) or a1s[2] < a2s[2]:
            return False
        if len(a1s) < len(a2s) or a1s[3] < a2s[3]:
            return False
        return True




if __name__ == '__main__':
    AddRegionInfo('geobase.txt', 'input.txt', 'output.txt')
