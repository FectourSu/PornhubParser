import os
import subprocess
import sys
class Module:
    @staticmethod
    def install(package): # Used to install packages
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])    
        