# coding:utf-8
from Apps.Daily.Kernel import *
import os
import sys
import getopt

this_path = os.path.dirname(os.path.realpath(__file__))

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def DailyWeb(question, msid):
    path = this_path + "/temp"
    isDebug = True

    print('q=' + question)
    print('sid=' + msid)

    # ——————————————学习初始化————————_

    Kia = Kernel()
    Kia.learn(path + "/Kia.aiml")
    Kia.learn(path + "/nk.aiml")
    Kia.learn(path + "/learnNewU.aiml")
    os.chdir(path)

    if isDebug:
        print(os.getcwd())
        print(os.listdir())
    # QandSID=input('问小开>>').split(' ')
    # question=QandSID[0]
    # sid=QandSID[1]

    # ——————添加本次对话————————
    caches = os.listdir()
    cache = open(msid + '.txt', 'a+', encoding='utf-8')
    cache.write(question + '\n')
    cache.close()

    # ----------复原对话----------
    print(msid)
    cache = open(msid + '.txt', 'r', encoding='utf-8')
    lines = cache.readlines()

    for line in lines:
        respond = Kia.respond(line.strip())  # 最后一次respond即为答案
        if isDebug:
            print('usr:' + line.strip())
            print('Kia:' + respond)

    print('ans=' + respond.strip())
    return (respond.strip())


if __name__ == "__main__":
    DailyWeb("你好", "21")
