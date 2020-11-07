import config 
import task
import importlib

im = ["AX86U_official_sourcecode", "AX86U_official_firmware"]
mpkg='AX86U_official_sourcecode'
imp = importlib.import_module('task.'+im[0])
imp.get_version()
del imp
imp = importlib.import_module('task.'+im[1])
imp.get_version()
# print(task.AX86U_official_sourcecode.get_version())
# AX86U_official_sourcecode.get_version()