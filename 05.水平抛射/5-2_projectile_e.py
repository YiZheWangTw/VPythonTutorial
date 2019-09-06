"""
 VPython教學: 5-2.水平抛射, 恢復係數e
 Ver. 1: 2018/2/19
 Ver. 2: 2019/9/6
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
"""
scene = canvas(title="Projectile", width=800, height=600, x=0, y=0, center=vec(0, h/2, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, 10), texture=textures.metal)
ball = sphere(pos=vec(-L/2, h, 0), radius=size, texture=textures.wood, make_trail=True, v=vec(v0, 0, 0), a=vec(0, -g, 0))

"""
 3. 物體運動部分, 小球觸地時反彈
"""
while(ball.pos.x < L/2):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    if(ball.pos.y - floor.pos.y <= size + 0.5*floor.height and ball.v.y < 0):
        i += 1
        print(i, t, ball.pos.x + L/2)
        ball.v.y = -ball.v.y*e
    t += dt
