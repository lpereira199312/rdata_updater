import time
from tkinter.filedialog import askdirectory
import os
from git.repo.base import Repo
import shutil
from bar import CloneProgress

print("select rdata directory folder")
path = askdirectory(title="rdata folder",initialdir=r'/',mustexist=True)
check_dir = os.path.exists(path+"/rdata-server")
print("try locate rdata")
if check_dir == True:
    dir = "/tmp/rdatatmp/"
    if(os.path.isdir(dir)==True):
        os.popen("sudo rm -R /tmp/rdatatmp/")
        time.sleep(3)
    print("start clone git rdata")
    print("not close wait download finish")
    url_git = "https://github.com/reactioon/rdata.git"
    temp_download = Repo.clone_from(url_git,f"/tmp/rdatatmp",progress=CloneProgress())
    print("finished clone git rdata ")
    try:
        os.popen("sudo systemctl stop rdata")
        print("rdata service terminated successfully...")
        time.sleep(5)
        for file_name in os.listdir(f"/tmp/rdatatmp/builds/linux"):
            print(f"{file_name} updated")
            shutil.move(f"/tmp/rdatatmp/builds/linux/{file_name}", f"{path}/{file_name}")
        print("wait delete tmp files")
        os.popen("sudo rm -R /tmp/rdatatmp/")
        print("tmp files deleted")
        print("update finished")
        try:
            print("try start rdata service")
            os.popen("sudo systemctl start rdata")
            print("rdata service started successfully...")
        except OSError as ose:
            print("Error while running the command. try start rdata manually")
    except OSError as ose:
        print("Error while running the command. try stop rdata manually")
        input = input("do you like continue? y/n")
        if (input == "y" or "Y"):
            for file_name in os.listdir(f"/tmp/rdatatmp/builds/linux"):
                print(f"{file_name} updated")
                shutil.move(f"tmp/rdatatmp/builds/linux/{file_name}",f"{path}/{file_name}")
            print("wait delete tmp files")
            os.popen("sudo rm -R /tmp/rdatatmp/")
            print("tmp files deleted")
            print("update finished")
            try:
                print("try restart rdata service")
                os.popen("sudo systemctl start rdata")
                print("rdata service started successfully...")
            except OSError as ose:
                print("Error while running the command. try start rdata manually")
        else:
            print("rdata update stoped")
else:
    print("rdata not found please check directory")