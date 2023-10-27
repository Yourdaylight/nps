# -*- coding: utf-8 -*-
# @Time    :2023/10/27 16:53
# @Author  :lzh
# @File    : client_start.py.py
# @Software: PyCharm
"""
Client installer
Execute to generate exe:pyinstaller --onefile --add-data "./npc.exe;." start.py
Before execute this script, you should pack npc.exe into this directory
"""
# -*- coding: utf-8 -*-
# @Time    :2023/10/27 14:08
# @Author  :lzh
# @File    : start.py
# @Software: PyCharm
import os
import shutil
import platform
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('error_log.txt', 'w', 'utf-8')])

HOST = "1.1.1.1"
PORT = 8888
KEY = ""
ROOT_PATH = "./npc"
WEB_PORT = 8080

# 检查c盘根目录下是否存在npc文件夹，如果不存在则创建
if not os.path.exists(ROOT_PATH):
    os.mkdir(ROOT_PATH)


def move_to_npc(arch="amd"):
    # 检查是否存在npc.exe，不存在则将项目目录的npc.exe复制到npc文件夹下
    if not os.path.exists(f"{ROOT_PATH}/npc.exe"):
        src_path = os.path.join(os.path.dirname(__file__), arch, "npc.exe")
        src_path = os.path.abspath(src_path)
        logging.info(f"src_path: {src_path}")
        shutil.copy(src_path, ROOT_PATH)
        logging.info(f"Copied {arch}/npc.exe to {ROOT_PATH}")


if __name__ == '__main__':
    try:
        # 检查当前环境是x86还是arm
        logging.info(f"Current platform is {platform.machine()}")
        KEY = input("请输入密码(vkey)：")
        # 获取可执行文件所在的目录
        exe_dir = os.path.dirname(os.path.abspath(__file__))
        # 构造npc.exe的绝对路径
        npc_exe_path = os.path.join(exe_dir, 'npc.exe')
        # 构造命令
        register_cmd = f"{npc_exe_path} install -server={HOST}:{PORT} -vkey={KEY} -type=tcp"
        start_cmd = f"{npc_exe_path} start"

        # 运行命令
        subprocess.run(register_cmd, check=True, shell=True)
        subprocess.run(start_cmd, check=True, shell=True)
        msg = f"链接成功!现在你可以前往http://{HOST}:{WEB_PORT} 登录配置内网穿透，用户名和密码均为你的vkey"
        os.system('pause')

    except Exception as e:
        logging.error(e, exc_info=True)  # 记录错误日志
        print(e)
        os.system('pause')

