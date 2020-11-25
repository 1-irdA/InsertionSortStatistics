import csv

"""
    File operations
"""
class FileUtils:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode 

    def write_file(self, to_write):
        if to_write[0] == '0':
            to_write[0] = 'random'
        with open(self.filename, self.mode) as my_file: 
            writer = csv.writer(my_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(to_write)
