import heap
import time

f=open('graph_7.txt','r')
graph=[]
Z={}
next(f)
for line in f:
    line =line.replace("\n","")
    graph.append(list(map(int,line.split(' '))))
f.close()
for item in graph:                      #从测试文本中读入每条边的信息，用字典存储
    if item[0] not in Z:
        Z[item[0]]={}
        Z[item[0]][item[1]] = item[2]
    else:
        Z[item[0]][item[1]]=item[2]
    if item[1] not in Z:
        Z[item[1]]={}
        Z[item[1]][item[0]] = item[2]
    else:
        Z[item[1]][item[0]]=item[2]
#print(Z)

V=set()
X=set()
s=input("please input start_node:")
s=int(s)
X.add(s)
T=[]
d={}
p={}
A=[]
sum=0
start=time.perf_counter()
for i in Z:
    V.add(i)
for i in V:                  #初始化每个点的d和p
    d[i]=10000
    p[i]=0
d[s]=0
for t in Z[s]:              #先遍历起始点s点的附近节点，记录各个节点的d和p，并将每个点对应的最小边插入堆中
    if Z[s][t]<d[t]:
        d[t]=Z[s][t]
        p[t]=s
        flag=[p[t],t,d[t]]
        heap.heap_insert(A,flag)
while (V-X):
    m=heap.extract_min(A)     #堆中取最小的边
    while m[0] in X and m[1] in X:    #如果最小边的两个点已经在X中，重新取最小边
        m=heap.extract_min(A)
    T.append(m)               #将最小边加入集合T中
    if m[0] not in X:         #加入最小边的两个点中，不在X中的点t
        i=m[0]
        X.add(m[0])
    else:
        i=m[1]
        X.add(m[1])
    sum=sum+m[2]
    for t in Z[i]:            #遍历t点的附近节点，记录各个节点的d和p，并将每个点对应的最小边插入堆中
        if Z[i][t]<d[t]:
            d[t]=Z[i][t]
            p[t]=i
            flag=[p[t],t,d[t]]
            heap.heap_insert(A,flag)
print(T)
print(sum)
print(time.perf_counter()-start)

