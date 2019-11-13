"""
 VPython教學: 6-1.斜向抛射, 球落地停止運作
 Ver. 1: 2018/2/21
 Ver. 2: 2019/9/7
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size=1              # 小球半徑
v0=30               # 小球初速
theta=radians(30)   # 小球抛射仰角, 用 radians 將單位轉為弧度
L=100               # 地板長度
g=9.8               # 重力加速度 9.8 m/s^2
t=0                 # 時間
dt=0.001            # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title="Projection", width=800, height=400, x=0, y=0,
               center=vec(0, 5, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, 10), texture=textures.metal)
ball = sphere(pos=vec(-L/2, 0, 0), radius=size, color=color.red, make_trail=True,
              v=vec(v0*cos(theta), v0*sin(theta), 0), a=vec(0, -g, 0))

"""
 3. 物體運動部分
"""
while(ball.pos.y - floor.pos.y >= size):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    t += dt

print(t, ball.pos.x + L/2)
