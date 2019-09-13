"""
 VPython教學: 14-1.水平彈簧與小球組成的雙重簡諧運動
 Ver. 1: 2017/6/11
 Ver. 2: 2017/6/15   加上能量時間關係圖
 Ver. 3: 2018/1/4   修改為 Python 3.X 版程式碼
 Ver. 4: 2018/2/26
 Ver. 5: 2018/4/5
 Ver. 6: 2019/9/13
 作者: 王一哲
"""

from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 變數組合
    (1) m1=0.1, m2=0.2, v1=4, v2=0, k=5
    (2) m1=0.1, m2=0.2, v1=0, v2=4, k=5
    (3) m1=0.2, m2=0.1, v1=4, v2=0, k=5
    (4) m1=0.2, m2=0.1, v1=0, v2=4, k=5
"""
r1, m1, v1, c1 = 0.1, 0.1, 4, color.red      # 球1的半徑、質量、初速、顏色
r2, m2, v2, c2 = 0.1, 0.2, 0, color.green    # 球2的半徑、質量、初速、顏色
L0, k = 1.0, 5.0                             # 彈簧的原長 L0=1 m, 彈性常數 k=5.0 N/m
xmax, xmin = 2.0, 0.0                        # x 軸範圍
t, dt = 0, 0.00005     	                     # 時間, 時間間隔，原為0.001但能量不夠準確, 故改為0.00005

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Double Simple Harmonic Motion", width=800, height=300, center=vec(0, 0.4, 0),
               background=vec(0, 0.6, 0.6))
# 產生地板
floor = box(pos=vec(0, -1.2*r1, 0), size=vec(2.0*(xmax - xmin), 0.05, 0.8), color=color.blue)
# 產生左側小球 b1, 右側小球 b2 並設定初速度
b1 = sphere(pos=vec(-L0, 0, 0), radius=r1, color=c1, v=vec(v1, 0, 0))
b2 = sphere(pos=vec(0, 0, 0), radius=r2, color=c2, v=vec(v2, 0, 0))
# 產生彈簧, 起點為 b1.pos, 方向為 b2.pos - b1.pos
spring = helix(pos=b1.pos, axis=b2.pos - b1.pos, radius=0.05, thickness=0.03)
# 繪圖部分
gd = graph(title="<i>E</i> - <i>t</i> plot", x=0, y=300, width=600, height=450, xtitle="<i>t</i> (s)",
           ytitle="red: <i>K</i><sub>1</sub>, green: <i>K</i><sub>2</sub>, orange: <i>U</i>, cyan: <i>E</i> (J)")
kt1 = gcurve(graph=gd, color=c1)
kt2 = gcurve(graph=gd, color=c2)
ut = gcurve(graph=gd, color=color.orange)
et = gcurve(graph=gd, color=color.cyan)
gd2 = graph(title="<i>v</i> - <i>t</i> plot", x=0, y=750, width=600, height=450, xtitle="<i>t</i> (s)",
            ytitle="red: <i>v</i><sub>1</sub>, green: <i>v</i><sub>2</sub> (m/s)")
vt1 = gcurve(graph=gd2, color=c1)
vt2 = gcurve(graph=gd2, color=c2)

"""
 3. 物體運動部分, b2 到達地板右側邊緣時停止
    由虎克定律求彈簧的回復力 force=-k*delta_x
    為了使 force 變為向量, 需要乘以 spring.axis 的單位向量
    mag(a)=a.mag => 計算向量 a 的量值
    a / mag(a)=a.norm()=norm(a) => 回傳向量 a 的單位向量
"""
while(b2.pos.x <= xmax):
    rate(1000)
# 更新彈簧的起點位置、長度、方向
    spring.pos = b1.pos
    spring.axis = b2.pos - b1.pos
# 計算彈簧回復力，更新小球的加速度、速度、位置
    force = -k*(spring.axis.mag - L0) * spring.axis.norm()
    b1.a = -force/m1     
    b2.a = force/m2
    b1.v += b1.a * dt
    b2.v += b2.a * dt
    b1.pos += b1.v * dt
    b2.pos += b2.v * dt
# 計算小球的動能、系統彈性位能、力學能並畫圖
    k1 = 0.5 * m1 * b1.v.mag2
    k2 = 0.5 * m2 * b2.v.mag2
    u = 0.5 * k * (spring.axis.mag - L0)**2
    e = k1 + k2 + u
    kt1.plot(pos=(t, k1))
    kt2.plot(pos=(t, k2))
    ut.plot(pos=(t, u))
    et.plot(pos=(t, e))
# 畫 v-t 圖
    vt1.plot(pos=(t, b1.v.x))
    vt2.plot(pos=(t, b2.v.x))
# 更新時間
    t += dt
