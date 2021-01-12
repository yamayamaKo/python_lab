import matplotlib.pyplot as plt 
import glob 
import os

# files = glob.glob('C:\研究室\みんなのアイデア\予備実験結果\*')

path = 'C:\研究室\みんなのアイデア\内藤洗濯機1203.txt'
words = []

with open(path, encoding='utf_8') as file:
    index = 0
    for s in file:
        line = str(index)+' '+s
        words.append(line)
        index += 1
        print(s)
        # line = list(s.strip().split())
        # if len(line) == 1:
        #     continue
        # line.insert(0,str(index))
        # line.append('\n')
        # words.append(line)
        # index += 1
# print(words)
with open(path,'a',encoding='utf_8') as file:
    for i in range(len(words)):
        if i == 0:
            continue
        file.write(words[i])

