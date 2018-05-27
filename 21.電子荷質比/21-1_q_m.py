"""
 VPython教學: 21-1.電子荷質比
 日期: 2018/4/8
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
size = 0.005                  # 粒子半徑
m = 1E-11                     # 粒子質量
v0 = 10                       # 粒子水平速度
q = -3E-9                     # 粒子電量
V = 1                         # 平行帶電板間的電壓
d = 0.1                       # 平行帶電板間的距離
L = 0.2                       # 平行帶電板間的長度
E_field = vector(0, -V/d, 0)  # 電場
t = 0                         # 時間
dt = 1E-5                     # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生平行帶電板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 cylinder 物件產生水平線 http://www.glowscript.org/docs/VPythonDocs/cylinder.html
    (4) 用 sphere 物件產生帶電粒子 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (5) 用 arrow 物件產生表示速度、加速度用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (6) 用 label 產生標籤 http://www.glowscript.org/docs/VPythonDocs/label.html
"""
# 產生動畫視窗、平行帶電板、水平線、帶電粒子
scene = canvas(title = "q/m", width = 800, height = 600, x = 0, y = 0, center = vector(0, 0, 0), \
                          background = color.black)
p1 = box(pos = vector(-L/2, d/2, 0), length = L, height = 0.01*L, width = L, color = color.blue)
p2 = box(pos = vector(-L/2, -d/2, 0), length = L, height = 0.01*L, width = L, color = color.blue)
screen = box(pos = vector(L, 0, 0), length = 0.01*L, height = 1.5*L, width = L, color = color.blue)
line = cylinder(pos = vector(-1.5*L, 0, 0), radius = 0.2*size, axis = vector(3*L, 0, 0), color = color.yellow)
charge = sphere(pos = vector(-1.5*L, 0, 0), v = vector(v0, 0, 0), radius = size, color = color.red, make_trail = True)
# 產生表示電場的箭頭及標籤
arrow_E = arrow(pos = vector(-L, d/2, 0), axis = vector(0, -0.1, 0), shaftwidth = size, color = color.green)
label_E = label(pos = vector(-L, d/2, 0), text = "E", xoffset = -25, yoffset = 25, color = color.green, font = "sans")
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos = charge.pos, shaftwidth = 0.3*size, color = color.cyan)
arrow_a = arrow(pos = charge.pos, shaftwidth = 0.3*size, color = color.magenta)

"""
 3. 物體運動部分, 當帶電粒子到達屏幕或撞到平行帶電板時停止
"""
xp = charge.pos.x
while(0 < charge.pos.x < screen.pos.x - screen.length/2 - size or \
      (charge.pos.x < 0 and abs(charge.pos.y) < d/2 - p1.height - size)):
    rate(500)
# 計算帶電粒子所受合力, 在平行帶電板間才有電場
    if(-L <= charge.pos.x <= 0): F = q*E_field
    else: F = vector(0, 0, 0)
# 更新帶電粒子加速度、速度、位置
    charge.a = F/m
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
        line2 = cylinder(pos = vector(-1.5*L, charge.pos.y, 0), radius = 0.2*size, axis = vector(3*L, 0, 0), color = color.yellow)
    xp = xc
# 更新時間
    t += dt
