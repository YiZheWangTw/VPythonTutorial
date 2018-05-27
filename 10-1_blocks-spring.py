"""
 VPython教學: 10.木塊彈簧系統分離, 動量守恆
 日期: 2018/3/4
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
r1 , m1, c1 = 0.1, 0.1, color.red        # 左側木塊1的邊長 = r1*2 = 0.2 m, 質量 = 0.1 kg, 紅色
r2 , m2, c2 = 0.1, 0.2, color.green      # 右側木塊2的邊長 = r2*2 = 0.2 m, 質量 = 0.2 kg, 綠色
L, L0, k = 0.5, 1.0, 10.0                # 動畫開始時彈簧長度 = 0.5 m, 原長 = 1.0 m, 彈性常數 = 10.0 N/m
xmax, xmin = 2.0, -2.0                   # x 軸範圍
t = 0         	                         # 時間
dt = 0.0001     	                 # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html  
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 helix 物件產生彈簧 http://www.glowscript.org/docs/VPythonDocs/helix.html
    (5) 用 graph 物件產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
scene = canvas(title = "Blocks and Spring", width = 800, height = 300, center = vector(0, 0.4, 0), background = vector(0, 0.6, 0.6))
floor = box(length = (xmax - xmin), height = 0.05, width = 0.8, pos = vector(0, -r1*1.2, 0), color = color.blue)
b1 = box(length = 2*r1, width = 2*r1, height = 2*r1, color = c1, pos = vector(-L-r1, 0, 0))    # 產生左側木塊 b1
b2 = box(length = 2*r2, width = 2*r2, height = 2*r2, color = c2, pos = vector(r2, 0, 0))       # 產生右側木塊 b2
b1.v = vector(0, 0, 0)    # 左側木塊 b1 的初速度
b2.v = vector(0, 0, 0)    # 右側木塊 b2 的初速度
# 產生彈簧, 起點為 start, 終點為 end
start = b2.pos - vector(r2, 0, 0)
end = b1.pos + vector(r1, 0, 0)
spring = helix(radius = 0.5*r1, thickness = 0.3*r1, pos = start, axis = end - start, color = color.yellow)
# 畫 E-t plot
gd = graph(title = "E-t plot", x = 0, y = 300, width = 600, height = 450, xtitle = "t (s)", ytitle = "red: K1, green: K2, orange: U, cyan: E(J)")
kt1 = gcurve(graph = gd, color = c1)
kt2 = gcurve(graph = gd, color = c2)
ut = gcurve(graph = gd, color = color.orange)
et = gcurve(graph = gd, color = color.cyan)
# 畫 v-t plot
gd2 = graph(title = "v - t plot", x = 0, y = 750, width = 600, height = 450, xtitle = "t (s)", ytitle = "red: v1, green: v2(m/s)")
vt1 = gcurve(graph = gd2, color = c1)
vt2 = gcurve(graph = gd2, color = c2)
# 畫 a-t plot
gd3 = graph(title = "a - t plot", x = 0, y = 1200, width = 600, height = 450, xtitle = "t (s)", ytitle = "red: a1, green: a2(m/s^2)")
at1 = gcurve(graph = gd3, color = c1)
at2 = gcurve(graph = gd3, color = c2)

"""
 3. 物體運動部分, 當木塊抵達地板邊緣時停止
"""
while(b2.pos.x - r2 <= xmax and b1.pos.x - r1 >= xmin):
    rate(500)
# 更新彈簧的起點、終點、長度 = mag(終點 - 起點), 當長度 < 原長時代入虎克定律求回復力, 若長度 > 原長則回復力為 0
    start = b2.pos - vector(r2, 0, 0)
    end = b1.pos + vector(r1, 0, 0)
    spring.pos = start
    if(mag(end - start) < L0):
        spring.axis = end - start
        force = k*(spring.axis.mag - L0) * spring.axis.norm()
    else:
        spring.axis = vector(-L0, 0, 0)
        force = vector(0, 0, 0)
# 更新木塊的加速度、速度、位置
    b1.a = -force/m1 
    b2.a = force/m2
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
# 計算木塊的動能、系統彈性位能、力學能並畫圖
    k1 = 0.5 * m1 * b1.v.mag2
    k2 = 0.5 * m2 * b2.v.mag2
    u = 0.5 * k * (spring.axis.mag - L0)**2
    e = k1 + k2 + u
    kt1.plot(pos = (t, k1))
    kt2.plot(pos = (t, k2))
    ut.plot(pos = (t, u))
    et.plot(pos = (t, e))
# 畫 v-t 圖
    vt1.plot(pos = (t, b1.v.x))
    vt2.plot(pos = (t, b2.v.x))
# 畫 a-t 圖
    at1.plot(pos = (t, b1.a.x))
    at2.plot(pos = (t, b2.a.x))
# 更新時間
    t += dt
