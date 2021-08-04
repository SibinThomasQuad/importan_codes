from __future__ import print_function
from termcolor import colored
import os
from nude import Nude
f = open("label.txt", "r")
print(f.read())
def crowl_folder():
    #line
    rootdir = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir(rootdir):
        #line
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            #line
            #print(d)
            detect(d)
def detect(path):
    #line
    IMAGE_ROOT = ROOT = '/'+str(path)
    for file_name in os.listdir(IMAGE_ROOT):
        #line
        file_path = os.path.join(IMAGE_ROOT, file_name)
        if os.path.isdir(file_path):
            #line
            continue
        n = Nude(file_path)
        n.parse()
        results=n.result
        message=n.message
        if results == True:
            #line
            print('\033[91m'+"[+] Image:"+str(path)+str(file_name));
            print("[+] Result:"+str(results))
            print("[+] Message:"+str(message))
        else:
            #line
            print('\033[92m'+"[+] Image:"+str(path)+str(file_name));
            print("[+] Result:"+str(results))
            print("[+] Message:"+str(message))
crowl_folder()
