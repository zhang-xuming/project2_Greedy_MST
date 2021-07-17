import union_find
import time

def take_third(elem):
    return elem[2]

f=open('graph_12.txt','r')
graph=[]
next(f)
for line in f:
    line =line.replace("\n","")
    graph.append(list(map(int,line.split(' ')))) #从测试文本中读入每条边的信息，用list存储
f.close()
graph.sort(key=take_third)              #将每条边按权重排序

start=time.perf_counter()
T=set()
Z={}
S={}
leader={}
num=1
sum=0
for i in range(len(graph)-1):
    if graph[i][0] not in Z:
        Z[graph[i][0]]=num              #用字典Z存储所有点，并初始化所有点的leader
        S[num]=set()                    #S为相同leader的点的集合
        S[num].add(graph[i][0])
        num=num+1
    if graph[i][1] not in Z:
        Z[graph[i][1]]=num
        S[num]=set()                    #操作同上
        S[num].add(graph[i][1])
        num=num+1
while(graph):
    flag=graph.pop(0)
    if (union_find.find(flag,S,leader)):       #若不成环
        union_find.union(flag,S,leader)        #更新leader
        T.add(str(flag))                #记录最小生成树
        sum=sum+flag[2]
print(T)
print(sum)
print(time.perf_counter()-start)

