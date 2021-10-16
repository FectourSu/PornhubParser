import glob
import os
from abc import abstractmethod

class IFolder:
    @abstractmethod
    def Clear(path:str):
        raise NotImplementedError

    @abstractmethod
    def Create(path: str):
        raise NotImplementedError

class Folder(IFolder):
    @staticmethod
    def Clear(path: str):
        r = glob.glob(path)
        for i in r:
            os.remove(i)

    @staticmethod
    def Create(path: str):
        if not os.path.exists(path):
            os.mkdir(path)