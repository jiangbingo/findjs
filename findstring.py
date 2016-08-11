#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
import re , collections
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
                print 'seaching in :%s' % fname
                if open(fname).read().find(searchkey) != -1:
                    print '%s has %s '%(fname,searchkey)
                    fcount += 1
                if raw.find(searchkey) != -1:
                    # import ipdb; ipdb.set_trace()
                    lines = raw.split('\n')
                    count = 0
                    for line in lines:
                        count += 1
                        if count % 1000 == 0:
                            print "filename:%s total:%s current_line_no: %s" %(fname,len(lines),count)
                        if line.find(searchkey) > -1:
                            vars = re.findall(r"([\d\w]*" + searchkey +"[\d\w]*)", line)
                            for var in vars:
                                list_of_contain_lines.append(var)
                            # print list_of_contain_lines

                    # for line in lines:
                    #     chars = line.split(' ') or line.split('.')
                    #     for char in chars:
                    #         if char =='':
                    #             pass
                    #         elif char.find(searchkey) != -1 and isJSVar(char):
                    #                 list_of_contain_lines.append(char)
                    #                 print lines, line, list_of_contain_lines

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

    # 除了下划线其他非字母字符分割的包含查询字符的字符串均为变量

    '''
    :param s:
        48  57  65 90 95 97 122   46
        0    9  A  Z  _  a   z    .
    :return:
    '''
    str0_to_int = ord(string[0])
    if (str0_to_int>=97 and  str0_to_int<=122 ) or (str0_to_int>=65 and  str0_to_int<=90 ) or str0_to_int==95 or str0_to_int==46:
        i = 1
        while i<len(string):
            str_to_int= ord(string[i])
            if (str_to_int>=97 and str_to_int<=122 ) or (str_to_int>=65 and  str_to_int<=90 ) or (str_to_int==95) or (str_to_int==46) or (str_to_int>=48 and str_to_int<=57 ):
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
    root = 'E:/findjs'
    # key=raw_input("type the search key:")
    key = 'JSQ'
    # title = raw_input("type your name(default:none):")

    searcher(root,key)
    print 'Found in %d files,visited %d'%(fcount,vcount)
    oldkeys = []
    oldlabels = []
    olddict = dict()

    newkeys = []
    delkeys = []
    addkeys = []
    addlabels = []

    cachelabels = []
    # with open("cache.txt") as f:
    #     for line in f.readlines():
    #         cachelabels = line.strip()

    if os.path.isfile('cache.txt'):
        fcache = open("cache.txt",'r')
        for line in fcache.readlines():
            cachelabels = line.strip()
    else:
        fcache = open("cache.txt",'w+')
        fcache.close()




    if os.path.isfile('result.txt'):
        fresult = open('result.txt','r')
        for line in fresult.readlines():
            line = line.strip()
            oldkey, oldlabel = line.split(":")
            # if line.find("###") != -1:
            #     title,content = line.split("###")
            #     oldkey,oldlabel = content.split(":")
            # else:
            #     title = '   '
            #     oldkey, oldlabel = line.split(":")
            oldkeys.append(oldkey)
            oldlabels.append(oldlabel)
    else:
        fresult = open("result.txt", 'w+')
        fresult.close()

    _dict =  dict(zip(oldkeys,oldlabels))

    olddict = collections.OrderedDict()
    for key in oldkeys:
        olddict[key] = _dict[key]


    for i in list_of_contain_lines:
        if not  i in newkeys:
            newkeys.append(i)

    for j in newkeys:
        if not j in oldkeys:
            addkeys.append(j)

    # for k in oldkeys:
    #     if not  k in newkeys:
    #         delkeys.append(k)

    labelstring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(newkeys)
    templabels = label_array(n,labelstring)

    labels = []
    for label in templabels:
        labels.append(label+'_'+label)

    for k in labels:
        if not k in olddict.values():
            addlabels.append(k)



    t = 0
    newdict = collections.OrderedDict()

    for key in  newkeys:
        if key in olddict.keys():
            newdict[key] = olddict[key]
        else:
            newdict[key] = addlabels[t]
            t = t + 1

    f = open('result.txt','w+')
    for key in newdict.keys():
        f.write(key + ':' + newdict[key] +  "\n")
    f.close()

    # fd = open('cache.txt', 'a')
    # for label in newdict.values():
    #     fd.write(label + '\n')
    # fd.close()
