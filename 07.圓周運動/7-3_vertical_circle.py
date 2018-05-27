"""
 VPython教學: 7-3.鉛直面圓周運動
 日期: 2018/3/30
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.5            # 小球半徑
R = 5                 # 圓周運動半徑
g = 9.8               # 重力加速度 9.8 m/s^2
v0 = 1*sqrt(g*R)      # 小球初速, 1 ~ 7 sqrt(g*R)
ratio = 0.1           # 速度, 加速度箭頭長度與實際的比例
i = 0                 # 小球回到出發點的次數
t = 0                 # 時間
dt = 0.0001           # 時間間隔, 取 0.0001 以降低誤差

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 cylinder 物件產生圓心及繩子 http://www.glowscript.org/docs/VPythonDocs/cylinder.html
    (4) 用 arrow 物件產生表示速度及加速度的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (5) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
scene = canvas(title = "Vertical Circle", width = 600, height = 600, x = 0, y = 0, background = color.black)
ball = sphere(pos = vector(0, R, 0), radius = size, color = color.red, make_trail = True, retain = 100)
ball.v = vector(-v0, 0, 0)
center = cylinder(pos = vector(0, 0, -size), axis = vector(0, 0, 2*size), radius = 0.1*size, color = color.white)
rope = cylinder(pos = vector(0, 0, 0), axis = ball.pos, radius = 0.1*size, color = color.yellow)
arrow_v = arrow(pos = ball.pos, axis = vector(0, 0, 0), radius = 0.2*size, shaftwidth = 0.4*size, color = color.green)
arrow_a = arrow(pos = ball.pos, axis = vector(0, 0, 0), radius = 0.2*size, shaftwidth = 0.4*size, color = color.blue)
gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "green: v(m/s), red: at(m/s^2), blue: an(m/s^2)")
vt_plot = gcurve(graph = gd, color = color.green)
at_plot = gcurve(graph = gd, color = color.red)
an_plot = gcurve(graph = gd, color = color.blue)

"""


 3. 自訂函式, findan 計算法線加速度, findat 計算切線加速度
"""
def findan(v, pos):
    an = -v.mag2 / R * pos.norm()
    return an

def findat(pos):
    x = pos.x
    y = pos.y
    r = sqrt(x**2 + y**2)
    sintheta = abs(x)/r
    costheta = abs(y)/r
    absat = g*sintheta
    aty = -absat*sintheta
    if((x <= 0 and y <= 0) or (x >=0 and y>= 0)):
        atx = +absat*costheta
    elif((x <= 0 and y >= 0) or (x >= 0 and y <= 0)):
        atx = -absat*costheta
    at = vector(atx, aty, 0)
    return at

"""
 4. 物體運動部分, 小球回到出發點 5 次停止運作
"""
while(i < 5):
# 由於 dt 較小，每秒計算 5000 次使動畫速度加快
    rate(5000)
# xp 是小球原來的位置, xc 是小球現在的位置, 用來判斷小球是否回到出發點    
# 計算小球 an, at, 更新加速度, 速度, 位置
    xp = ball.pos.x
    an = findan(ball.v, ball.pos)
    at = findat(ball.pos)
    ball.a = an + at
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    xc = ball.pos.x
    rope.axis = ball.pos
# 若小球回到出發點, 將 i 加 1, 印出時間 t, 由於誤差會累積, 取第一次回到出發點的時間作為週期
    if(xp > 0 and xc < 0):
        i += 1
        print(i, t)
# 更新代表速度, 加速度的箭頭
    arrow_v.pos = ball.pos
    arrow_v.axis = ball.v * ratio
    arrow_a.pos = ball.pos
    arrow_a.axis = ball.a * ratio
# 更新 v-t, at-t, an-t 圖
    vt_plot.plot(t, ball.v.mag)
    at_plot.plot(t, at.mag)
    an_plot.plot(t, an.mag)
# 更新時間
    t += dt
