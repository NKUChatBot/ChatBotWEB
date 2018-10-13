#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:47:45 2018

@author: MacBook
"""

import re


f=open("zhaosheng.txt","r")
f1=open("zhaosheng.aiml","w")
count=1
for line in f:
    #郁闷了好久，mac存储为txt的编码格式是gbk    
   #line=line.decode("gbk")
   #line=re.match(r'(.*)/?',line)
        if re.search(u"一、|二、|三、|四、|五、|六、|七、|八、|九、|十、",line) and not re.search(r"软件工程",line):
            
            f1.write("</template>"+"\n"+"</category>"+"\n")
            f1.write("<category>"+"\n")
            f1.write("<pattern>"+line+"</pattern>"+"\n")
            f1.write("<template>")

        else:
            f1.write(line)
        
f1.write("</template>")
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

