"""def isDouble(n):
    return n%2 == 0

num=int(input("输入一个数字以判断奇偶："))
if isDouble(num):
    print(f"数字{num}是偶数")
else :
    print(f"数字{num}是奇数")
"""

def a (n,age=18,*args,**kwargs):
    if age >=18:
        print(n)
        for i in args:
            print(i)
    else:
        print("no!")
    print(kwargs["ns"])
    print(kwargs["nt"])

a(1,196,2,3,6,9,ns=15,nt=16)