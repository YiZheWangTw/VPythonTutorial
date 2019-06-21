"""
 VPython教學: 3.等速度直線運動
 日期: 2018/2/18
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.1   # 木塊邊長
L = 1        # 地板長度
v = 0.03     # 木塊速度
t = 0        # 時間
dt = 0.01    # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生木塊及地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 顏色選項說明 http://www.glowscript.org/docs/VPythonDocs/color.html
    (4) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
scene = canvas(title = "1D Motion", width = 800, height = 600, x = 0, y = 0, center = vector(0, 0.1, 0),
               background = vector(0, 0.6, 0.6))
floor = box(pos = vector(0, 0, 0), length = L, height = size*0.1, width = L*0.5, color = color.blue)
#floor = box(pos = vec(0, 0, 0), size = vec(L, size*0.1, L*0.5), color = color.blue)
cube = box(pos = vector(-L*0.5 + size*0.5, size*0.55, 0), length = size, height = size, width = size, color = color.red)
cube.v = vector(v, 0, 0)
gd = graph(title = "x-t plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "x(m)")
gd2 = graph(title = "v-t plot", width = 600, height = 450, x = 0, y = 1050, xtitle = "t(s)", ytitle = "v(m/s)")
xt = gcurve(graph = gd, color = color.red)
vt = gcurve(graph = gd2, color = color.red)

"""
 3. 物體運動部分, 木塊到達地板邊緣時停止執行
"""
while(cube.pos.x <= L*0.5 - size*0.5):
    rate(1000)
    cube.pos.x += v*dt
    xt.plot(pos = (t, cube.pos.x))
    vt.plot(pos = (t, cube.v.x))
    t += dt

print("t = ", t)
