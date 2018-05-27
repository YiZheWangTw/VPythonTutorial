"""
 VPython教學: 11-6.雙星運動
 日期: 2018/3/1
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 太陽及行星半徑、質量、遠日距、遠日點速率, 資料來源
    太陽 https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    地球 https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
"""
G = 6.67408E-11
size = 2E8                 # 星球半徑
m = 1E25                   # 行星質量
n = 3                      # 另一個行星質量 M = n*m
d = 1E10                   # 1 AU = 1.5E11 m
v0 = sqrt((G*m)/((n+1)*d)) # M = n*m 行星的速率, m 行星速率為 n*v0
t = 0
dt = 60*60

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生星球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 星球的半徑要手動調整比例, 否則會看不到星球
"""
scene = canvas(title = "Binary Star", width = 600, height = 600, x = 0, y = 0, background = color.black)
# 產生行星 p1, p2, 質心 cm
cm = sphere(pos = vector(0,0,0), radius = 0.6*size, color = color.orange)
p1 = sphere(pos = vector((n*d)/(n+1), 0, 0), radius = size, color = color.blue, make_trail = True, retain = 1000)
p1.v = vector(0, n*v0, 0)
p2 = sphere(pos = vector(-d/(n+1), 0, 0), radius = size*n**(1/3), color = color.red, make_trail = True, retain = 1000)
p2.v = vector(0, -v0, 0)
line = cylinder(pos = p1.pos, axis = p2.pos - p1.pos, radius = 0.2*size, color = color.yellow)

"""
 3. 星球運動部分
"""
while(True):
    rate(60*24)
    p1.a = - G*n*m / d**2 * p1.pos.norm()
    p1.v += p1.a*dt
    p1.pos += p1.v*dt
    p2.a = - G*m / d**2 * p2.pos.norm()
    p2.v += p2.a*dt
    p2.pos += p2.v*dt
    line.pos = p1.pos
    line.axis = p2.pos - p1.pos
    t += dt
