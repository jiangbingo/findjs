#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import fnmatch

# 获取
def find_target_files(path, filetype):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, filetype):
            yield os.path.join(root, filename)


if __name__ == '__main__':
    root=raw_input("type your root directory:")
    type=raw_input("type your file type(*.js *.html ...):")
    # type = '*.js'

    for filename in find_target_files(root, type):
        print filename