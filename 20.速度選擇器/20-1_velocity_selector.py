"""
 VPython教學: 20-1.速度選擇器
 Ver. 1: 2018/4/7
 Ver. 2: 2019/9/16
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) 直線 v0 = E/B = V/(B*d), v0 = 10, V = 1, d = 0.1, B = 1
    (2) q > 0, 向上 v0*B > E = V/d, e.g. v0 = 20
    (3) q > 0, 向上 v0*B > E = V/d, e.g. d = 0.2
    (4) q > 0, 向下 v0*B < E = V/d, e.g. V = 2
    (5) q > 0, 向上 v0*B > E = V/d, e.g. B = 5
"""
size, m, v0, q = 0.005, 1E-10, 10, 1E-9  # 粒子半徑, 質量, 水平速度, 電量
V, d, L, B = 1, 0.1, 0.2, 1 # 平行帶電板間的電壓, 距離, 長度, 外加磁場強度
E_field = vec(0, -V/d, 0)   # 電場
B_field = vec(0, 0, -B)     # 磁場
t, dt = 0, 1E-5             # 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗、平行帶電板、水平線、帶電粒子
scene = canvas(title="Velocity Selector", width=800, height=600, x=0, y=0, center=vec(0, 0, 0), background=color.black)
p1 = box(pos=vec(0, d/2, 0), size=vec(L, 0.01*L, L), color=color.blue)
p2 = box(pos=vec(0, -d/2, 0), size=vec(L, 0.01*L, L), color=color.blue)
line = cylinder(pos=vec(-L, 0, 0), radius=0.1*size, axis=vec(2*L, 0, 0), color=color.yellow)
charge = sphere(pos=vec(-L, 0, 0), v=vec(v0, 0, 0), radius=size, color=color.red, m=m, make_trail=True)
# 產生表示電場、磁場的箭頭及標籤
arrow_E = arrow(pos=vec(-L/2, d/2, 0), axis=vec(0, -0.1, 0), shaftwidth=size, color=color.green)
arrow_B = arrow(pos=vec(-L/2, 0, d/2), axis=vec(0, 0, -0.1), shaftwidth=size, color=color.orange)
label_E = label(pos=vec(-L/2, d/2, 0), text="E", xoffset=-25, yoffset=25, color=color.green, font="sans")
label_B = label(pos=vec(-L/2, 0, d/2), text="B", xoffset=-25, yoffset=-25, color=color.orange, font="sans")
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos=charge.pos, shaftwidth=0.3*size, color=color.cyan)
arrow_a = arrow(pos=charge.pos, shaftwidth=0.3*size, color=color.magenta)

"""
 3. 物體運動部分, 當帶電粒子到達畫面最右側或撞到平行帶電板時停止
"""
while(charge.pos.x < L and abs(charge.pos.y) < d/2 - p1.height - size):
    rate(500)
# 計算帶電粒子所受合力, 在平行帶電板間才有電場、磁場
    if(-L/2 <= charge.pos.x <= L/2): F = q*(E_field + cross(charge.v, B_field))
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
# 更新時間
    t += dt
