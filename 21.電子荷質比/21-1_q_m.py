"""
 VPython教學: 21-1.電子荷質比
 Ver. 1: 2018/4/8
 Ver. 2: 2019//9/16
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) 向上撞到平行帶電板 v0 = 10, q = -3E-9, V = 1, d = 0.1
    (2) 向上但不會撞到平行帶電板 v0 = 10, q = -2E-9, V = 1, d = 0.1
    (3) 向上但不會撞到平行帶電板 v0 = 20, q = -3E-9, V = 1, d = 0.1
    (4) 向下撞到平行帶電板 v0 = 10, q = 3E-9, V = 1, d = 0.1
    (5) 向下但不會撞到平行帶電板 v0 = 10, q = 2E-9, V = 1, d = 0.1
    (6) 向下但不會撞到平行帶電板 v0 = 20, q = 3E-9, V = 1, d = 0.1
"""
size, m, q, v0 = 0.005, 1E-11, -3E-9, 10   # 粒子半徑, 質量, 電量, 水平速度
V, d, L = 1, 0.1, 0.2      # 平行帶電板間的電壓, 距離, 長度
E_field = vec(0, -V/d, 0)  # 電場
t, dt = 0, 1E-5            # 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗、平行帶電板、水平線、帶電粒子
scene = canvas(title="Mass-to-Charge Ratio", width=800, height=600, x=0, y=0,
               center=vec(0, 0, 0), background = color.black, range=1.2*L)
p1 = box(pos=vec(-L/2, d/2, 0), size=vec(L, 0.01*L, L), color=color.blue)
p2 = box(pos=vec(-L/2, -d/2, 0), size=vec(L, 0.01*L, L), color=color.blue)
screen = box(pos=vec(L, 0, 0), size=vec(0.01*L, 1.5*L, L), color=color.blue)
line = cylinder(pos=vec(-1.5*L, 0, 0), radius=0.2*size, axis=vec(3*L, 0, 0), color=color.yellow)
charge = sphere(pos=vec(-1.5*L, 0, 0), v=vec(v0, 0, 0), radius=size, color=color.red, m=m, make_trail=True)
# 產生表示電場的箭頭及標籤
arrow_E = arrow(pos=vec(-L, d/2, 0), axis=vec(0, -0.1, 0), shaftwidth=size, color=color.green)
label_E = label(pos=vec(-L, d/2, 0), text="E", xoffset=-25, yoffset=25, color=color.green, font="sans")
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=charge.pos, shaftwidth=0.3*size, color=color.cyan)
arrow_a = arrow(pos=charge.pos, shaftwidth=0.3*size, color=color.magenta)

"""
 3. 物體運動部分, 當帶電粒子到達屏幕或撞到平行帶電板時停止
"""
xp = charge.pos.x
while(0 < charge.pos.x < screen.pos.x - screen.length/2 - size or \
      (charge.pos.x < 0 and abs(charge.pos.y) < d/2 - p1.height - size)):
    rate(500)
# 計算帶電粒子所受合力, 在平行帶電板間才有電場
    if(-L <= charge.pos.x <= 0): F = q*E_field
    else: F = vec(0, 0, 0)
# 更新帶電粒子加速度、速度、位置
    charge.a = F/charge.m
    charge.v += charge.a*dt
    charge.pos += charge.v*dt
# 更新表示速度、加速度的箭頭, 只畫出方向以避免動畫自動縮小
    arrow_v.pos = charge.pos
    arrow_a.pos = charge.pos
    arrow_v.axis = charge.v.norm()*0.05
    arrow_a.axis = charge.a.norm()*0.05
# 當帶電粒子離開平行帶電板時畫出水平線標示 y 方向位移
    xc = charge.pos.x
    if(xp < 0 and xc > 0):
        line2 = cylinder(pos=vec(-1.5*L, charge.pos.y, 0), radius=0.2*size,
                         axis=vec(3*L, 0, 0), color=color.yellow)
    xp = xc
# 更新時間
    t += dt
