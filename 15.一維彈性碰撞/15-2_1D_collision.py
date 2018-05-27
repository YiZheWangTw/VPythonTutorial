"""
 VPython教學: 15-2.木塊彈簧系統彈性碰撞
 Ver. 1: 2017/6/15
 Ver. 2: 2017/12/31 改為新版VPython語法
 Ver. 3: 2018/2/28 加上 v-t, a-t 圖
 作者: 王一哲
"""

from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) m1 = 0.5, m2 = 0.1, v1 = 1.0, v2 = 0.0, k = 2.0
    (2) m1 = 0.2, m2 = 0.4, v1 = 1.0, v2 = -2.0, k = 5.0
    (3) m1 = 0.4, m2 = 0.2, v1 = 2.5, v2 = -0.5
"""
d1, m1, v1, c1 = 0.2, 0.4, 2.5, color.red         # 木塊1的寬度 = 0.1 m, 質量 = 0.5 kg, 初速, 紅色
d2, m2, v2, c2 = 0.2, 0.2, -0.5, color.green       # 木塊2的寬度 = 0.1 m, 質量 = 0.1 kg, 初速, 綠色
L0, k = 0.5, 5.0                                  # 彈簧的原長 = 0.5 m, 彈性常數 = 2.0 N/m
xmax, xmin = 2.0, -2.0                            # x 軸範圍
dt = 0.0005     	                          # 畫面更新的時間間隔，單位為s, 原為0.001但能量不夠準確, 故改為0.00005
t = 0         	                                  # 模擬所經過的時間 ，單位為s，初始值為0

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvans.html
    (2) 用 box 物件產生木塊及地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 helix 物件產生彈簧 http://www.glowscript.org/docs/VPythonDocs/helix.html
    (4) 用 graph 物件產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "1 Dimension Collision", width = 800, height = 300, center = vector(0, 0.4, 0), \
               background = vector(0, 0.6, 0.6))
# 產生地板
floor = box(length = (xmax - xmin), height = 0.05, width = 0.8, pos = vector(0, -d1/2.0, 0), color = color.blue)
# 產生左側木塊 b1 並設定初速度
b1 = box(length = d1, height = d1, width = d1, color = c1, pos = vector(-L0 - 1, 0, 0), m = m1)
b1.v = vector(v1, 0, 0)
# 產生右側木塊 b2 並設定初速度
b2 = box(length = d2, height = d2, width = d2, color = c2, pos = vector(0, 0, 0), m = m2)
b2.v = vector(v2, 0, 0)
# 產生彈簧, 起點為(-d2/2.0, 0, 0), 方向為(-L0, 0, 0)
spring = helix(radius = 0.05, pos = b2.pos + vector(-d2/2.0, 0, 0), axis = vector(-L0, 0, 0), thickness = 0.03)
# 繪圖部分
gd1 = graph(title = "E-t plot", x = 0, y = 300, widht = 600, height = 450, xtitle = "t(s)", \
            ytitle = "red: K1, green: K2, orange: U, blue: E(J)")
kt1 = gcurve(graph = gd1, color = c1)
kt2 = gcurve(graph = gd1, color = c2)
ut = gcurve(graph = gd1, color = color.orange)
et = gcurve(graph = gd1, color = color.blue)
gd2 = graph(title = "v-t & a-t plot", x = 0, y = 750, widht = 600, height = 450, xtitle = "t(s)",\
            ytitle = "red: v1, green: v2(m/s); orange: a1, blue: a2(m/s^2)")
vt1 = gcurve(graph = gd2, color = c1)
vt2 = gcurve(graph = gd2, color = c2)
at1 = gcurve(graph = gd2, color = color.orange)
at2 = gcurve(graph = gd2, color = color.blue)

"""
 3. 物體運動部分, 重複執行直到木塊抵達邊緣時
    由虎克定律求彈簧的回復力 force = -k*delta_x
    為了使 force 變為向量, 需要乘以 spring.axis 的單位向量
    mag(a) = a.mag => 計算向量 a 的量值
    a / mag(a) = a.norm() => 回傳向量 a 的單位向量
"""
# 印出木塊撞前速度
print("m1=", b1.m, "m2 =", b2.m)
print(b1.v.x, b2.v.x)

while ((b2.pos.x <= xmax - d2/2) and (b1.pos.x >= xmin + d1/2)):
    rate(1000)
# 計算木塊間的距離, 更新彈簧起點位置
    dx = b2.pos.x - b1.pos.x - d1/2.0 - d2/2.0
    spring.pos = b2.pos + vector(-d2/2.0, 0, 0)
# 若木塊間的距離大於等於彈簧原長, 彈簧未被壓縮, 回復力 = 0, 木塊加速度 = 0
# 若木塊間的距離小於彈簧原長, 彈簧被壓縮, 計算彈簧回復力, 木塊加速度
    if(dx >= L0):
        spring.axis = vector(-L0, 0, 0)
        dL = 0
        b1.a = vector(0, 0, 0)
        b2.a = vector(0, 0, 0)
    else:
        spring.axis = vector(-dx, 0, 0)
        dL = L0 - dx
        force = vector(-k*dL, 0, 0)
        b1.a = force/b1.m
        b2.a = -force/b2.m
# 更新木塊速度、位置
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
# 計算木塊動能、系統彈性位能、力學能並作圖
    k1 = 0.5 * m1 * b1.v.mag2
    k2 = 0.5 * m2 * b2.v.mag2
    u = 0.5 * k * dL**2
    e = k1 + k2 + u
    kt1.plot(pos = (t, k1))
    kt2.plot(pos = (t, k2))
    ut.plot(pos = (t, u))
    et.plot(pos = (t, e))
# 畫v-t圖及a-t圖
    vt1.plot(pos = (t, b1.v.x))
    vt2.plot(pos = (t, b2.v.x))
    at1.plot(pos = (t, b1.a.x))
    at2.plot(pos = (t, b2.a.x))
# 更新時間
    t += dt

# 印出木塊撞後速度
print(b1.v.x, b2.v.x)
