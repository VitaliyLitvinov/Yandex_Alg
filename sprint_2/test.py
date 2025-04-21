class AddRegionInfo:
    def __init__(self, geo_file_name, in_log_file_name, out_log_file_name):
        self.geo_data = self.read_geo_data(geo_file_name)
        self.process_log(in_log_file_name, out_log_file_name)

    def read_geo_data(self, file_name):
        f = open(file_name, 'r', encoding='utf8')
        return f.readlines()

    def process_log(self, in_file_name, out_file_name):
        f = open(in_file_name, 'r', encoding='utf8')
        for line in f.readline():
            ip = line.split()[0]
            for geo in self.geo_data:
                gf = geo.split()


        file_out = open(out_file_name, 'w', encoding='utf8')






if __name__ == '__main__':
    AddRegionInfo('geobase.txt', 'input.txt', 'output.txt')
