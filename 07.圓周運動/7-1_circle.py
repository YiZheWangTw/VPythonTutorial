"""
 VPython教學: 7-1.圓周運動
 Ver. 1: 2018/2/22
 Ver. 2: 2019/9/7
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
"""
scene = canvas(title="Circle", width=800, height=400, x=0, y=0, background=vec(0, 0.6, 0.6))
scene.camera.pos = vec(0, L/2, L/2)
scene.camera.axis = vec(0, -L/2, -L/2)
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, L), texture=textures.metal)
ball = sphere(pos=vec(R, size, 0), radius=size, color=color.red, make_trail=True, retain=100, v=vec(0, 0, -v0))
arrow_v = arrow(pos=ball.pos, axis=ball.v, radius=0.2*size, shaftwidth=0.4*size, color=color.green)
arrow_a = arrow(pos=ball.pos, axis=vec(0, 0, 0), radius=0.2*size, shaftwidth=0.4*size, color=color.blue)

"""
 3. 物體運動部分
"""
while(True):
    rate(1000)
    axis = vec(0, size, 0) - ball.pos
    ball.a = (ball.v.mag2 / R) * axis.norm()
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    arrow_v.pos = ball.pos
    arrow_v.axis = ball.v
    arrow_a.pos = ball.pos
    arrow_a.axis = ball.a
    t += dt
