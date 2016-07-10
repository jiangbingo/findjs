#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
import fnmatch

listonly = False
filetype = ['.js']
def visitfile(fname,searchkey):
   global fcount,vcount
   try:
      if not listonly:
         if os.path.splitext(fname)[1] in filetype:
            if open(fname).read().find(searchkey) != -1:
               print '%s has %s '%(fname,searchkey)
               fcount+=1
   except: pass
   vcount +=1

def visitor(args,directoryName,filesInDirectory):
   for fname in filesInDirectory:
      # 返回文件所在路径和文件名
      fpath = os.path.join(directoryName,fname)
      if not os.path.isdir(fpath):
         visitfile(fpath,args)

def searcher(startdir,searchkey):
   global fcount,vcount
   fcount = vcount = 0
   os.path.walk(startdir,visitor,searchkey)

if __name__=='__main__':
   # root=raw_input("type root directory:")
   root = '/home/jiangbin/findJS'
   string=raw_input("type string:")
   searcher(root,string)
   print 'Found in %d files,visited %d'%(fcount,vcount)



