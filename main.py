# 检索当前目录下的MDK工程，选择要编译的。

import os
from terminal_layout.extensions.choice import *
from terminal_layout import *
from intelhex import IntelHex
from struct import *
import xml.etree.ElementTree as ET
import subprocess


def get_filename_include_keyword(dir, keyword1, keyword2):
    filename = list()
    for file in os.listdir(dir):
        if keyword1 in file and keyword2 in file:
            filename.append(file)
    return filename


def search_in_xml(path, para):
    tree = ET.parse(path)
    root = tree.getroot()
    target_name = list()

    for i in root[2].findall(para):
        target_name.append(i[0].text)
    return target_name


Pycharm_Debug = False

if __name__ == '__main__':
    if Pycharm_Debug is False:
        filelist = get_filename_include_keyword(".", ".", "uvprojx")
        if filelist.__len__() > 1:
            software_chioce = Choice('检索到以下文件，请选择：', filelist,
               icon_style=StringStyle(fore=Fore.yellow),
               selected_style=StringStyle(fore=Fore.yellow), default_index=0, icon="» ")
            index, prj_file_name = software_chioce.get_choice()
        else:
            prj_file_name = filelist[0]
    else:
        prj_file_name = "Project.uvprojx"
    print("选择：%s" % prj_file_name)

    find_result = search_in_xml(prj_file_name, "Target")
    if Pycharm_Debug is False:
        if find_result.__len__() > 1:
            prj_chioce = Choice('检索到以下文件，请选择：', find_result,
                                     icon_style=StringStyle(fore=Fore.yellow),
                                     selected_style=StringStyle(fore=Fore.yellow), default_index=0, icon="» ")
            index, prj_name = prj_chioce.get_choice()
        else:
            prj_name = find_result[0]
    else:
        prj_name = find_result[0]
    print("工程选择：%s" % prj_name)

    cmd = "UV4.exe -j0 -b %s -t %s -o .\\build_log.txt" % (prj_file_name, prj_name)
    if Pycharm_Debug is False:
        pid = subprocess.Popen(cmd, shell=True)
        return_code = pid.wait()

        with open("build_log.txt", "r") as file:
            for i in file.readlines():
                print(i, end="")
    else:
        print(cmd)
