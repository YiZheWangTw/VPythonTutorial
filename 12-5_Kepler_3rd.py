"""
 VPython教學: 12-5.克卜勒第三行星運動定律
 Ver. 1: 2018/3/1
 Ver. 2: 2018/4/17
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 太陽及行星半徑、質量、遠日距、遠日點速率, 資料來源
    太陽 https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    地球 https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
"""
size = 2E10            # 星球半徑, 放大約2000倍, 否則會看不見
sun_m = 1988500E24     # 太陽質量
d = 1.5E11             # 地球平均軌道半徑為 1.5E11 m
v0 = 29780             # 地球公轉平均速率為 29780 m/s
eps = 10000            # 計算週期用的精準度
m = 4                  # 自訂行星 planet 軌道半徑為 m*d
ec = 0.0               # 自訂行星軌道離心率(eccentricity), 若 m != 1 時設為 0
G = 6.67408E-11        # 重力常數
t = 0                  # 時間
dt = 60*60             # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生星球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 星球的半徑要手動調整比例, 否則會看不到星球
"""
scene = canvas(title = "Kepler's Third Law of Planetary Motion", width = 600, height = 600, x = 0, y = 0, background = color.black)
# 產生太陽 sun, 地球 earth 及自訂行星 planet
sun = sphere(pos = vector(0,0,0), radius = size, m = sun_m, color = color.orange, emissive = True)
earth = sphere(pos = vector(d, 0, 0), radius = size, texture = textures.earth, make_trail = True, trail_color = color.blue, retain = 365)
earth.v = vector(0, v0, 0)
planet = sphere(pos = vector(m*(1+ec)*d, 0, 0), radius = size, color = color.red, make_trail = True, retain = 365*m)
planet.v = vector(0, v0/sqrt(m)*sqrt((1-ec)/(1+ec)), 0)
line = cylinder(pos = vector(0, 0, 0), axis = vector(m*(1+ec)*d, 0, 0), radius = 0.3*size, color = color.yellow)
# 原來的寫法為 scene.lights = [local_light(pos = vector(0,0,0), color = color.white)]
# 在 VPython 7 中 canvas.lights 無法設定為 local_light, 只能另外在太陽處放置另一個光源 lamp
lamp = local_light(pos = vector(0,0,0), color = color.white)

"""
 3. 星球運動部分
"""
while(True):
    rate(60*24)
# 計算行星加速度、更新速度、位置
    earth.a = - G*sun.m / earth.pos.mag2 * earth.pos.norm()
    earth.v += earth.a*dt
    earth.pos += earth.v*dt
    planet.a = - G*sun.m / planet.pos.mag2 * planet.pos.norm()
    planet.v += planet.a*dt
    planet.pos += planet.v*dt
# 判斷行星是否回到出發點
    if(abs(earth.pos.x - d) <= eps):
        print("t_Earth =", t)
    if(abs(planet.pos.x - m*(1+ec)*d) <= eps):
        print("t_planet =", t)
# 更新時間
    t += dt
