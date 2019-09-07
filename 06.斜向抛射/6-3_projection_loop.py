"""
 VPython教學: 6-3.斜向抛射, 使用for 迴圈改變仰角 theta, 空氣阻力係數 b
 Ver. 1: 2018/3/29
 Ver. 2: 2019/9/7
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size=1                 # 小球半徑
m=1                    # 小球質量
v0=30                  # 小球初速
degree=30              # 小球抛射仰角, 單位為角度
theta=radians(degree)  # 小球抛射仰角, 用 radians 將單位轉為弧度
L=100                  # 地板長度
#b=0.0                  # 空氣阻力 f=-bv
g=9.8                  # 重力加速度 9.8 m/s^2
t=0                    # 時間
dt=0.001               # 時間間隔
n=10                   # 於 for 迴圈當中代入數值的次數, 改變 theta 時設為16, 改變 b 時設為10

"""
 2. 畫面設定
"""
scene = canvas(title="Projection with for loop", width=800, height=400, x=0, y=0,
               center=vec(0, 5, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, 10), texture=textures.metal)

# 開啟檔案 data.csv, 屬性為寫入, 先寫入欄位的標題
file = open("data.csv", "w", encoding="UTF-8")
file.write("v0(m/s), theta(degree), b, t(s), R(m)\n")

"""
 3. 物體運動部分
"""
for i in range(0, n):
# 改變 theta 使用以下 2 行
#    degree = 15 + 5*i
#    theta = radians(degree)
# 改變 b 使用以下 1 行
    b = 0.1*i
    ball = sphere(pos=vec(-L/2, 0, 0), radius=size, color=vec((n-i)/n, 0, i/n),
                  make_trail=True, v=vec(v0*cos(theta), v0*sin(theta), 0))
    while(ball.pos.y - floor.pos.y >= size):
        rate(1000)
        f = -b*ball.v
        ball.a = vec(0, -g, 0) + f/m
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
    print(v0, degree, b, t, ball.pos.x + L/2)
    file.write(str(v0) + "," + str(degree) + "," + str(b) + "," + str(t) + "," + str(ball.pos.x + L/2) + "\n")

file.close() # 關閉檔案
