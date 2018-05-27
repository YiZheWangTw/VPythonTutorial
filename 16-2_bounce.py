"""
 VPython教學: 16-2.自由落下三球碰撞
 日期: 2018/2/28
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) r1 = 3, m1 = 3, r2 = 2, m2 = 2, r3 = 1, m3 = 1
    (2) r1 = 1, m1 = 1, r2 = 2, m2 = 2, r3 = 3, m3 = 3
"""
r1, m1, c1 = 3, 3, color.red     # 小球1半徑, 質量, 顏色
r2, m2, c2 = 2, 2, color.green   # 小球2半徑, 質量, 顏色
r3, m3, c3 = 1, 1, color.blue    # 小球3半徑, 質量, 顏色
h = 15                   # 小球離地高度
L = 50                   # 地板邊長
g = 9.8                  # 重力加速度 9.8 m/s^2
t = 0                    # 時間
dt = 0.001               # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "Free Fall and Collision", width = 600, height = 600, x = 0, y = 0, center = vector(0, h/2, 0), \
                          background = vector(0, 0.6, 0.6), range = L)
# 產生地板
floor = box(pos = vector(0, -r1, 0), length = L, height = 0.01, width = L, texture = textures.wood)
# 產生小球並設定初速度、加速度
b1 = sphere(pos = vector(0, h, 0), radius = r1, color = c1)
b1.v, b1.a = vector(0, 0, 0), vector(0, -g, 0)
b2 = sphere(pos = vector(0, h + r1 + r2, 0), radius = r2, color = c2)
b2.v, b2.a = vector(0, 0, 0), vector(0, -g, 0)
b3 = sphere(pos = vector(0, h + r1 + 2*r2 + r3, 0), radius = r3, color = c3)
b3.v, b3.a = vector(0, 0, 0), vector(0, -g, 0)
# y-t plot
gd = graph(title = "y-t plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "red: y1, green:y2, blue: y3(m)")
yt1 = gcurve(graph = gd, color = c1)
yt2 = gcurve(graph = gd, color = c2)
yt3 = gcurve(graph = gd, color = c3)
# v-t plot
gd2 = graph(title = "v-t plot", width = 600, height = 450, x = 0, y = 1050, xtitle = "t(s)", ytitle = "red: v1, green:v2, blue: v3(m/s)")
vt1 = gcurve(graph = gd2, color = c1)
vt2 = gcurve(graph = gd2, color = c2)
vt3 = gcurve(graph = gd2, color = c3)
# 一維彈性碰撞速度公式
def af_col_v(m1, m2, v1, v2):
    v1_prime = (m1-m2)/(m1+m2)*v1 + (2*m2)/(m1+m2)*v2
    v2_prime = (2*m1)/(m1+m2)*v1 + (m2-m1)/(m1+m2)*v2
    return (v1_prime, v2_prime)

"""
 3. 物體運動部分, 小球觸地時反彈
"""
while(t < 20):
    rate(1000)
# 更新小球速度、位置
    b1.v += b1.a*dt
    b1.pos += b1.v*dt
    b2.v += b2.a*dt
    b2.pos += b2.v*dt
    b3.v += b3.a*dt
    b3.pos += b3.v*dt
# 繪製小球 y-t、v-t 圖
    yt1.plot(pos = (t, b1.pos.y))
    yt2.plot(pos = (t, b2.pos.y))
    yt3.plot(pos = (t, b3.pos.y))
    vt1.plot(pos = (t, b1.v.y))
    vt2.plot(pos = (t, b2.v.y))
    vt3.plot(pos = (t, b3.v.y))
# 若 b1 撞到地板則反彈
    if(b1.pos.y <= 0 and b1.v.y < 0): b1.v.y = -b1.v.y
# 若 b1、b2 相撞則計算撞後速度並重新指定給 vy1, vy2
    if(b2.pos.y - b1.pos.y <= r1 + r2):
        b1.v.y, b2.v.y = af_col_v(m1, m2, b1.v.y, b2.v.y)
# 若 b2、b3 相撞則計算撞後速度並重新指定給 vy2, vy3
    if(b3.pos.y - b2.pos.y <= r2 + r3):
        b2.v.y, b3.v.y = af_col_v(m2, m3, b2.v.y, b3.v.y)
# 更新時間
    t += dt
