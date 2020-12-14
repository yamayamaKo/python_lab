import matplotlib.pyplot as plt 

path = 'C:\研究室\みんなのアイデア'
file_name = '\西村冷蔵庫1212.txt'
file_name2 = '\西村洗濯機1212.txt' 

with open(path+file_name, encoding='utf_8') as f:
    ideatimes = []
    ideamergins = []
    for s in f:
        line = list(s.strip().split())
        if len(line) <= 1:
            continue
        ideatimes.append(int(line[2]))
        ideamergins.append(int(line[3]))
    plt.plot(ideatimes,ideamergins)

with open(path+file_name2,encoding='utf_8') as f:
    ideatimes = []
    ideamergins = []
    for s in f:
        line = list(s.strip().split())
        if len(line) <= 1:
            continue
        ideatimes.append(int(line[2]))
        ideamergins.append(int(line[3]))
    plt.plot(ideatimes,ideamergins)

'''
データを可視化してみて
特に何も発見がない。
何も分からねえ。もう普通に数だけで見ればよかったのではないか。
'''
plt.show()