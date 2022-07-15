import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from E911 import EID_MUBARAK
    EID_MUBARAK()
elif bit == '32bit':
    from E32 import EID_MUBARAK
    EID_MUBARAK()
