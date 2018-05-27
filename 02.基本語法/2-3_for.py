"""
 VPython教學: 2-3.基本語法 for
 日期: 2018/2/18
 作者: 王一哲
"""
result = 0
result2 = 0
result3 = 0

# 用 range(11) 產生整數 1 ~ 10 
for i in range(11):
    print("i = ", i)
    result += i

print("result = ", result)

# 用 range(1, 11) 產生整數 1 ~ 10 
for i in range(1, 11):
    print("i = ", i)
    result2 += i

print("result2 = ", result2)

# 用 range(1, 11, 2) 產生奇數 1 ~ 9 
for i in range(1, 11, 2):
    print("i = ", i)
    result3 += i

print("result3 = ", result3)
