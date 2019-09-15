"""
 VPython教學: 19-1.靜電力造成的簡諧運動（放置在連心線中點右側）
 Ver. 1: 2018/3/14
 Ver. 2: 2019/9/15
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 當 h << d 時週期理論值 5.2345 s
"""
size, m = 1, 1         # 小球半徑, 質量
q, Q = 2E-4, 2E-4      # 小球電量, 大球電量
d, h = 10, 3           # 大球之間距離的0.5倍, 小球在連心線中點右側的距離
k = 8.988E9            # 靜電力常數
i, t, dt = 0, 0, 0.001 # 小球回到初位置的次數, 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Electric Force and Simple Harmonic Motion", width=600, height=600, x=0, y=0,
               center=vec(0, 0, 0), background=color.black)
# 產生固定位置的大球、可移動的小球
s1 = sphere(pos=vec(-d, 0, 0), radius=size, color=color.blue)
s2 = sphere(pos=vec(d, 0, 0), radius=size, color=color.blue)
ball = sphere(pos=vec(h, 0, 0), v=vec(0, 0, 0), radius=0.4*size, color=color.red, m=m)
# 畫大球連心線、平衡點、端點位置   
line = cylinder(pos=s1.pos, axis=s2.pos-s1.pos, radius=0.1*size, color=color.yellow)
center = cylinder(pos=vec(0, -2, 0), axis=vec(0, 4, 0), radius=0.1*size, color=color.white)
right = cylinder(pos=vec(h, -2, 0), axis=vec(0, 4, 0), radius=0.1*size, color=color.white)
left = cylinder(pos=vec(-h, -2, 0), axis=vec(0, 4, 0), radius=0.1*size, color=color.white)
# 產生代表速度、加速度的箭頭
arrow_v = arrow(pos=ball.pos+vec(0, 1, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.green)
arrow_a = arrow(pos=ball.pos+vec(0, 2, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.magenta)
# 繪圖部分
gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i> (s)",
           ytitle="blue: <i>x</i> (m), green: <i>v</i> (m/s), magenta: <i>a</i> (m/s<sup>2</sup>)")
xt = gcurve(graph=gd, color=color.blue)
vt = gcurve(graph=gd, color=color.green)
at = gcurve(graph=gd, color=color.magenta)

"""
 3. 物體運動部分, 小球來回 5 次時停止
"""
while(i < 5):
    rate(1000)
# 計算小球所受靜電力並存到變數 F
    r1 = ball.pos - s1.pos
    r2 = ball.pos - s2.pos
    F1 = (k*Q*q) / r1.mag2 * r1.norm()
    F2 = (k*Q*q) / r2.mag2 * r2.norm()
    F = F1 + F2
# 計算運動中小球的加速度、速度、位置, 畫出代表速度、加速度的箭頭
    ball.a = F/ball.m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    arrow_v.pos = ball.pos + vec(0, 1, 0)
    arrow_a.pos = ball.pos + vec(0, 2, 0)
    arrow_v.axis = ball.v
    arrow_a.axis = ball.a
# 畫出 x-t, v-t, a-t 圖
    xt.plot(pos=(t, ball.pos.x))
    vt.plot(pos=(t, ball.v.x))
    at.plot(pos=(t, ball.a.x))
# 判斷小球是否回到出發點, 計算回到出發點的次數
    if(ball.pos.x >= h and ball.v.x >= 0):
        print(t)
        i += 1
# 更新時間
    t += dt
