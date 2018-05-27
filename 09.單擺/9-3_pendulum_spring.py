"""
 VPython教學: 9-3.單擺 + 彈簧
 日期: 2018/4/5
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
m = 1                    # 小球質量
size = 0.2               # 小球半徑
L = 5                    # 擺長
theta0 = radians(30)     # 起始擺角, 用 radians 將單位換成 rad
theta = theta0           # 擺角
g = 9.8                  # 重力加速度
k = 10                   # 彈性常數 10 N/m
L0 = 4                   # 彈簧原長
T = 2*pi*sqrt(L/g)       # 單擺週期理論值
ratio = 0.2              # 箭頭長度與實際值的比例
t = 0                    # 時間
dt = 0.001               # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生天花板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 helix 物件產生彈簧 http://www.glowscript.org/docs/VPythonDocs/helix.html
    (4) 用 arrow 物件產生表示速度、加速度用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (5) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗、天花板、小球、彈簧
scene = canvas(title = "Pendulum with Spring", width = 600, height = 600, x = 0, y = 0, background = vector(0, 0.6, 0.6))
roof = box(pos = vector(0, L/2 + 0.05, 0), length = L, height = 0.1, width = L/2, color = color.blue)
ball = sphere(pos = vector(L*sin(theta0), L/2 - L*cos(theta0), 0), radius = size, color = color.red, make_trail = True, retain = 100)
ball.v = vector(0, 0, 0)
spring = helix(pos = vector(0, L/2, 0), axis = ball.pos - vector(0, L/2, 0), radius = 0.6*size, thickness = 0.3*size, color = color.yellow)
# 產生表示速度的箭頭
arrow_v = arrow(pos = ball.pos, axis = vector(0, 0, 0), shaftwidth = 0.3*size, color = color.green)
arrow_vx = arrow(pos = ball.pos, axis = vector(0, 0, 0), shaftwidth = 0.3*size, color = color.magenta)
arrow_vy = arrow(pos = ball.pos, axis = vector(0, 0, 0), shaftwidth = 0.3*size, color = color.orange)
# 繪圖部分
gd1 = graph(title = "position", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", \
            ytitle = "blue: r(m), red: x(m), green: y(m)")
r_t = gcurve(graph = gd1, color = color.blue)
x_t = gcurve(graph = gd1, color = color.red)
y_t = gcurve(graph = gd1, color = color.green)
gd2 = graph(title = "velocity", width = 600, height = 450, x = 0, y = 1050, xtitle = "t(s)", \
            ytitle = "blue: v(m/s), red: vx(m/s), green: vy(m/s)")
v_t = gcurve(graph = gd2, color = color.blue)
vx_t = gcurve(graph = gd2, color = color.red)
vy_t = gcurve(graph = gd2, color = color.green)
gd3 = graph(title = "acceleration", width = 600, height = 450, x = 0, y = 1500, xtitle = "t(s)", \
            ytitle = "blue: a(m/s^2), red: ax(m/s^2), green: ay(m/s^2)")
a_t = gcurve(graph = gd3, color = color.blue)
ax_t = gcurve(graph = gd3, color = color.red)
ay_t = gcurve(graph = gd3, color = color.green)

"""
 3. 物體運動部分
"""
r = ball.pos - vector(0, L/2, 0)
while(True):
    rate(1000)
# 計算小球所受合力、加速度、速度、位置, 更新彈簧長度、方向
    F = vector(0, -m*g, 0) - k*(r.mag - L0)*r.norm()
    ball.a = F/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    r = ball.pos - vector(0, L/2, 0)
    spring.axis = r
# 更新代表速度的箭頭位置、方向、長度
    arrow_v.pos = ball.pos
    arrow_vx.pos = ball.pos
    arrow_vy.pos = ball.pos
    arrow_v.axis = ball.v * ratio
    arrow_vx.axis = vector(ball.v.x, 0, 0) * ratio
    arrow_vy.axis = vector(0, ball.v.y, 0) * ratio
# 畫出位置、速度、加速度與時間關係圖
    r_t.plot(pos = (t, ball.pos.mag))
    x_t.plot(pos = (t, ball.pos.x))
    y_t.plot(pos = (t, ball.pos.y))
    v_t.plot(pos = (t, ball.v.mag))
    vx_t.plot(pos = (t, ball.v.x))
    vy_t.plot(pos = (t, ball.v.y))
    a_t.plot(pos = (t, ball.a.mag))
    ax_t.plot(pos = (t, ball.a.x))
    ay_t.plot(pos = (t, ball.a.y))
# 更新時間
    t += dt
