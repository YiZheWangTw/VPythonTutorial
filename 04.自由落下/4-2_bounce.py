"""
 VPython教學: 4-2.自由落下, 小球觸地時反彈
 Ver. 1: 2018/2/18
 Ver. 2: 2019/9/6
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
h = 15       # 小球離地高度
g = 9.8      # 重力加速度 9.8 m/s^2
t = 0        # 時間
dt = 0.001   # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title="Free Fall", width=600, height=600, x=0, y=0, center=vec(0, h/2, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, 0, 0), size=vec(40, 0.01, 10), color=color.blue)
ball = sphere(pos=vec(0, h, 0), radius=size, color=color.red, v=vec(0, 0, 0), a=vec(0, -g, 0))
gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="t(s)", ytitle="blue: y(m), red: v(m/s)")
yt = gcurve(graph=gd, color=color.blue)
vt = gcurve(graph=gd, color=color.red)

"""
 3. 物體運動部分, 小球觸地時反彈
"""
while(t < 20):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    yt.plot(pos=(t, ball.pos.y))
    vt.plot(pos=(t, ball.v.y))
    if(ball.pos.y - floor.pos.y <= size + 0.5*floor.height and ball.v.y < 0):
        ball.v.y = -ball.v.y
    t += dt


print("t = ", t)
