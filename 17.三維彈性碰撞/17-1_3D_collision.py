"""
 VPython教學: 17-1.三維彈性碰撞, m1=m2
 Ver. 1: 2018/3/4
 Ver. 2: 2019/9/14 改成畫 px-t 及 py-t 圖
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
m1, r1, c1, v1 = 1, 1, color.blue, vec(8, 0, 0)     # 小球1質量, 半徑, 顏色, 初速
m2, r2, c2, v2 = 1, 1, color.red, vec(0, 0, 0)      # 小球2質量, 半徑, 顏色, 初速
L, t, dt = 10, 0, 0.001    # 畫面邊長, 時間, 時間間隔

"""
 2. 畫面設定
"""
# 產生動畫視窗及小球
scene = canvas(title="3D Collision", width=600, height=600, x=0, y=0, background=vec(0, 0.6, 0.6), range=L)
b1 = sphere(pos=vec(-L+r1, r1*(2/3), 0), m=m1, v=v1, radius=r1, color=c1, make_trail=True)
b2 = sphere(pos=vec(0, 0, 0), m=m2, v=v2, radius=r2, color=c2, make_trail=True)
# px-t plot
gd1 = graph(title="<i>p<sub>x</sub></i>-<i>t</i> plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i> (s)",
            ytitle="blue: <i>p<sub><i>x</i>1</sub>, red: <i>p</i><sub><i>x</i>2</sub>, green: <i>p</i><sub>x</sub></i> (kg m/s)")
px1 = gcurve(graph=gd1, color=c1)
px2 = gcurve(graph=gd1, color=c2)
px = gcurve(graph=gd1, color=color.green)
# py-t plot
gd2 = graph(title="<i>p<sub>y</sub></i>-<i>t</i> plot", width=600, height=450, x=0, y=1050, xtitle="<i>t</i> (s)",
            ytitle="blue: <i>p<sub><i>y</i>1</sub>, red: <i>p</i><sub><i>y</i>2</sub>, green: <i>p</i><sub>y</sub></i> (kg m/s)")
py1 = gcurve(graph=gd2, color=c1)
py2 = gcurve(graph=gd2, color=c2)
py = gcurve(graph=gd2, color=color.green)
# 計算撞後速度的函式
def af_col_v(v1, v2, x1, x2):
    v1_prime = v1 + dot((v2 - v1), (x1 - x2)) / mag2(x1 - x2) * (x1 - x2)
    v2_prime = v2 + dot((v1 - v2), (x2 - x1)) / mag2(x2 - x1) * (x2 - x1)
    return (v1_prime, v2_prime)

"""
 3. 物體運動部分, 小球到達畫面邊緣時停止運作
"""
# 印出撞前動能
K1 = 0.5*b1.m*b1.v.mag2
K2 = 0.5*b2.m*b2.v.mag2
print("K1 =", K1, "K2 =", K2, "K =", K1 + K2)

while(abs(b1.pos.x) < L and abs(b1.pos.y) < L and abs(b2.pos.x) < L and abs(b2.pos.y) < L):
    rate(500)
# 更新小球位置
    b1.pos += b1.v*dt
    b2.pos += b2.v*dt
# 繪製小球 p-t 圖
    px1.plot(pos=(t, b1.m*b1.v.x))
    px2.plot(pos=(t, b2.m*b2.v.x))
    px.plot(pos=(t, b1.m*b1.v.x + b2.m*b2.v.x))
    py1.plot(pos=(t, b1.m*b1.v.y))
    py2.plot(pos=(t, b2.m*b2.v.y))
    py.plot(pos=(t, b1.m*b1.v.y + b2.m*b2.v.y))
# 若 b1、b2 相撞則計算撞後速度並重新指定給 v1, v2
    if(mag(b1.pos - b2.pos) <= r1 + r2 and dot((b1.pos - b2.pos), (b1.v - b2.v)) <=0):
        b1.v, b2.v = af_col_v(b1.v, b2.v, b1.pos, b2.pos)
        cm = sphere(pos=(b1.pos + b2.pos)/2, radius=r1/5, color=color.yellow)
# 更新時間
    t += dt

# 印出撞後動能
K1 = 0.5*b1.m*b1.v.mag2
K2 = 0.5*b2.m*b2.v.mag2
print("K1 =", K1, "K2 =", K2, "K =", K1 + K2)
