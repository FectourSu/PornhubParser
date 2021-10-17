import csv
import os
import random
class Converter:
    @staticmethod
    def ConvertToList(file):
        if os.path.isfile(file):
            with open(file, "r") as f:
                lines = csv.reader(f, delimiter='\n')
                items = [str(s) for line in lines for s in line]
                return items
        return Exception(f"No such file or directory {file}")

