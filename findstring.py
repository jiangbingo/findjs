#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
from itertools import product

listonly = False

# 结果放入.txt文件，故禁用.txt
filetype = ['.js']

def visitfile(fname,searchkey):
    global fcount,vcount,list_of_contain_lines
    try:
        if not listonly:
            if os.path.splitext(fname)[1] in filetype:
                raw = open(fname).read()
                if open(fname).read().find(searchkey) != -1:
                    print '%s has %s '%(fname,searchkey)
                    fcount += 1
                if raw.find(searchkey) != -1:
                    # import ipdb; ipdb.set_trace()
                    lines = raw.split('\n')
                    for line in lines:
                        chars = line.split(' ')
                        for char in chars:
                            if char =='':
                                pass
                            elif char.find(searchkey) != -1 and isJSVar(char):
                                    list_of_contain_lines.append(char)
                                    print lines, line, list_of_contain_lines

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

def isJSVar(string):
    # 判断一个.js文件里的字符串是否是合法的变量
    '''
    :param s:
        48  57  65 90 95 97 122
        0    9  A  Z  _  a   z
    :return:
    '''
    str0_to_int = ord(string[0])
    if (str0_to_int>=97 and  str0_to_int<=122 ) or (str0_to_int>=65 and  str0_to_int<=90 ) or str0_to_int==95:
        i = 1
        while i<len(string):
            str_to_int= ord(string[i])
            if (str_to_int>=97 and str_to_int<=122 ) or (str_to_int>=65 and  str_to_int<=90 ) or (str_to_int==95) or (str_to_int>=48 and str_to_int<=57 ):
                i += 1
            else:
                return False
        return True
    else:
        return False

def label_array(n, labelstring):
    results = []
    for l in range(1, len(labelstring)+1):
        results.extend([''.join(p) for p in product(labelstring, repeat=l)])
        if len(results) >= n:
            return results[:n]
    return None



if __name__=='__main__':
    # root=raw_input("type root directory:")
    root = '/home/jiangbin/findJS'
    key=raw_input("type key:")
    searcher(root,key)
    print 'Found in %d files,visited %d'%(fcount,vcount)
    fd = open("result.txt", "w")

    labelstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(list_of_contain_lines)
    labels = label_array(n,labelstring)

    for i in range(n):
        one = list_of_contain_lines[i]
        label = labels[i]
        fd.write(one+ ":" + label+'_'+label + "\n")
    fd.close()