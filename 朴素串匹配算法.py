''' 对模式串实现由第一个字母开始匹配，直到全部匹配完成'''
def naive_matching(t, p):
	m, n = len(p), len(t)
	i, j = 0, 0
	while i < m and j < n:
		if p[i] == t[j]:
			i, j = i + 1, j + 1
		else:
			i, j = 0, j - i + 1
	if i == m:
		return j - i
	return -1
