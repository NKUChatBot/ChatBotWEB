#coding:utf-8

import os
import sys

showQS=True
showLog=False

usrQ="你好啊"
mcd=os.popen("cd C:\\Users\\tropping\\Desktop\\国创\\QA_DailyQ\\py3Aiml_Chinese",'r',100).read()
print(mcd)	
print(os.getcwd())	
res=os.popen("python3 C:\\Users\\tropping\\Desktop\\国创\\QA_DailyQ\\py3Aiml_Chinese\\Kia.py -c "+usrQ+" -s 3",'r',1000)
lines=res.readlines()
for line in lines:
	if "q=" in line:
		q=line
	if "sid=" in line:
		sid=line
	if "ans=" in line:
		ans=line.replace("ans=",'')

print(q+sid+ans)