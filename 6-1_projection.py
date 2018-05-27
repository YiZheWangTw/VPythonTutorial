"""
 VPython教學: 6-1.斜向抛射, 球落地停止運作
 日期: 2018/2/21
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1              # 小球半徑
v0 = 30               # 小球初速
theta = radians(30)   # 小球抛射仰角, 用 radians 將單位轉為弧度
L = 100               # 地板長度
g = 9.8               # 重力加速度 9.8 m/s^2
t = 0                 # 時間
dt = 0.001            # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
"""
scene = canvas(title = "Projection", width = 800, height = 400, x = 0, y = 0, center = vector(0, 5, 0), \
                          background = vector(0, 0.6, 0.6))
floor = box(pos = vector(0, -size, 0), length = L, height = 0.01, width = 10, texture = textures.metal)
ball = sphere(pos = vector(-L/2, 0, 0), radius = size, color = color.red, make_trail = True)
ball.v = vector(v0*cos(theta), v0*sin(theta), 0)
ball.a = vector(0, -g, 0)

"""
 3. 物體運動部分
"""
while(ball.pos.y >= 0):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    t += dt

print(t, ball.pos.x + L/2)
