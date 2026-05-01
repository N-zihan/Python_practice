import math # “import”是用于导入某个函数库，少了这个甭想拿代码当计算器使唤！
print(math.sin(math.pi/2))
print(math.log2(16))
### 接下来是方程计算！###
## 计算方程：-x**2-2x+3=0 ##
# 注：“*”为乘号，“**”为乘方 #
a = -1
b = -2
c = 3
delta = b ** 2 - 4 * a * c
print((-b + math.sqrt(delta))/(2 * a))
print((-b - math.sqrt(delta))/(2 * a))