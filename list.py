# 获取元素
"""
array = [[1,2,3],[5,6,7],[8,9,10]]
a=array[1]# [5, 6, 7]
b=array[1][2]# 7
print(a,b)
"""

# 列表可以无限嵌套
array = [[
    [1,2,3],[5,6,7],[8,9,10]],
    [["hi",2,3],[5,6,7]],
    [[False,2,3],[8,9,10]
]]
# 遍历列表,列表可以添加任何元素
for a in array:
    for b in a :
        for c in b:
            print(c)

# 判断元素是否在列表里
a = [1,False,"eat",b,[1,2,3]]
if 1 in a:
    print("yes")
if "happy" not in a:
    print("no")

a.append("happy")# 将元素插入列表队尾
if "happy" in a:
    print("yes")
print(a)

a.insert(2,"ccc")# 在指定位置插入元素
print(a)

a.pop(1)# 指定位置删除元素
print(a)

a.remove("eat")# 匹配元素名称删除元素
print(a)

a.clear()# 清空列表
print(a)

del a# 删除列表

a=[1, False, 'ccc', 'eat', [8, 9, 10], [1, 2, 3], 'happy']
print(a)
a[0]=123
print(a)
b=a # 仅复制指针
b=a.copy() #复制数据

a=[4,2,1,3]
a.sort()
a=sorted(a)# 都是对a进行从小到大的数字排序
print(a)

