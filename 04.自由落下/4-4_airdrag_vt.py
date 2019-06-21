"""
 VPython教學: 4-4.自由落下, 有空氣阻力, 求終端速度
 日期: 2018/3/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
m = 1        # 小球質量
h = 0        # 小球離地高度
g = 9.8      # 重力加速度 9.8 m/s^2
b = 0.3      # 空氣阻力 f = -bv
t = 0        # 時間
dt = 0.001   # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生地板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 graph 產生繪圖視窗 http://www.glowscript.org/docs/VPythonDocs/graph.html
"""
scene = canvas(title = "Free Fall", width = 600, height = 600, x = 0, y = 0, center = vector(0, h/2, 0),
               background = vector(0, 0.6, 0.6))
ball = sphere(pos = vector(0, h, 0), radius = size, color = color.red)
ball.v = vector(0, 0, 0)
ball.a = vector(0, -g, 0)
gd = graph(title = "y-t plot", width = 600, height = 450, x = 0, y = 600, xtitle = "t(s)", ytitle = "y(m)")
gd2 = graph(title = "v-t plot", width = 600, height = 450, x = 0, y = 1050, xtitle = "t(s)", ytitle = "v(m/s)")
gd3 = graph(title = "a-t plot", width = 600, height = 450, x = 0, y = 1500, xtitle = "t(s)", ytitle = "a(m/s^2)")
yt = gcurve(graph = gd, color = color.red)
vt = gcurve(graph = gd2, color = color.red)
at = gcurve(graph = gd3, color = color.red)

# 開啟檔案 4-4_airdrag_vt_data.txt, 屬性為寫入, 先寫入欄位的標題
file = open("4-4_airdrag_vt_data.txt", "w", encoding = "UTF-8")
file.write("t(s), y(m), v(m/s), a(m/s^2)\n")
tp = 0
# 設定計算終端速度用的變數
eps = 0.00001
v1 = 0

"""
 3. 物體運動部分, 小球速度變化小於 eps 時停止運作
"""
while(True):
# 更新小球受力、加速度、速度、位置，畫 y-t 及 v-t 圖
    f = -b*ball.v
    ball.a = vector(0, -g, 0) + f/m
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    yt.plot(pos = (t, ball.pos.y))
    vt.plot(pos = (t, ball.v.y))
    at.plot(pos = (t, ball.a.y))
# 每隔 0.1 秒將資料轉成字串後寫入檔案
    tc = t
    if(tc == 0 or tc - tp >= 0.1):
        file.write(str(t) + "," + str(ball.pos.y) + "," + str(ball.v.y) + "," + str(ball.a.y) + "\n")
        tp = tc
# 計算終端速度, 當 abs(v2 - v1) > eps 時將 v2 的值指定給 v1, 當 abs(v2 - v1) > eps 時結束迴圈
    v2 = ball.v.y
    if(abs(v2 - v1) > eps): v1 = v2
    else: break
# 更新時間
    t += dt

print("t =", t, "vt =", v2)
file.close() # 關閉檔案
