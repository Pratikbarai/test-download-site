import os
import subprocess
import time

CREATE_NO_WINDOW = 0x08000000
work_dir = "C:\\Temp\\lolbin_test"
os.makedirs(work_dir, exist_ok=True)
os.chdir(work_dir)

# Create 5 folders/files silently using LOLBins
subprocess.run('mkdir folder1', shell=True, creationflags=CREATE_NO_WINDOW)
subprocess.run('mkdir folder2', shell=True, creationflags=CREATE_NO_WINDOW)
subprocess.run('type nul > file1.txt', shell=True, creationflags=CREATE_NO_WINDOW)
subprocess.run('type nul > file2.txt', shell=True, creationflags=CREATE_NO_WINDOW)
subprocess.run('type nul > file3.txt', shell=True, creationflags=CREATE_NO_WINDOW)

time.sleep(1)

# Delete 3 silently using LOLBins
subprocess.run('rmdir /s /q folder1', shell=True, creationflags=CREATE_NO_WINDOW)
subprocess.run('del /f /q file1.txt', shell=True, creationflags=CREATE_NO_WINDOW)
subprocess.run('del /f /q file2.txt', shell=True, creationflags=CREATE_NO_WINDOW)
