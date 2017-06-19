"""Script Downloading Powerline fonts and move them decently"""
import os
import shutil
import urllib.request


def save_download(url, filename):
    """File Download to current dir"""
    response = urllib.request.urlopen(url)
    out_file = open(filename, "wb")
    shutil.copyfileobj(response, out_file)


def mv_otf(filename):
    """Move otf file to specific dir"""
    if os.path.exists("/usr/share/fonts/X11/misc/"):
        os.rename("./" + filename, "/usr/share/fonts/X11/misc/" + filename)
        if os.path.exists("/usr/share/fonts/X11/misc/" + filename):
            print("File moved successfully")
            return "/usr/share/fonts/X11/misc/"
    exit("File was not moved! Path not found? (otf)")


def mv_conf(filename):
    """Move font conf to specific dir"""
    if os.path.exists("/etc/fonts/conf.d/"):
        os.rename("./" + filename, "/etc/fonts/conf.d/" + filename)
        if os.path.exists("/etc/fonts/conf.d/" + filename):
            print("File moved successfully")
            return
    # Delete upper moved file
    exit("File was not moved! Path not found? (conf)")


print(os.geteuid())
print(os.getcwd())
if os.geteuid() != 0:
    exit("Not root")

save_download(
    "https://github.com/powerline/powerline/"
    "raw/develop/font/PowerlineSymbols.otf",
    "PowerlineSymbols.otf")
save_download(
    "https://github.com/powerline/powerline/"
    "raw/develop/font/10-powerline-symbols.conf",
    "10-powerline-symbols.conf")
OTF_PATH = mv_otf("PowerlineSymbols.otf")
mv_conf("10-powerline-symbols.conf")
print("Run 'fc-cache -vf " + OTF_PATH
      + "' and restart the X-Window or restart")
