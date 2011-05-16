from subprocess import call
from os import popen

apk_list = popen("ls").read().split()
apk_list.remove("copiar_apks.py")
original_apk_list = [apk + "_original" for apk in apk_list]

files_to_remove = []

def pull_apks_from_adb():
    for apk in apk_list:
        new_apk = "%s_original.apk" % apk
        call("adb pull /system/app/%s.apk %s" % (apk, new_apk), shell=True)
        files_to_remove.append(new_apk)

def extract_apks():
    for apk in original_apk_list:
        new_apk_folder = apk
        call("apktool d %s.apk %s" % (apk, apk), shell=True)
        files_to_remove.append(new_apk_folder)

def merge_apks():
    for (apk, apk_original) in zip(apk_list, original_apk_list):
        call("cp -Rfv %s/* %s" % (apk_original, apk), shell=True)

def clean_the_mess():
    for temp_file in files_to_remove:
        call("rm -rf %s" % temp_file, shell=True)

if __name__ == '__main__':
    clean_the_mess()
    pull_apks_from_adb()
    extract_apks()
    merge_apks()
    clean_the_mess()
