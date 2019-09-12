"""
 VPython教學: 11-1.重力造成的簡諧運動, 初速為0, 從端點出發
 Ver. 1: 2018/2/23
 Ver. 2: 2018/3/14
 Ver. 3: 2019/9/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 當 h << d 時週期理論值 3.84669 s
"""
size = 1              # 小球半徑
m = 1                 # 小球質量
M = 2E13              # 星球質量
d = 10                # 星球之間的距離*0.5倍
h = 9                 # 小球在星球連線的中垂線上的距離
G = 6.67E-11          # 重力常數
v0 = 0                # 小球初速
i = 0                 # 小球回到初位置的次數
t = 0                 # 時間
dt = 0.001            # 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Gravity and SHM", width=600, height=600, x=0, y=0,
               center=vec(0, 0, 0), background=color.black)
# 產生 2 個質量為 M 的星球
s1 = sphere(pos=vec(-d, 0, 0), radius=size, color=color.blue)
s2 = sphere(pos=vec(d, 0, 0), radius=size, color=color.blue)
# 產生質量為 m 的星球並設定初速度
ball = sphere(pos=vec(0, h, 0), radius=0.4*size, color=color.red, v=vec(0, v0, 0))
# 畫星球間的連線、上端點、下端點
line = cylinder(pos=s1.pos, axis=s2.pos - s1.pos, radius=0.1*size, color=color.yellow)
top = cylinder(pos=vec(-2, h, 0), axis=vec(4, 0, 0), radius=0.1*size, color=color.white)
bottom = cylinder(pos=vec(-2, -h, 0), axis=vec(4, 0, 0), radius=0.1*size, color=color.white)
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=ball.pos + vec(1, 0, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.green)
arrow_a = arrow(pos=ball.pos + vec(2, 0, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.magenta)
# 繪圖部分
gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i> (s)", 
           ytitle="blue: <i>y</i> (m), green: <i>v</i> (m/s), magenta: <i>a</i> (m/s<sup>2</sup>)")
yt = gcurve(graph=gd, color=color.blue)
vt = gcurve(graph=gd, color=color.green)
at = gcurve(graph=gd, color=color.magenta)

"""
 3. 物體運動部分, 小球來回 5 次時停止
"""
while(i < 5):
    rate(1000)
# 計算小球所受重力並存到變數 F
    r1 = ball.pos - s1.pos
    r2 = ball.pos - s2.pos
    F1 = -(G*M*m) / r1.mag2 * r1.norm()
    F2 = -(G*M*m) / r2.mag2 * r2.norm()
    F = F1 + F2
# 計算運動中小球的加速度、速度、位置, 畫出代表速度、加速度的箭頭
    ball.a = F/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    arrow_v.pos = ball.pos + vec(1, 0, 0)
    arrow_a.pos = ball.pos + vec(2, 0, 0)
    arrow_v.axis = ball.v
    arrow_a.axis = ball.a
# 畫出 y-t, v-t, a-t 圖
    yt.plot(pos=(t, ball.pos.y))
    vt.plot(pos=(t, ball.v.y))
    at.plot(pos=(t, ball.a.y))
# 判斷小球是否回到出發點, 計算回到出發點的次數
    if(ball.pos.y > h):
        print(t)
        i += 1
# 更新時間
    t += dt
