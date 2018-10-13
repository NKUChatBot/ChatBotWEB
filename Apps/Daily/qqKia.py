#coding:utf-8


import Kia
from qqbot import _bot as bot
bot.Login(['-q','2352341722'])
s=bot.List('buddy')
print(s[0])
s=bot.List('group','小开测试群')[0]
print(s,type(s),s.qq,s.name,s.uin,s.mark)
