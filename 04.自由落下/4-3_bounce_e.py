"""
 VPython教學: 4-3.自由落下, 小球觸地時反彈, 恢復係數為e
 日期: 2018/2/19
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
e = 0.9      # 恢復係數
i = 0        # 小球撞地板次數
N = 20       # 小球撞地板次數上限, 到達上限後停止運作
h = 15       # 小球離地高度
g = 9.8      # 重力加速度 9.8 m/s^2
t = 0        # 時間
dt = 0.001   # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
scene = canvas(title = "Free Fall", width = 600, height = 600, x = 0, y = 0, center = vector(0, h/2, 0), \
                          background = vector(0, 0.6, 0.6))
floor = box(pos = vector(0, 0, 0), length = 40, height = 0.01, width = 10, color = color.blue)
ball = sphere(pos = vector(0, h, 0), radius = size, color = color.red)
ball.v = vector(0, 0, 0)
ball.a = vector(0, -g, 0)
gd = graph(title = "plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "blue: y(m), red: v(m/s)")
yt = gcurve(graph = gd, color = color.blue)
vt = gcurve(graph = gd, color = color.red)

"""
 3. 物體運動部分, 小球觸地時反彈
"""
while(i < N):
    rate(1000)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    yt.plot(pos = (t, ball.pos.y))
    vt.plot(pos = (t, ball.v.y))
    if(ball.pos.y <= size + floor.height/2 and ball.v.y < 0):
        ball.v.y = -ball.v.y*e
        i += 1
    t += dt

print("i = ", i)
print("t = ", t)
