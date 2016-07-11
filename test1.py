#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
def find_file_text(root_dir,target_text):
 suffix=['js','txt','html']
 for root,dirs,files in os.walk(root_dir):
    for file in files:
        file_suffix=file[file.find('.')+1:len(file)]
        if file_suffix in suffix:
            file_obj=open(os.path.join(root, file),'rU')
            line_no=0
            for eachline in file_obj:
                line_no=line_no+1
                if eachline.find(target_text)!=-1:
                    print "%s %d:%s"%(os.path.join(root, file),line_no,eachline)

if __name__ == '__main__':
    root=raw_input("type root directory:")
    target='target.txt'

    find_file_text(root,target)