import random
a = random.randint(1,100)# 0-100随机整数
b = random.uniform(1,100)# 0-100的随机数带小数
c = random.random()# 0-1之间的随机数
print(a,b,c)




a=1
print(a)
a = a+1
print(a)
a +=1
print(a)
# 加减乘除符号互换

b=2
print(b)
b=(b+10)/((2*5)-1)
print(b)
# 可以使用嵌套的括号来进行运算
"""
a = int(input("请输入一个整数以判断是否是偶数："))
b = a % 2
if b == 0:
    print("是偶数")
else:
    print("不是偶数")
# 判断奇偶数
"""
c=float(input("请输入你的分数："))
if c<0 or c>100:
    print("非法输入")
elif c<60:
    print("不及格")
elif c<80:
    print("合格")
else:
    print("优秀")