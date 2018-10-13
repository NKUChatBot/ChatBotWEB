#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:50:01 2018

@author: MacBook
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:09:31 2018

@author: MacBook
"""


import re

f=open("NewContact.txt","r")
#f1=open("temp.txt","w")
#f1.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+"\n")
#f1.write("<aiml version=\"1.0\">"+"\n")
#f1.write("<meta name=\"language\" content=\"zh\"/>"+"\n")
temp=""
s=""
i=1
for line in f:
    #郁闷了好久，mac存储为txt的编码格式是gbk    
   #line=line.decode("gbk")
    str=line.split()
    length=len(str)
    if temp!= str[0]:
        print(str[0])
        #if i!=1:
 #           f1.write("<template>你想知道的部门是哪一个："+s+"</template>"+"\n")
 #           f1.write("</category>"+"\n")
        #print("你想知道的部门是哪一个："+s)
        
        
 #       f1.write("<category>"+"\n")
  #      f1.write("<pattern>"+str[0]+"</pattern>"+"\n")
        #print("\n"+str[0]+"\n")
        temp=str[0]
        #s=""
    #s+=str[1]+" " 
    #i+=1
    
#f1.write("<template>你想知道的部门是哪一个："+s+"</template>"+"\n")
#f1.write("</category>"+"\n")
#f1.write("</aiml>")
    
         
#f1.close()
f.close()

