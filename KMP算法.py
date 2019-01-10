'''构建前缀与后缀相同的pnext表，避免回溯事件，大大提高了串匹配效率'''
#KMP算法
"""def gen_pnext(p):
    #生成p中的前缀与后缀的相同数i，用于KMP算法
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1,k+1
            pnext[i] = k #设置pnext元素
        else:
            k = pnext[k]
    return pnext"""
#pnext构建算法改进
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m 
    while i < m-1:#生成下一个pnext元素
        if k == -1 or p[i] == p[k]:
            i, k = i+1,k+1
            if p[i] == p[k]:
                pnext[i] == pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext
#KPM算法的实现
def matching_KMP(t, p, pnext):
    """KMP串匹配，主函数。""" 
    j, i = 0, 0
    n, m =len(t),len(p)
    while j < n and i < m:# i==m说明找到匹配
        if i == -1 or t[j] == p[i]:   #考虑p中下一字符
            j, i = j+1, i+1
        else:# 失败！考虑pnext决定的下一字符
            i = pnext[i]
    if i == m:# 找到匹配，返回下标
        return j-i
    return -1# 无匹配，返回特殊值
p = "abbcabcaabbcaa"
print(p)
t = "abcaa"
print(t)
pnext=gen_pnext(p)
print(pnext)
a=matching_KMP(p, t, pnext)
print(a)
