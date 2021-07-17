def union(flag,S,leader):
    if len(S[leader[0]])<len(S[leader[1]]):         #比较两个leader集合的大小，将集合小的leader改为集合大的leader，并删除小集合
        S[leader[1]]=S[leader[1]].union(S[leader[0]])
        del S[leader[0]]
    else:
        S[leader[0]]=S[leader[0]].union(S[leader[1]])
        del S[leader[1]]


def find(flag,S,leader):
    k=j=-1
    for i in S:             #S中查找两个点的leader
        if flag[0] in S[i]:
            j=i
        if flag[1] in S[i]:
            k=i
        if(k>0 and j>0):
            break
    if k==j:              #leader一样，即成环，返回0
        return 0
    else:                 #leader不同，不成环，记录leader,返回1
        leader[0]=j
        leader[1]=k
        return 1


