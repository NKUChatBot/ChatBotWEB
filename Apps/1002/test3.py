#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 21:09:31 2018

@author: MacBook
"""


import re


f=open("NewContact.txt","r")
f1=open("contact.aiml","w")
f1.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+"\n")
f1.write("<aiml version=\"1.0\">"+"\n")
f1.write("<meta name=\"language\" content=\"zh\"/>"+"\n")
for line in f:
    #郁闷了好久，mac存储为txt的编码格式是gbk    
   #line=line.decode("gbk")
    str=line.split()
    length=len(str)
    s=""
    for i in range(length-1):
        if i==0:
            print(str[0]+"+"+str[1])
            f1.write("<category>"+"\n")
            f1.write("<pattern>"+str[0]+"+"+str[1]+"</pattern>"+"\n")
        else:
            s+=str[i+1]+" "
            
    print(s)
    f1.write("<template>"+s+"</template>"+"\n")
    f1.write("</category>"+"\n")
    
f1.write("</aiml>")
    
#这是什么傻逼逻辑 唉也只有我能这么写    
        
# =============================================================================
#         if re.search(r"/?",line):
#             str=re.findall(r"、(.*)/?",line)
#             print(str)
# =============================================================================

# =============================================================================
#        line=line.split(" ")
#        print("<category>")
#        f1.write("<category>"+"\n")
#        print("<pattern>"+line[1]+"</pattern>")
#        f1.write("<pattern>"+line[1]+"</pattern>"+"\n")
#        print("<template>"+line[0]+"</template>"+"\n"+"</category>"+"\n")
#        f1.write("<template>"+line[0]+"</template>"+"\n"+"</category>"+"\n")
# =============================================================================
       
f1.close()
f.close()

