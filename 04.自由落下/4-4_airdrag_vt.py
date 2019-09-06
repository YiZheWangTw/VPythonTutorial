"""
 VPython教學: 4-4.自由落下, 有空氣阻力, 求終端速度
 Ver. 1: 2018/3/8
 Ver. 2: 2019/2/2
 Ver. 3: 2019/9/6
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size=1     # 小球半徑
m=1        # 小球質量
h=0        # 小球離地高度
g=9.8      # 重力加速度 9.8 m/s^2
b=0.1      # 空氣阻力 f=-bv
c1, c2=color.red, color.green
t=0        # 時間
dt=0.0001  # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title="Free Fall", width=400, height=400, x=0, y=0, center=vec(0, h/2, 0), background=vec(0, 0.6, 0.6))

# b1 with air drag, b2 without air drag 
b1 = sphere(pos=vec(2*size, h, 0), radius=size, color=c1, v=vec(0, 0, 0), a=vec(0, -g, 0))
b2 = sphere(pos=vec(-2*size, h, 0), radius=size, color=c2, v=vec(0, 0, 0), a=vec(0, -g, 0))

gd = graph(title="y-t plot", width=400, height=300, x=0, y=400, xtitle="t(s)", ytitle="y(m)")
gd2 = graph(title="v-t plot", width=400, height=300, x=0, y=700, xtitle="t(s)", ytitle="v(m/s)")
gd3 = graph(title="a-t plot", width=400, height=300, x=0, y=1000, xtitle="t(s)", ytitle="a(m/s<sup>2</sup>)")
yt1 = gcurve(graph=gd, color=c1)
yt2 = gcurve(graph=gd, color=c2)
vt1 = gcurve(graph=gd2, color=c1)
vt2 = gcurve(graph=gd2, color=c2)
at1 = gcurve(graph=gd3, color=c1)
at2 = gcurve(graph=gd3, color=c2)

# 開啟檔案 4-4_airdrag_vt_data.csv, 屬性為寫入, 先寫入欄位的標題
file = open("data.csv", "w", encoding="UTF-8")
file.write("t(s), y1(m), y2(m), v1(m/s), v2(m/s), a1(m/s^2), a2(m/s^2)\n")
tp = 0

# 設定計算終端速度用的變數
eps = 0.0000000001
v1 = 0

"""
 3. 物體運動部分, 小球速度變化小於 eps 時停止運作
"""
while(True):
# 更新小球受力、加速度、速度、位置，畫 y-t 及 v-t 圖
    f = -b*b1.v
    b1.a = vec(0, -g, 0) + f/m
    b1.v += b1.a*dt
    b1.pos += b1.v*dt
    b2.v += b2.a*dt
    b2.pos += b2.v*dt
    yt1.plot(pos=(t, b1.pos.y))
    vt1.plot(pos=(t, b1.v.y))
    at1.plot(pos=(t, b1.a.y))
    yt2.plot(pos=(t, b2.pos.y))
    vt2.plot(pos=(t, b2.v.y))
    at2.plot(pos=(t, b2.a.y))
# 每隔 0.1 秒將資料轉成字串後寫入檔案
    tc = t
    if(tc == 0 or tc - tp >= 0.1):
        file.write(str(t) + "," + str(b1.pos.y) + "," + str(b2.pos.y) + "," + str(b1.v.y) + "," + str(b2.v.y) \
                   + "," + str(b1.a.y) + "," + str(b2.a.y) + "\n")
        tp = tc
# 計算終端速度, 當 abs(v2 - v1) > eps 時將 v2 的值指定給 v1, 當 abs(v2 - v1) > eps 時結束迴圈
    v2 = b1.v.y
    if(abs(v2 - v1) > eps): v1 = v2
    else: break
# 更新時間
    t += dt

print("t =", t, "vt =", v2)
file.close() # 關閉檔案
