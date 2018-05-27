"""
 VPython教學: 20-1.速度選擇器
 日期: 2018/4/7
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) 直線 v0 = E/B = V/(B*d), v0 = 10, V = 1, d = 0.1, B = 1
    (2) q > 0, 向上 v0*B > E = V/d, e.g. v0  = 20
    (3) q > 0, 向上 v0*B > E = V/d, e.g. d = 0.2
    (4) q > 0, 向下 v0*B < E = V/d, e.g. V = 2
    (5) q > 0, 向上 v0*B > E = V/d, e.g. B = 5
"""
size = 0.005                  # 粒子半徑
m = 1E-10                     # 粒子質量
v0 = 10                       # 粒子水平速度 10
q = 1E-9                      # 粒子電量  
V = 1                         # 平行帶電板間的電壓
d = 0.1                       # 平行帶電板間的距離
L = 0.2                       # 平行帶電板間的長度
B = 1                         # 外加磁場強度
E_field = vector(0, -V/d, 0)  # 電場
B_field = vector(0, 0, -B)    # 磁場
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
scene = canvas(title = "Velocity Selector", width = 800, height = 600, x = 0, y = 0, center = vector(0, 0, 0), \
                          background = color.black)
p1 = box(pos = vector(0, d/2, 0), width = L, height = 0.01*L, length = L, color = color.blue)
p2 = box(pos = vector(0, -d/2, 0), width = L, height = 0.01*L, length = L, color = color.blue)
line = cylinder(pos = vector(-L, 0, 0), radius = 0.1*size, axis = vector(2*L, 0, 0), color = color.yellow)
charge = sphere(pos = vector(-L, 0, 0), v = vector(v0, 0, 0), radius = size, color = color.red, make_trail = True)
# 產生表示電場、磁場的箭頭及標籤
arrow_E = arrow(pos = vector(-L/2, d/2, 0), axis = vector(0, -0.1, 0), shaftwidth = size, color = color.green)
arrow_B = arrow(pos = vector(-L/2, 0, d/2), axis = vector(0, 0, -0.1), shaftwidth = size, color = color.orange)
label_E = label(pos = vector(-L/2, d/2, 0), text = "E", xoffset = -25, yoffset = 25, color = color.green, font = "sans")
label_B = label(pos = vector(-L/2, 0, d/2), text = "B", xoffset = -25, yoffset = -25, color = color.orange, font = "sans")
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos = charge.pos, shaftwidth = 0.3*size, color = color.cyan)
arrow_a = arrow(pos = charge.pos, shaftwidth = 0.3*size, color = color.magenta)

"""
 3. 物體運動部分, 當帶電粒子到達畫面最右側或撞到平行帶電板時停止
"""
while(charge.pos.x < L and abs(charge.pos.y) < d/2 - p1.height - size):
    rate(500)
# 計算帶電粒子所受合力, 在平行帶電板間才有電場、磁場
    if(-L/2 <= charge.pos.x <= L/2): F = q*(E_field + cross(charge.v, B_field))
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
# 更新時間
    t += dt
