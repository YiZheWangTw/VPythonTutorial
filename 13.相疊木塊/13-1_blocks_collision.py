"""
 VPython教學: 13-1.相疊的木塊完全非彈性碰撞
 Ver. 1: 2017/6/16
 Ver. 2: 2018/1/4   修改為 Python 3.X 版程式碼
 Ver. 3: 2018/2/26   增加 v-t 圖
 作者: 王一哲
"""

from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) m1 = 0.2, v1 = 0.0, m2 = 0.1, v2 = 2.0
    (2) m1 = 0.2, v1 = 1.0, m2 = 0.1, v2 = 0.0
    (3) m1 = 0.2, v1 = 0.0, m2 = 0.1, v2 = 2.5 => b2 會飛出去
    (4) m1 = 0.2, v1 = 2.0, m2 = 0.1, v2 = 0.0 => b1 到畫面右側時還沒有達到等速度
"""
d1 , h1, w1 = 1.8, 0.2, 0.2             # 下方木塊1的長度 = 1.8m, 高度 = 0.2m, 寬度 = 0.2 m
d2 , h2, w2 = 0.2, 0.2, 0.2             # 上方木塊2的長度 = 0.2m, 高度 = 0.2m, 寬度 = 0.2 m
m1, v1, c1 = 0.2, 0.0, color.red        # 下方木塊1的質量 = 0.2 kg, 初速 = 0.0 m/s, 紅色
m2, v2, c2 = 0.1, 2.0, color.green      # 上方木塊2的質量 = 0.1 kg, 初速 = 2.0 m/s, 綠色
xmax, xmin = 2.0, -2.0                  # x 軸範圍
g = 9.8                                 # 重力加速度 = 9.8 m/s^2
mu = 0.1                                # 動摩擦係數
dt = 0.0005     	                # 畫面更新的時間間隔，單位為s, 原為0.001但不夠準確, 故改為0.0005
t = 0         	                        # 模擬所經過的時間 ，單位為s，初始值為0
bx = 0      	                        # 計算 b2 初位置用的變數
i, te = 0, -1                           # 記錄 b1、b2 達到等速度經過時間用的變數

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生木塊及地板 http://vpython.org/contents/docs/box.html
    (3) 用 graph 物件產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
# 產生動畫視窗
scene = canvas(title = "Two Blocks", width = 800, height = 300, center = vector(0, 0.4, 0), background = vector(0, 0.6, 0.6))
# 產生地板
floor = box(length = (xmax - xmin), height = 0.05, width = 0.8, pos = vector(0, -h2/2.0, 0), color = color.blue)
# 產生下方木塊 b1, 位於畫面最左側 xmin + d1/2, 初速度 v1
b1 = box(length = d1, height = h1, width = w1, color = c1, pos = vector(xmin + d1/2, 0, 0))
b1.v = vector(v1, 0, 0)
# 產生上方木塊 b2, 若 v2 >= v1 則位於畫面最左側 xmin + d2/2; 若 v2 < v1, 則位於 b1 最右側 xmin + d1 - d2/2, 初速度 v2
if(v2 >= v1): bx = xmin + d2/2
else: bx = xmin + d1 - d2/2
b2 = box(length = d2, height = h2, width = w2, color = c2, pos = vector(bx, h1, 0))
b2.v = vector(v2, 0, 0)
# 繪圖部分
gd = graph(title = "E - t plot", x = 0, y = 300, width = 600, height = 450, xtitle = "t (s)", ytitle = "red: K1, green: K2, blue: E(J)")
kt1 = gcurve(graph = gd, color = c1)
kt2 = gcurve(graph = gd, color = c2)
et = gcurve(graph = gd, color = color.blue)
gd2 = graph(title = "v - t plot", x = 0, y = 750, width = 600, height = 450, xtitle = "t (s)", ytitle = "red: v1, green: v2(m/s)")
vt1 = gcurve(graph = gd2, color = c1)
vt2 = gcurve(graph = gd2, color = c2)

"""
 3. 物體運動部分, 重複執行直到: (1) b1 抵達邊緣時, (2) b2 抵達 b1 邊緣時
"""
while((b1.pos.x <= xmax - d1/2) and (b2.pos.x + d2/2 <= b1.pos.x + d1/2 + 0.001)):
#動畫執行頻率, 每秒500次
    rate(500)
#由 b1, b2 速度判斷動摩擦力量值及加速度方向, 
    if(b2.v.x > b1.v.x):
        force = mu * m2 * g
        b1.a = vector(force / m1, 0, 0)
        b2.a = vector(-force / m2, 0, 0)
    elif(b2.v.x < b1.v.x):
        force = mu * m2 * g
        b1.a = vector(-force / m1, 0, 0)
        b2.a = vector(force / m2, 0, 0)
    else:
        force = 0
        b1.a = vector(0, 0, 0)
        b2.a = vector(0, 0, 0)
# 記錄 b1、b2 達到等速度需要的時間
    if(abs(b2.v.x - b1.v.x) < 0.0005 and i == 0):
        te = t
        i = 1     
#計算 b1, b2 的速度, 位置
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
# 計算 b1, b2 動能及系統力學能, 畫能量 - 時間關係圖
    k1 = 0.5 * m1 * mag2(b1.v)
    k2 = 0.5 * m2 * mag2(b2.v)
    e = k1 + k2
    kt1.plot(pos = (t, k1))            
    kt2.plot(pos = (t, k2))
    et.plot(pos = (t, e))
# 畫速度 - 時間關係圖
    vt1.plot(pos = (t, b1.v.x))            
    vt2.plot(pos = (t, b2.v.x))
#更新時間
    t += dt
#結束 while 迴圈, 印出末速及 b1、b2 達到等速度需要的時間
print("v1 = ", b1.v.x)
print("v2 = ", b2.v.x)
print("te = ", te)
print("end")
