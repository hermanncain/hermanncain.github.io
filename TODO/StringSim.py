# -*- coding: UTF-8 -*-
import copy
import math
'''
Typical string similarity measurement
@author hermanncain
'''

'''
Calculate the LCS of 2 strings
the same length with x,y: same
smaller: less similar

@class LCS
@constructor
@params {string/list} x,y
'''
class LCS:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.r = []
        self.d = 0
        self.get_length()
        self.islist = isinstance(x,list)

    # get length of lcs
    # @params self
    # @return void
    def get_length(self):
        m = len(self.x)
        n = len(self.y)
        if m==0 or n==0:
            return
        # build c
        self.c = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if self.x[i-1] == self.y[j-1]:
                    self.c[i][j] = self.c[i-1][j-1]+1
                else:
                    self.c[i][j] = max(self.c[i-1][j], self.c[i][j-1])
        self.d = self.c[m][n]
        # get all lcs
        if self.islist:
            self.getAllLCS(m,n,[])
        else:
            self.getAllLCS(m,n,'')

    # Get all lcs
    # given i,j, recall c[i][j] to build lcs
    # push every lcs to self.r
    # @params {int} i,j {string} z
    # @return void
    def getAllLCS(self,i,j,z):
        if i==0 or j==0:
            # 去重
            if z[::-1] not in self.r:
                self.r.append(z[::-1])
            return
        if self.x[i-1]==self.y[j-1]:
            if self.islist:
                z.append(self.x[i-1])
                self.getAllLCS(i-1,j-1,z)
            else:
                self.getAllLCS(i-1,j-1,z+self.x[i-1])
        elif self.c[i-1][j]>self.c[i][j-1]:
            self.getAllLCS(i-1,j,z)
        elif self.c[i-1][j]<self.c[i][j-1]:
            self.getAllLCS(i,j-1,z)
        else:
            tmp = copy.deepcopy(z)
            self.getAllLCS(i-1,j,z)
            self.getAllLCS(i,j-1,tmp)


'''
Calculate the edit-distance of 2 strings
0: same
bigger: less similar

@params {string/list} x,y
@return {int}
'''
def editDistance(x,y):
    m = len(x)
    n = len(y)
    # 空串的情况先赋值，i>0,j>0会重新赋值，先不用管
    e = [[i+j for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            a = e[i-1][j]+1
            b = e[i][j-1]+1
            if x[i-1]==y[j-1]:
                c = e[i-1][j-1]
            else:
                c = e[i-1][j-1]+1
            e[i][j]=min(a,b,c)
    return e[m][n]


'''
Calculate the cosine similarity of 2 strings
1: same
smaller: less similar
cosine distance = 1 - cosine similarity

@params {list} x,y
@return {float}
'''
def cosdis(x,y):
	assert(len(x) != len(y))
	product = 0
	a=0
	b=0
	for (i,j) in zip(x,y):
		product += i*j
		a += i**2
		b += j**2
	return product/math.sqrt(a)/math.sqrt(b)


# get ngram of a list
def ngram(s,n=2):
    m = len(s)
    assert(n<m and n>0)
    r = []
    for i in range(m-n+1):
        r.append(s[i:i+n])
    return r


'''
Calculate the DICE similarity of 2 strings
1: SOMTIMES same
smaller: less similar

@params {list} x,y
@return {float}
'''
def DICE(x,y,n=2):
    xs = ngram(x,n)
    ys = ngram(y,n)
    i = 0
    for k in xs:
        if k in ys:
            i += 1.0
    return 2*i/(len(xs)+len(ys))


'''
Calculate the ngram-distance of 2 strings
0: same
bigger: less similar

@params {list} x,y
@return {float}
'''
def ngramDistance(x,y,n=2):
    k = len(x)
    l = len(y)
    if isinstance(x,str):
        xl = list(x)
        yl = list(y)
    xp = ngram(['_']*(n-1)+xl,n)
    yp = ngram(['_']*(n-1)+yl,n)
    # 以下和编辑距离类似，只是c的计算由+1变成了+ngram的编辑距离/n
    e = [[i+j for i in range(l+1)] for j in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,l+1):
            a = e[i-1][j]+1.0
            b = e[i][j-1]+1.0
            # 网上的代码都是整除，所以还是+0或1，和编辑距离计算方法一样
            # 但整除的方法会产生问题：
            # 最后一对ngram的最后一个元素不同的序列计算结果距离也是0
            # 如'112'和'111'只有最后一个元素不同
            # 但最后一对2-gram '12','11'计算编辑距离整除n结果是0，最终距离也就是0
            # 因此这里用了浮点除，保证上述情况距离不为0
            c = e[i-1][j-1]+1.0*editDistance(xp[i-1],yp[j-1])/(n-xp[i-1].count('_'))
            e[i][j]=min(a,b,c)
    return e[k][l]/max(k,l)


'''
Calculate the string kernel of 2 strings
0: same
bigger: less similar

@params {list} x,y
@return {float}
'''