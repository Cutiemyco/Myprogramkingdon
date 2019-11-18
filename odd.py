#coding:gbk
#利用for语句嵌套，实现输出九九乘法表。
#作者:伍杰
for i in range(1,10):
	for j in range(i,10):
		print("%d*%d=%d"%(i,j,i*j),end="  ")
		print("")
		
