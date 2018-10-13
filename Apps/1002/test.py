#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 19:48:32 2018

@author: MacBook
"""



f=open("url.txt","r")
f1=open("url0.aiml","w")
count=1
for line in f:
    #郁闷了好久，mac存储为txt的编码格式是gbk    
   line=line.decode("gbk")
   line=line.split(" ")
   print("<category>")
   f1.write("<category>"+"\n")
   print("<pattern>"+line[1]+"</pattern>")
   f1.write("<pattern>"+line[1]+"</pattern>"+"\n")
   print("<template>"+line[0]+"</template>"+"\n"+"</category>"+"\n")
   f1.write("<template>"+line[0]+"</template>"+"\n"+"</category>"+"\n")

       
f1.close()
f.close()

