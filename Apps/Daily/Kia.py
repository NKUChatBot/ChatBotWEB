#coding:utf-8
import Kernel
import os
import sys
import getopt



this_path=os.path.dirname(os.path.realpath(__file__))


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

def Daily(argv):
	#path="C:\\Temp\\tmp_qqbot"	#存放临时文件和aiml文件的路径
	path=this_path+"\\temp"
	isDebug=True
	question='null'
	msid='null'
	try:
		opts,args=getopt.getopt(argv,"hc:s:",["content=","sid="])
	except getopt.GetoptError:
		print('Error: Kia.py -c <content> -s <sid>')
		print('   or: Kia.py --content=<content> --sid=<sid>')
		sys.exit(2)
	for opt,arg in opts:
		if opt=="-h":
			print('usage:Kia.py -c <content> -s <sid>')
			print('   or: Kia.py --content=<content> --sid=<sid>')
			sys.exit()
		elif opt in ("-s","--sid"):
			msid=arg

		elif opt in ("-c","--content"):
			question=arg
	print('q='+question)
	print('sid='+msid)



	if (question=='null' or msid=='null'):
		print('Error: Kia.py -c <content> -s <sid>')
		print('   or: Kia.py --content=<content> --sid=<sid>')
		sys.exit(2)
#——————————————学习初始化————————_
	
	Kia=Kernel.Kernel()
	Kia.learn(path+"\\Kia.aiml")
	Kia.learn(path+"\\nk.aiml") 
	Kia.learn(path+"\\learnNewU.aiml")   
	os.chdir(path)

	if isDebug :
		print(os.getcwd())
		print(os.listdir())
	#QandSID=input('问小开>>').split(' ')
	#question=QandSID[0]
	#sid=QandSID[1]
    
#——————添加本次对话————————
	caches=os.listdir()
	cache=open(msid+'.txt','a+')
	cache.write(question+'\n')
	cache.close()
    
#----------复原对话----------
	cache=open(msid+'.txt','r')
	lines=cache.readlines()

	for line in lines:	
		respond=Kia.respond(line.strip())	#最后一次respond即为答案
		if isDebug:
			print('usr:'+line.strip())
			print('Kia:'+respond)

		


	print('ans='+respond.strip())
	return(respond.strip())
    
if __name__=="__main__":
	Daily(sys.argv[1:])