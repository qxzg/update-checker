import os
import glob

modules = glob.glob(os.path.dirname(__file__)+"/*.py")
tasks = [os.path.basename(f)[:-3] for f in modules]
tasks.remove('__init__')
