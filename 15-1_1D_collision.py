"""
 VPython教學: 15-1.一維彈性碰撞公式
 日期: 2018/2/28
 作者: 王一哲
"""

from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) m1 = 0.5, m2 = 0.1, v1 = 1.0, v2 = 0.0
    (2) m1 = 0.2, m2 = 0.4, v1 = 1.0, v2 = -2.0
    (3) m1 = 0.4, m2 = 0.2, v1 = 2.5, v2 = -0.5
"""
d1, m1, v1, c1 = 0.2, 0.5, 1.0, color.red         # 木塊1的寬度 = 0.1 m, 質量 = 0.5 kg, 初速, 紅色
d2, m2, v2, c2 = 0.2, 0.1, 0.0, color.green      # 木塊2的寬度 = 0.1 m, 質量 = 0.1 kg, 初速, 綠色
xmax, xmin = 2.0, -2.0                            # x 軸範圍
dt = 0.0005     	                          # 畫面更新的時間間隔，單位為s, 原為0.001但能量不夠準確, 故改為0.0005
t = 0         	                                  # 模擬所經過的時間 ，單位為s，初始值為0

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvans.html
    (2) 用 box 物件產生木塊及地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 arrow 物件產生表示速度、加速度用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
    (4) 用 graph 物件產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "1 Dimension Collision", width = 800, height = 300, center = vector(0, 0.4, 0), \
               background = vector(0, 0.6, 0.6))
# 產生地板
floor = box(length = (xmax - xmin), height = 0.05, width = 0.8, pos = vector(0, -d1/2.0, 0), color = color.blue)
# 產生左側木塊 b1 並設定初速度
b1 = box(length = d1, height = d1, width = d1, color = c1, pos = vector(xmin + d1/2, 0, 0), m = m1)
b1.v = vector(v1, 0, 0)
# 產生右側木塊 b2 並設定初速度
b2 = box(length = d2, height = d2, width = d2, color = c2, pos = vector(0, 0, 0), m = m2)
b2.v = vector(v2, 0, 0)
# 繪圖部分
gd = graph(title = "v-t plot", x = 0, y = 300, widht = 600, height = 450, xtitle = "t(s)", \
           ytitle = "red: v1, green: v2(m/s)")
vt1 = gcurve(graph = gd, color = c1)
vt2 = gcurve(graph = gd, color = c2)

# 自訂函式，一維彈性碰撞速度公式
def af_col_v(m1, m2, v1, v2):
    v1_prime = (m1-m2)/(m1+m2)*v1 + (2*m2)/(m1+m2)*v2
    v2_prime = (2*m1)/(m1+m2)*v1 + (m2-m1)/(m1+m2)*v2
    return (v1_prime, v2_prime)

"""
 3. 物體運動部分, 重複執行直到木塊抵達邊緣時
"""
# 印出木塊撞前速度
print("m1=", b1.m, "m2 =", b2.m)
print(b1.v.x, b2.v.x)

while ((b2.pos.x <= xmax - d2/2) and (b1.pos.x >= xmin + d1/2)):
    rate(1000)
# 計算木塊間的距離, 若發生碰撞則計算撞後速度
    dx = b2.pos.x - b1.pos.x
    if(dx <= (d1 + d2)/2):
        b1.v.x, b2.v.x = af_col_v(b1.m, b2.m, b1.v.x, b2.v.x)
# 更新木塊的位置
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
# 畫 v-t 圖
    vt1.plot(pos = (t, b1.v.x))
    vt2.plot(pos = (t, b2.v.x))
# 更新時間
    t += dt

# 印出木塊撞後速度
print(b1.v.x, b2.v.x)
