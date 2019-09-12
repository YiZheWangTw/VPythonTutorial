"""
 VPython教學: 12-1.行星運動, 自訂星球速度、距離, 可更改萬有引力定律中 r 的次方
 Ver. 1: 2018/2/25
 Ver. 2: 2018/3/1
 Ver. 3: 2019/9/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
G = 6.67408E-11        # 重力常數
size = 1E10            # 星球半徑, 放大約1000倍, 否則會看不見
sun_m = 1988500E24     # 太陽質量
d = 1.5E11             # 地球平均軌道半徑為 1.5E11 m
v0 = 29290             # 地球於遠日點公轉速率為 29290 m/s
theta = radians(90)    # 速度與 +x 軸夾角, 用 radians 將單位換為 rad, 預設為 90 度
n = 2                  # 萬有引力定律中 r 的次方
t = 0                  # 時間
dt = 60*60             # 時間間隔

"""
 2. 畫面設定
"""
scene = canvas(title="Planetary Motion", width=600, height=600, x=0, y=0, background=color.black)
# 產生太陽 sun, 行星 planet
sun = sphere(pos=vec(0,0,0), radius=size, m=sun_m, color=color.orange, emissive=True)
planet = sphere(pos=vec(d, 0, 0), radius=size, texture=textures.earth, make_trail=True,
                trail_color=color.blue, trail_radius=0.1*size, v=vec(v0*cos(theta), v0*sin(theta), 0))
# 原來的寫法為 scene.lights=[local_light(pos=vec(0,0,0), color=color.white)]
# 在 VPython 7 中 canvas.lights 無法設定為 local_light, 只能另外在太陽處放置另一個光源 lamp
lamp = local_light(pos=vec(0,0,0), color=color.white)
# 產生表示速度、加速度用的箭頭
arrow_v = arrow(pos=planet.pos, axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.green)
arrow_a = arrow(pos=planet.pos, axis=vec(0, 0, 0), shaftwidth=0.3*size, color=color.magenta)
# 產生繪圖視窗
gdr = graph(title="r-t plot", width=600, height=450, x=0, y=600, xtitle="<i>t</i> (s)", ytitle="<i>r</i> (m)")
gdv = graph(title="v-t plot", width=600, height=450, x=0, y=1050, xtitle="<i>t</i> (s)", ytitle="<i>v</i> (m/s)")
gda = graph(title="a-t plot", width=600, height=450, x=0, y=1500, xtitle="<i>t</i> (s)", ytitle="<i>a</i> (m/s<sup>2</sup>")
rt = gcurve(graph=gdr, color=color.blue)
vt = gcurve(graph=gdv, color=color.green)
at = gcurve(graph=gda, color=color.magenta)

"""
 3. 星球運動部分
"""
while(True):
    rate(60*24*2)
# 更新行星加速度、速度、位置
    planet.a = -G*sun.m / planet.pos.mag**n * planet.pos.norm()
    planet.v += planet.a*dt
    planet.pos += planet.v*dt
# 更新代表速度、加速度的箭頭位置、方向、長度
    arrow_v.pos = planet.pos
    arrow_a.pos = planet.pos
    arrow_v.axis = planet.v*2E6    # 乘以 2E6 放大箭頭, 否則會看不見
    arrow_a.axis = planet.a*1E13   # 乘以 1E13 放大箭頭, 否則會看不見
# 畫出 r-t, v-t, a-t 圖
    rt.plot(pos=(t, planet.pos.mag))
    vt.plot(pos=(t, planet.v.mag))
    at.plot(pos=(t, planet.a.mag))
# 更新時間
    t += dt
