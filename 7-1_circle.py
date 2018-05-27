"""
 VPython教學: 7-1.圓周運動
 日期: 2018/2/22
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.5            # 小球半徑
v0 = 10               # 小球初速
R = 5                 # 圓周運動半徑
L = 4*R               # 地板長度
t = 0                 # 時間
dt = 0.001            # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 arrow 物件產生表示速度及加速度的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
"""
scene = canvas(title = "Circle", width = 800, height = 400, x = 0, y = 0, background = vector(0, 0.6, 0.6))
scene.camera.pos = vector(0, L/2, L/2)
scene.camera.axis = vector(0, -L/2, -L/2)
floor = box(pos = vector(0, -size, 0), length = L, height = 0.01, width = L, texture = textures.metal)
ball = sphere(pos = vector(R, size, 0), radius = size, color = color.red, make_trail = True, retain = 100)
ball.v = vector(0, 0, -v0)
arrow_v = arrow(pos = ball.pos, axis = ball.v, radius = 0.2*size, shaftwidth = 0.4*size, color = color.green)
arrow_a = arrow(pos = ball.pos, axis = vector(0, 0, 0), radius = 0.2*size, shaftwidth = 0.4*size, color = color.blue)

"""
 3. 物體運動部分
"""
while(True):
    rate(1000)
    axis = vector(0, size, 0) - ball.pos
    ball.a = (ball.v.mag2 / R) * axis.norm()
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    arrow_v.pos = ball.pos
    arrow_v.axis = ball.v
    arrow_a.pos = ball.pos
    arrow_a.axis = ball.a
    t += dt
