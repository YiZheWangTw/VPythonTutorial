"""
 VPython教學: 12-2.行星運動, 用dictionary 儲存星球資料
 日期: 2018/2/25
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 太陽及行星半徑、質量、遠日距、遠日點速率, 資料來源
    太陽 https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    水星 https://nssdc.gsfc.nasa.gov/planetary/factsheet/mercuryfact.html
    金星 https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
    地球 https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
    火星 https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html
"""
# 用 dictionary 儲存星球資料, 半徑 radius, 質量 mass, 遠日距 d_at_aphelion, 於遠日點的速率 v_at_aphelion
radius = {"Mercury": 2439700, "Venus": 6051800, "Earth": 6371000, "Mars": 3389500, "Sun": 696392000}
mass = {"Mercury": 0.33011E24, "Venus": 4.8675E24, "Earth": 5.9723E24, "Mars": 0.64171E24, "Sun": 1988500E24}
d_at_aphelion = {"Mercury": 6982E7, "Venus": 10894E7, "Earth": 15210E7, "Mars": 24923E7}
v_at_aphelion = {"Mercury": 38860, "Venus": 34790, "Earth": 29290, "Mars": 21970}
G = 6.67408E-11       # 重力常數
eps = 10000           # 精準度
t = 0                 # 時間
dt = 60*60            # 時間間隔


"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生星球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 星球的半徑要手動調整比例, 否則會看不到星球
"""
scene = canvas(title = "Planetary Motion", width = 600, height = 600, x = 0, y = 0, background = color.black)
# 產生太陽 sun, 地球 earth 及火星 mars
sun = sphere(pos = vector(0,0,0), radius = radius["Sun"]*20, m = mass["Sun"], color = color.orange, emissive = True)
earth = sphere(pos = vector(d_at_aphelion["Earth"], 0, 0), radius = radius["Earth"]*2E3, m = mass["Earth"], \
               texture = textures.earth, make_trail = True, trail_color = color.blue, retain = 365)
earth.v = vector(0, v_at_aphelion["Earth"], 0)
mars = sphere(pos = vector(d_at_aphelion["Mars"], 0, 0), radius = radius["Mars"]*2E3, m = mass["Mars"], \
              color = color.red, make_trail = True, retain = 365)
mars.v = vector(0, v_at_aphelion["Mars"], 0)
# 原來的寫法為 scene.lights = [local_light(pos = vector(0,0,0), color = color.white)]
# 在 VPython 7 中 canvas.lights 無法設定為 local_light, 只能另外在太陽處放置另一個光源 lamp
lamp = local_light(pos = vector(0,0,0), color = color.white)

"""
 3. 星球運動部分
"""
while(True):
    rate(60*24)
# 更新行星加速度、速度、位置
    earth.a = - G*sun.m / earth.pos.mag2 * earth.pos.norm()
    earth.v += earth.a*dt
    earth.pos += earth.v*dt
    mars.a = - G*sun.m / mars.pos.mag2 * mars.pos.norm()
    mars.v += mars.a*dt
    mars.pos += mars.v*dt
# 判斷行星是否回到遠日點, 若回到出發點則顯示經過的時間
    if(abs(earth.pos.x - d_at_aphelion["Earth"]) <= eps):
        print("t_Earth =", t)
    if(abs(mars.pos.x - d_at_aphelion["Mars"]) <= eps):
        print("t_Mars =", t)
# 更新時間
    t += dt
