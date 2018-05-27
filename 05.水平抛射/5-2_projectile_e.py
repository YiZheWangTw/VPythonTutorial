"""
 VPython教學: 5-2.水平抛射, 恢復係數e
 日期: 2018/2/19
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
v0 = 5       # 小球水平初速
e = 0.8      # 恢復係數
h = 15       # 小球離地高度
L = 50       # 地板長度
g = 9.8      # 重力加速度 9.8 m/s^2
i = 0        # 小球撞地板次數
t = 0        # 時間
dt = 0.001   # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
scene = canvas(title = "Projectile", width = 800, height = 600, x = 0, y = 0, center = vector(0, h/2, 0), \
                          background = vector(0, 0.6, 0.6))
floor = box(pos = vector(0, -size, 0), length = L, height = 0.01, width = 10, texture = textures.metal)
ball = sphere(pos = vector(-L/2, h, 0), radius = size, texture = textures.wood, make_trail = True)
ball.v = vector(v0, 0, 0)
ball.a = vector(0, -g, 0)

"""
 3. 物體運動部分, 小球觸地時反彈
"""
while(ball.pos.x < L/2):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    if(ball.pos.y <= floor.height):
        i += 1
        print(i, t, ball.pos.x + L/2)
        ball.v.y = -ball.v.y*e
    t += dt
