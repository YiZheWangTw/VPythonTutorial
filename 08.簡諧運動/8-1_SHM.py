"""
 VPython教學: 8-1.簡諧運動
 Ver. 1: 2018/2/25
 Ver. 2: 2019/9/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
m = 4               # 木塊質量 4 kg
size = 1            # 木塊邊長 1 m
R = 5               # 振幅 5 m
k = 1               # 彈性常數 1 N/m
L0 = R + size       # 彈簧原長
i = 0               # 木塊回到初位置的次數
t = 0               # 時間
dt = 0.001          # 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗、地板、木塊、彈簧
scene = canvas(title="Simple Harmonic Motion", width=800, height=400, x=0, y=0, background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -(size+0.1)/2, 0), size=vec(2*L0, 0.1, R), texture=textures.metal)
wall = box(pos=vec(-L0, 0, 0), size=vec(0.1, size, R), texture=textures.metal)
block = box(pos=vec(R+size/2, 0, 0), size=vec(size, size, size), texture=textures.wood, v=vec(0, 0, 0))
spring = helix(pos=vec(-L0, 0, 0), radius=0.3*size, thickness=0.05*size, color=color.yellow)
spring.axis = block.pos - spring.pos - vec(size/2, 0, 0)
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=block.pos + vec(0, size, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.green)
arrow_a = arrow(pos=block.pos + vec(0, 2*size, 0), axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.magenta)
# 繪圖部分
gd = graph(title="plot", width=600, height=450, x=0, y=400, xtitle="<i>t</i>(s)", 
           ytitle="blue: <i>x</i>(m), green: <i>v</i>(m/s), magenta: <i>a</i>(m/s<sup>2</sup>)")
xt = gcurve(graph=gd, color=color.blue)
vt = gcurve(graph=gd, color=color.green)
at = gcurve(graph=gd, color=color.magenta)

"""
 3. 物體運動部分, 重覆3個週期
"""
while(i < 3):
    rate(1000)
# 計算彈簧長度、伸長量、回復力
    spring.axis = block.pos - spring.pos - vec(0.5*size, 0, 0)
    F = -k * (spring.axis - vec(L0, 0, 0))
# 計算木塊加速度, 更新速度、位置
    block.a = F/m
    block.v += block.a*dt
    block.pos += block.v*dt
# 更新代表速度、加速度的箭頭位置、方向、長度
    arrow_v.pos = block.pos + vec(0, size, 0)
    arrow_a.pos = block.pos + vec(0, 2*size, 0)
    arrow_v.axis = block.v
    arrow_a.axis = block.a
# 畫出 x-t, v-t, a-t 圖
    xt.plot(pos=(t, block.pos.x - size/2))
    vt.plot(pos=(t, block.v.x))
    at.plot(pos=(t, block.a.x))
# 判斷木塊是否回到出發點, 計算回到出發點的次數
    if(block.pos.x > R + size/2 and block.v.x > 0):
        print(i, t)
        i += 1
# 更新時間
    t += dt
