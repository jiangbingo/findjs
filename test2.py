#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import glob

def search(root, key, ftype='', logname=None):
    ftype = '*.'+ftype if ftype else '*'
    logname = logname or os.devnull
    symbol = os.path.join(root, ftype)
    fnames = glob.glob(symbol)
    vc = len(fnames)
    fc = 0

    with open(logname, 'w') as writer:
        for fname in fnames:
            found = False
            with open(fname) as reader:
                for idx, line in enumerate(reader):
                    line = line.strip()
                    if key in line.split():
                        line = line.replace(key, '**'+key+'**')
                        found = True
                        print('{} -- {}: {}'.format(fname, idx, line), file=writer)
            if found:
                fc = fc + 1
                print('{} has {}'.format(fname, key))

    return vc, fc


    if __name__=='__main__':
        root = 'mydir'
        key = input("type key: ")
        vc, fc = search(root, key, 'js', logname='results')
        print('Found in {} files, visited {}'.format(fc, vc))