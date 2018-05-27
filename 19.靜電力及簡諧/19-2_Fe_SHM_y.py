"""
 VPython教學: 19-2.靜電力造成的簡諧運動（放置在中垂線上方）
 日期: 2018/3/14
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 當 h << d 時週期理論值 7.4075 s
"""
size = 1              # 小球半徑
m = 1                 # 小球質量
q = -2E-4             # 小球電量
Q = 2E-4              # 大球電量
d = 10                # 大球之間距離的0.5倍
h = 3                 # 小球在大球連線的中垂線上的距離
k = 8.988E9           # 靜電力常數
i = 0                 # 小球回到初位置的次數
t = 0                 # 時間
dt = 0.001            # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 cylinder 物件產生星球連心線 http://www.glowscript.org/docs/VPythonDocs/cylinder.html
    (4) 用 arrow 物件產生表示速度用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (5) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "Electric Force and SHM", width = 600, height = 600, x = 0, y = 0, center = vector(0, 0, 0), \
                          background = color.black)
# 產生固定位置的大球、可移動的小球
s1 = sphere(pos = vector(-d, 0, 0), radius = size, color = color.blue)
s2 = sphere(pos = vector(d, 0, 0), radius = size, color = color.blue)
ball = sphere(pos = vector(0, h, 0), v = vector(0, 0, 0), radius = 0.4*size, color = color.red)
# 畫大球連心線、端點位置
line = cylinder(pos = s1.pos, axis = s2.pos - s1.pos, radius = 0.1*size, color = color.yellow)
top = cylinder(pos = vector(-2, h, 0), axis = vector(4, 0, 0), radius = 0.1*size, color = color.white)
bottom = cylinder(pos = vector(-2, -h, 0), axis = vector(4, 0, 0), radius = 0.1*size, color = color.white)
# 產生代表速度、加速度的箭頭
arrow_v = arrow(pos = ball.pos + vector(1, 0, 0), axis = vector(0, 0, 0), shaftwidth = 0.3*size, color = color.green)
arrow_a = arrow(pos = ball.pos + vector(2, 0, 0), axis = vector(0, 0, 0), shaftwidth = 0.3*size, color = color.magenta)
# 繪圖部分
gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "blue: y(m), green: v(m/s), magenta: a(m/s^2)")
yt = gcurve(graph = gd, color = color.blue)
vt = gcurve(graph = gd, color = color.green)
at = gcurve(graph = gd, color = color.magenta)

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
    if(ball.pos.y >= h and ball.v.y >= 0):
        print(t)
        i += 1
# 更新時間
    t += dt
