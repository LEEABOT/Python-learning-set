a =(1,2)# 元组不能被修改 又称只读列表 可以访问
print(a[1],"\n")

a="1242345235324"
b=[1,2,"d",4,5]
c=(1,2,"h")

for i in b:
    print(i)

for i in range(len(c)):
    print("\n",c[i])


s={1,2,4,5,6,6}# 集合逻辑上没有顺序，没有重复项，出现重复项会自动去掉
print(s)

d={"name":"lmj","age":23}
print(d.keys())# 获得字典中所有的键

print(d.values())# 获得字典中所有的值

print(d.items())# 获得字典中所有的键值对组成的元组，通过列表输出

print(d["name"])# 获取对应项的值

d["name"]="ggbond"# 更改对应项的值
print(d)

for k ,v in d.items():# 遍历字典 k为当前遍历项的键，v标识当前遍历项的值
    print(k)
    print(v)

a={}    # 空字典
b=set() # 空集合


del d["age"]# 删除某个键值对
print(d)
d.clear()# 清空字典
print(d)
del d # 删除字典