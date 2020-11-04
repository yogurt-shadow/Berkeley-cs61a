 #!/usr/bin/env python
# coding:utf-8


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq


# 待拟合的数据
X = np.array([36.4,35.7,36.3,36.3,36.3,36.1,36.0,36.1,35.9,35.8,34.0,35.7,36.3,35.9,35.5
,36.1,36.0,36.1,36.1,36.2,36.3,36.3,35.9,35.8,35.7,35.7,35.8,35.9,35.9,35.9,35.9,35.9,35.9
,36.7,36.7,36.7,36.7,36.7,36.7,36.8,36.8,36.8,36.8,36.8])

Y=np.array([855.65,850.781,854.809,853.198,857.226,853.198,852.392,851.586,853.198,858.32,
853.198,861.254,868.505,860.449,871.728,853.198,864.477,866.88,853.32,850.781,853.198,865.283
,861.254,862.60,861.254,866.894,866.88,862.886,862.866,861.254,859.243,862.60,865.283,869.311,854.3,865.283,
852.393,869.311,872.534,853.198,871.728,862.866,877.368,857.266,])


# 二次函数的标准形式
def func(params, x):
 a, b, c = params
 return a * x * x + b * x + c


# 误差函数，即拟合曲线所求的值与实际值的差
def error(params, x, y):
 return func(params, x) - y


# 对参数求解
def slovePara():
 p0 = [10, 10, 10]

 Para = leastsq(error, p0, args=(X, Y))
 return Para


# 输出最后的结果
def solution():
 Para = slovePara()
 a, b, c = Para[0]
 print "a=",a," b=",b," c=",c
 print "cost:" + str(Para[1])
 print "求解的曲线是:"
 print("y="+str(round(a,2))+"x*x+"+str(round(b,2))+"x+"+str(c))

 plt.figure(figsize=(8,6))
 plt.scatter(X, Y, color="green", label="sample data", linewidth=2)

 # 画拟合直线
 x=np.linspace(0,12,100) ##在0-15直接画100个连续点
 y=a*x*x+b*x+c ##函数式
 plt.plot(x,y,color="red",label="solution line",linewidth=2)
 plt.legend() #绘制图例
 plt.show()


solution()
