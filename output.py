a = "my name is xxx"
a = a[:5]
print(a)

a = "my name is xxx"
a = a[1:5]
print(a)

a = "my name is xxx"# 每两个字符输出一个
a = a[1:5:2]
print(a)

a = "my name is xxx"# 倒着输出
a = a[ : :-1]
print(a)

a = "my name is xxx"# 倒着输出区间字符
a = a[-5:-1]
print(a)

a = "my name is xxx"
a = a.replace("xxx","lmj")# 替换字符串中的某一段
print(a)

a = "my name is xxx"
arr = a.split(" ")# 分隔字符串的每一段，括号内的作为判断分隔的字符
print(arr)

# 大小写转换
a = "hello friend".capitalize()# 将字符串中的第一个字母转换为大写
print(a)
a = "hello friend".title()# 将字符串中的每个单词第一个字母转换为大写
print(a)
a = "HELLO FRIEND".lower()# 将字符串中大写转换为小写
print(a)
a = "hello friend".upper()# 将字符串中小写转换为大写
print(a)

# 删除空白字符
b = "   good".lstrip()# 删除字符串左边空白字符
print(b)
b = "good  ".rstrip()# 删除字符串右边空白字符
print(b)
b = "   good   ".strip()# 删除字符串两边空白字符
print(b)