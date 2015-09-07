#coding:utf-8
#功能：分词+排除停止词，并导出到指定文件

import jieba,sys

inputfile = sys.argv[1]
stopword = [x.strip() for x in open('stop.txt')]

for x in open(inputfile):
    x = x.strip()
    word = jieba.cut(x)
    keyword = ''
    for x in word:
        x = x.encode('utf-8')
        if x not in stopword:
            keyword += x+' '
    print keyword  
fenci_file.close()
