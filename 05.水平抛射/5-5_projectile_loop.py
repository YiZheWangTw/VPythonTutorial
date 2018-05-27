"""
 VPython教學: 5-5.水平抛射, 用for迴圈改變h, 記錄t、R
 日期: 2018/3/21
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
v0 = 5       # 小球水平初速
L = 50       # 地板長度
g = 9.8      # 重力加速度 9.8 m/s^2
dt = 0.001   # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title = "Projectile", width = 800, height = 600, x = 0, y = 0, center = vector(0, 5, 0), \
                          background = vector(0, 0.6, 0.6))
floor = box(pos = vector(0, -size, 0), length = L, height = 0.01, width = 10, texture = textures.metal)

# 開啟檔案 data.txt, 屬性為寫入, 先寫入欄位的標題
file = open("data.txt", "w", encoding = "UTF-8")
file.write("h(m), t(s), R(m)\n")

"""
 3. 用for迴圈改變h, 計算t、R, 寫入檔案
"""
for h in range(5, 51, 1):
    t = 0
    ball = sphere(pos = vector(-L/2, h, 0), radius = size, texture = textures.wood, make_trail = True)
    ball.v = vector(v0, 0, 0)
    ball.a = vector(0, -g, 0)
# 物體運動部分
    while(ball.pos.y > floor.height/2):
        rate(500)
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
    print(h, t, ball.pos.x + L/2)
    file.write(str(h) + "," + str(t) + "," + str(ball.pos.x + L/2) + "\n")

file.close() # 關閉檔案
