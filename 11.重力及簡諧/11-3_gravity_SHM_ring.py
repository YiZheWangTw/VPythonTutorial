"""
 VPython教學: 11-3.重力造成的簡諧運動, 圓環, 初速為0, 從端點出發
 Ver. 1: 2018/2/25
 Ver. 2: 2018/3/14
 Ver. 3: 2019/9/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 當 h << r 時週期理論值 3.44058 s
"""
size = 0.4            # 小球半徑
m = 1                 # 小球質量
M = 5E13              # 圓環的質量
r = 10                # 圓環的半徑
N = 100               # 圓環分割成小球的數量
dM = M/N              # 圓環分割後每個小球的質量
h = 9                 # 小球在圓環中垂線上的距離
G = 6.67E-11          # 重力常數
v0 = 0                # 小球初速
j = 0                 # 小球回到初位置的次數
t = 0                 # 時間
dt = 0.001            # 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Gravity and SHM", width=600, height=600, x=0, y=0,
               center=vec(0, h, 0), background=color.black)
# 產生質量為 m 的星球並設定初速度
ball = sphere(pos=vec(0, h, 0), radius=size, color=color.red, v=vec(0, v0, 0))
# 畫圓環間的連線、上端點、下端點
line1 = cylinder(pos=vec(-r, 0, 0), axis=vec(2*r, 0, 0), radius=0.1*size, color=color.yellow)
line2 = cylinder(pos=vec(0, 0, -r), axis=vec(0, 0, 2*r), radius=0.1*size, color=color.yellow)
top = cylinder(pos=vec(-2, h, 0), axis=vec(4, 0, 0), radius=0.1*size, color=color.white)
bottom = cylinder(pos=vec(-2, -h, 0), axis=vec(4, 0, 0), radius=0.1*size, color=color.white)
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=ball.pos+vec(1, 0, 0), axis=vec(0, 0, 0), shaftwidth=0.8*size, color=color.green)
arrow_a = arrow(pos=ball.pos+vec(2, 0, 0), axis=vec(0, 0, 0), shaftwidth=0.8*size, color=color.magenta)
# 產生質量為 M 的圓環及空白 list, 用 for 迴圈產生圓環分割後的小球並填入空白 list 中
stars_ring = ring(pos=vec(0, 0, 0), axis=vec(0, 1, 0), radius=r, thickness=0.4*size, color=color.green)
stars = []
for i in range(0, N):
    stars.append(sphere(pos=vec(r*cos(i*2*pi/N), 0, r*sin(i*2*pi/N)), radius=0.5*size, color=color.blue))
# 繪圖部分
gd = graph(title="plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i> (s)", 
           ytitle="blue: <i>y</i> (m), green: <i>v</i> (m/s), magenta: <i>a</i> (m/s<sup>2</sup>)")
yt = gcurve(graph=gd, color=color.blue)
vt = gcurve(graph=gd, color=color.green)
at = gcurve(graph=gd, color=color.magenta)

"""
 3. 物體運動部分, 小球來回 5 次時停止
"""
while(j < 5):
    rate(1000)
# 用 for 迴圈將 stars 當中的小球依序讀取出來指定給變數 star, 計算小球的重力並存到變數 F
    F = vec(0, 0, 0)
    for star in stars:
        r = ball.pos-star.pos
        f = -(G*dM*m) / r.mag2 * r.norm()
        F += f
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
    if(ball.pos.y >= h and ball.v.y >= 0):
        print(t)
        j += 1
# 更新時間
    t += dt
