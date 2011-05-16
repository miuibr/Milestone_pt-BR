from subprocess import call
from os import popen

apk_list = popen("ls").read().split()
apk_list.remove("copiar_apks.py")

recompiled_apks = [apk + ".apk" for apk in apk_list]

def create_build_dir():
    call("rm -rf build", shell=True)
    call("mkdir build", shell=True)

def recompile_all_apks():
    for (apk, recompiled_apk) in zip(apk_list, recompiled_apks):
        call("apktool b %s build/%s" % (apk, recompiled_apk), shell=True)

if __name__ == '__main__':
    create_build_dir()
    recompile_all_apks()
