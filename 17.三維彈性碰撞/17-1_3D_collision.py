"""
 VPython教學: 17-1.三維彈性碰撞, m1 = m2
 日期: 2018/3/4
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
m1, r1, c1, v1 = 1, 1, color.blue, vector(8, 0, 0)     # 小球1質量, 半徑, 顏色, 初速
m2, r2, c2, v2 = 1, 1, color.red, vector(0, 0, 0)      # 小球2質量, 半徑, 顏色, 初速
L = 10            # 畫面邊長
t = 0             # 時間
dt = 0.001        # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗及小球
scene = canvas(title = "3D Collision", width = 600, height = 600, x = 0, y = 0, background = vector(0, 0.6, 0.6), range = L)
b1 = sphere(pos = vector(-L+r1, r1*(2/3), 0), m = m1, v = v1, radius = r1, color = c1, make_trail = True)
b2 = sphere(pos = vector(0, 0, 0), m = m2, v = v2, radius = r2, color = c2, make_trail = True)
# vx-t plot
gd1 = graph(title = "vx-t plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", \
           ytitle = "blue: vx1, red:vx2(m/s)")
vxt1 = gcurve(graph = gd1, color = c1)
vxt2 = gcurve(graph = gd1, color = c2)
# vy-t plot
gd2 = graph(title = "vy-t plot", width = 600, height = 450, x = 0, y = 1050, xtitle = "t(s)", \
           ytitle = "blue: vy1, red:vy2(m/s)")
vyt1 = gcurve(graph = gd2, color = c1)
vyt2 = gcurve(graph = gd2, color = c2)
# 計算撞後速度的函式
def af_col_v(v1, v2, x1, x2):
    v1_prime = v1 + dot((v2 - v1), (x1 - x2)) / mag2(x1 - x2) * (x1 - x2)
    v2_prime = v2 + dot((v1 - v2), (x2 - x1)) / mag2(x2 - x1) * (x2 - x1)
    return (v1_prime, v2_prime)

"""
 3. 物體運動部分, 小球到達畫面邊緣時停止運作
"""
# 印出撞前動能
K1 = 1/2*b1.m*b1.v.mag2
K2 = 1/2*b2.m*b2.v.mag2
print("K1 =", K1, "K2 =", K2, "K =", K1 + K2)

while(abs(b1.pos.x) < L and abs(b1.pos.y) < L and abs(b2.pos.x) < L and abs(b2.pos.y) < L):
    rate(1000)
# 更新小球位置
    b1.pos += b1.v*dt
    b2.pos += b2.v*dt
# 繪製小球 v-t 圖
    vxt1.plot(pos = (t, b1.v.x))
    vxt2.plot(pos = (t, b2.v.x))
    vyt1.plot(pos = (t, b1.v.y))
    vyt2.plot(pos = (t, b2.v.y))
# 若 b1、b2 相撞則計算撞後速度並重新指定給 v1, v2
    if(mag(b1.pos - b2.pos) <= r1 + r2 and dot((b1.pos - b2.pos), (b1.v - b2.v)) <=0 ):
        b1.v, b2.v = af_col_v(b1.v, b2.v, b1.pos, b2.pos)
        cm = sphere(pos = (b1.pos + b2.pos)/2, radius = r1/5, color = color.yellow)
# 更新時間
    t += dt

# 印出撞後動能
K1 = 1/2*b1.m*b1.v.mag2
K2 = 1/2*b2.m*b2.v.mag2
print("K1 =", K1, "K2 =", K2, "K =", K1 + K2)
