"""
 VPython教學: 2-2.基本語法 while
 日期: 2018/2/18
 作者: 王一哲
"""
result = 0
result2 = 0
i = 1
j = 1
n = 10

while(i <= n):
    print("i = ", i)
    result += i
    i += 1

print("result = ", result)

while(j <= n):
    print("j = ", j)
    result2 += j
    j += 2

print("result2 = ", result2)
