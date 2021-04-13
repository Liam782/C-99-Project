import os
import shuttle
import time

ctime = os.stat(path).st_ctime
return ctime
ctime = time.time()

if os.path.exists(path):
    os.walk(path)

    if time > ctime:
        if path.isfile():
            os.remove(path)
        elif path.isdir():
            shutil.rmtree(path)

else:
    print("Path not found!")