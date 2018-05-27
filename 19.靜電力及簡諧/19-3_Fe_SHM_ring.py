"""
 VPython教學: 19-3.靜電力造成的簡諧運動（圓環, 放置在中垂線上方）
 日期: 2018/3/14
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 當 h << d 時週期理論值 5.29348 s
"""
size = 0.4            # 小球半徑
m = 1                 # 小球質量
q = -2E-4             # 小球電量
Q = 8E-4              # 圓環總電量
r = 10                # 圓環的半徑
N = 100               # 圓環分割成小球的數量
dQ = Q/N              # 圓環分割後每個小球的電量
h = 3                 # 小球在星球連線的中垂線上的距離
k = 8.988E9           # 靜電力常數
j = 0                 # 小球回到初位置的次數
t = 0                 # 時間
dt = 0.001            # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 cylinder 物件產生圓環直徑連線 http://www.glowscript.org/docs/VPythonDocs/cylinder.html
    (4) 用 arrow 物件產生表示速度用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (5) 用 ring 物件產生表示圓環 http://www.glowscript.org/docs/VPythonDocs/ring.html
    (6) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "Electric Force and SHM", width = 600, height = 600, x = 0, y = 0, center = vector(0, h, 0), \
                          background = color.black)
# 產生可移動的小球
ball = sphere(pos = vector(0, h, 0), v = vector(0, 0, 0), radius = size, color = color.red)
# 產生帶電圓環及空白 list, 用 for 迴圈產生圓環分割後的小球並填入空白 list 中
Q_ring = ring(pos = vector(0, 0, 0), axis=vector(0, 1, 0), radius = r, thickness = 0.4*size, color = color.green)
charges = []
for i in range(0, N):
    charges.append(sphere(pos = vector(r*cos(i*2*pi/N), 0, r*sin(i*2*pi/N)), radius = 0.5*size, color = color.blue))
# 畫圓環直徑、小球運動端點位置
line1 = cylinder(pos = vector(-r, 0, 0), axis = vector(2*r, 0, 0), radius = 0.1*size, color = color.yellow)
line2 = cylinder(pos = vector(0, 0, -r), axis = vector(0, 0, 2*r), radius = 0.1*size, color = color.yellow)
top = cylinder(pos = vector(-2, h, 0), axis = vector(4, 0, 0), radius = 0.1*size, color = color.white)
bottom = cylinder(pos = vector(-2, -h, 0), axis = vector(4, 0, 0), radius = 0.1*size, color = color.white)
# 產生代表速度、加速度的箭頭
arrow_v = arrow(pos = ball.pos + vector(1, 0, 0), axis = vector(0, 0, 0), shaftwidth = 0.8*size, color = color.green)
arrow_a = arrow(pos = ball.pos + vector(2, 0, 0), axis = vector(0, 0, 0), shaftwidth = 0.8*size, color = color.magenta)
# 繪圖部分
gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "blue: y(m), green: v(m/s), magenta: a(m/s^2)")
yt = gcurve(graph = gd, color = color.blue)
vt = gcurve(graph = gd, color = color.green)
at = gcurve(graph = gd, color = color.magenta)

"""
 3. 物體運動部分, 小球來回 5 次時停止
"""
while(j < 5):
    rate(1000)
# 用 for 迴圈將 charges 當中的小球依序讀取出來指定給變數 charge, 計算小球的靜電力並存到變數 F
    F = vector(0, 0, 0)
    for charge in charges:
        r = ball.pos - charge.pos
        f = (k*dQ*q) / r.mag2 * r.norm()
        F += f
# 計算運動中小球的加速度、速度、位置, 畫出代表速度、加速度的箭頭
    ball.a = F/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    arrow_v.pos = ball.pos + vector(1, 0, 0)
    arrow_a.pos = ball.pos + vector(2, 0, 0)
    arrow_v.axis = ball.v
    arrow_a.axis = ball.a
# 畫出 y-t, v-t, a-t 圖
    yt.plot(pos = (t, ball.pos.y))
    vt.plot(pos = (t, ball.v.y))
    at.plot(pos = (t, ball.a.y))
# 判斷小球是否回到出發點, 計算回到出發點的次數
    if(ball.pos.y >= h and ball.v.y >=0):
        print(t)
        j += 1
# 更新時間
    t += dt
