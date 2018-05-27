"""
 VPython教學: 24-1.拉塞福散射
 日期: 2018/4/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 長度單位 nm, 質量單位 amu, 電量單位 e, 時間單位 ns
"""
r1, m1, q1, c1 = 0.4, 4, 2, color.red      # 氦原子核半徑(放大後)、質量、電量、顏色
r2, m2, q2, c2 = 1, 197, 79, color.yellow  # 金原子核半徑(放大後)、質量、電量、顏色
v0 = vector(10, 0, 0)         # 氦原子核初速度
b = 1                         # 氦原子核初速度與金原子核的垂直距離
L = 40                        # 畫面長、寬
k = 1                         # 假的靜電力常數
t = 0                         # 時間
dt = 0.001                    # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生原子核 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 arrow 物件產生表示速度、加速度用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (4) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "Rutherford Scattering", width = 800, height = 600, x = 0, y = 0, center = vector(0, 0, 0), \
               background = color.black)
# 產生原子核
alpha = sphere(pos = vector(-L/2 + r1, b, 0), radius = r1, m = m1, q = q1, v = v0, color = c1, make_trail = True)
au = sphere(pos = vector(0, 0, 0), radius = r2, m = m2, q = q2, color = c2)
# 產生表示速度、加速度的箭頭
arrow_v = arrow(pos = alpha.pos, shaftwidth = 0.5*r1, color = color.cyan)
arrow_a = arrow(pos = alpha.pos, shaftwidth = 0.5*r1, color = color.magenta)
# 繪圖部分
gd = graph(title = "Energy - Time Plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t", \
           ytitle = "red: K, green: U, blue: E")
Kt = gcurve(graph = gd, color = color.red)
Ut = gcurve(graph = gd, color = color.green)
Et = gcurve(graph = gd, color = color.blue)

"""
 3. 物體運動部分
"""
while(abs(alpha.pos.x) < L/2 and abs(alpha.pos.y) < L/2):
    rate(500)
# 計算氦原子核所受合力, 更新氦原子核加速度、速度、位置
    F = k*alpha.q*au.q / alpha.pos.mag2 * alpha.pos.norm()
    alpha.a = F/alpha.m
    alpha.v += alpha.a*dt
    alpha.pos += alpha.v*dt
# 更新表示速度、加速度的箭頭
    arrow_v.pos = alpha.pos
    arrow_a.pos = alpha.pos
    arrow_v.axis = alpha.v
    arrow_a.axis = alpha.a
# 計算氦原子核動能、系統電位能、力學能並繪圖
    K = 0.5 * alpha.m * alpha.v.mag2
    U = k * alpha.q * au.q / alpha.pos.mag
    E = K + U
    Kt.plot(pos = (t, K))
    Ut.plot(pos = (t, U))
    Et.plot(pos = (t, E))
# 更新時間
    t += dt
