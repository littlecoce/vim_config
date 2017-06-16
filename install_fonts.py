import os
import shutil
import urllib.request

new_otf_path = ""

def save_download(url, filename):
    response = urllib.request.urlopen(url)
    out_file = open(filename, "wb")
    shutil.copyfileobj(response, out_file)

def mv_otf(filename):
    if os.path.exists("/usr/share/fonts/X11/misc/"):
        os.rename("./" + filename, "/usr/share/fonts/X11/misc/" + filename)
        if os.path.exists("/usr/share/fonts/X11/misc/" + filename):
            print("File moved successfully")
            global new_otf_path
            new_otf_path = "/usr/share/fonts/X11/misc/"
            return
    print("File was not moved! Path not found? (otf)")

def mv_conf(filename):
    if os.path.exists("/etc/fonts/conf.d/"):
        os.rename("./" + filename, "/etc/fonts/conf.d/" + filename)
        if os.path.exists("/etc/fonts/conf.d/" + filename):
            print("File moved successfully")
            return
    print("File was not moved! Path not found? (conf)")
print(os.geteuid())
print(os.getcwd())
if os.geteuid() != 0:
    exit("Not root")

save_download("https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf","PowerlineSymbols.otf")
save_download("https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf","10-powerline-symbols.conf")
mv_otf("PowerlineSymbols.otf")
mv_conf("10-powerline-symbols.conf")
print("Run 'fc-cache -vf " + new_otf_path + "' and restart the X-Window or relog/restart")
