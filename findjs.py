#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
import fnmatch

listonly = False
filetype = ['.js']


def visitfile(fname,searchkey):
    global fcount,vcount,list_of_contain_lines
    try:
        if not listonly:
            if os.path.splitext(fname)[1] in filetype:
                raw = open(fname).read()
                if open(fname).read().find(searchkey) != -1:
                    print '%s has %s '%(fname,searchkey)
                    fcount+=1
                if raw.find(searchkey) != -1:
                    lines = raw.split('\n')
                    for line in lines:
                        if searchkey in line:
                            list_of_contain_lines.append(line)
                            # print line
                            # if list_AA in list_of_contain_lines:
                            #     list_result=''

    except: pass
    vcount +=1

def visitor(args,directoryName,filesInDirectory):
    for fname in filesInDirectory:
        # 返回文件所在路径和文件名
        fpath = os.path.join(directoryName,fname)
        if not os.path.isdir(fpath):

            visitfile(fpath,args)

def searcher(startdir,searchkey):
    global fcount,vcount,list_of_contain_lines
    fcount = vcount = 0
    list_of_contain_lines = []
    os.path.walk(startdir,visitor,searchkey)

if __name__=='__main__':
    # root=raw_input("type root directory:")
    root = '/home/jiangbin/findJS'
    key=raw_input("type key:")
    searcher(root,key)
    print 'Found in %d files,visited %d'%(fcount,vcount)
    fd = open("result.txt", "w")
    # str_names = str.__name__()
    # str_names = "abcdefghijklmnopqrst"
    for i in range(len(list_of_contain_lines)):
        one = list_of_contain_lines[i]
        fd.write( str(i)+ ":" + one   + "\n")
    fd.close()

