"""
 VPython教學: 2-1.基本語法 if
 日期: 2018/2/18
 作者: 王一哲
"""

# 預設 a, b 量值的寫法
# a = 10
# b = 10

# 由使用者輸入 a, b 量值的寫法
a = int(input("a = "))
b = int(input("b = "))

# 1層if
if(a > b):
    print("a > b")
else:
    print("a <= b")

# 2層if
if(a > b):
    print("a > b")
elif(a == b):
    print("a = b")
else:
    print("a < b")
