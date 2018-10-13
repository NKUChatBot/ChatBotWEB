# _*_ coding:utf-8 _*_

import os
import sys
from Apps.Daily.Kiaweb import DailyWeb
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


def DailyQ(usrQ,sid):
	path=curPath	#存放Kia.py文件夹的路径
	aimlPath=path+"\\temp"									#存放临时文件和aiml文件的路径

	#_______check if learning_______
	isLearn=False
	ckLearn=open(aimlPath+"\\learn.txt","r")
	lines=ckLearn.readlines()
	f_data=""
	for line in lines:
		if (line.find("#waiting")>-1):
			line="a="+usrQ+"\n"
			isLearn=True
		f_data+=line
	ckLearn.close()

	#________如果在学习，进行记录_______
	if (isLearn):
		ckLearn=open(aimlPath+"\\learn.txt","w")
		ckLearn.write(f_data)
		ckLearn.close()
		#________将记录文件转换为aiml________
		LearnLog=open(aimlPath+"\\learn.txt","r")
		LearnAiml=open(aimlPath+"\\learn.aiml","r")
		liensLog=LearnLog.readlines()
		linesAiml=LearnAiml.readlines()
		LearnLog.close()
		LearnAiml.close()
		aiml_data=""
		for lineAiml in linesAiml:
			if(lineAiml.find("/aiml")>-1):
				paired=False
				for lineLog in liensLog:
					if(lineLog.find("q=")>-1):								
						qtmp=lineLog.replace("q=",'').strip()
						paired=False
					elif(lineLog.find("a=")>-1):
						atmp=lineLog.replace("a=",'').strip()
						paired=True
					if(paired):
						aimltmp="<category><pattern>"+qtmp+"</pattern><template>"+atmp+"</template></category>\n"
						aiml_data+=aimltmp
			aiml_data+=lineAiml

		LearnAiml=open(aimlPath+"\\learnNew.aiml","w")
		LearnAiml.write(aiml_data)
		LearnAiml.close()


		#________转码________
		LearnAiml=open(aimlPath+"\\learnNew.aiml","r",encoding="gbk")
		lines=LearnAiml.read()
		LearnAiml.close()
		LearnAiml=open(aimlPath+"\\learnNewU.aiml","w",encoding="utf-8")
		lines=lines
		LearnAiml.write(lines)
		LearnAiml.close()

		KiaAns="我已经会啦，试试看吧"
		return(KiaAns)



		




	res=DailyWeb(usrQ,sid)


	ans=res.replace("ans=",'')
	if (ans.find("#learn")>-1):
		LearnLog=open(aimlPath+"\\learn.txt","a+")
		LearnLog.write("q="+usrQ+"\n")
		LearnLog.write("a=#waiting\n")
		LearnLog.close()
	KiaAns=ans.strip()
	return(KiaAns)
if __name__=="__main__":
	ans=DailyQ("乌拉拉","21")
	print(ans)