import glob
import os
from abc import abstractmethod

class Folder():
    @staticmethod
    def Clear(folder:str):
        r = glob.glob(folder)
        for i in r:
            os.remove(i)

    @staticmethod
    def Create(folder:str):
        if not os.path.exists(folder):
            os.mkdir(folder)
        return folder
