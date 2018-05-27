"""
 VPython教學: 23-2.質譜儀, 用 for 迴圈自動跑完 5 種粒子
 日期: 2018/4/8
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.01                   # 粒子半徑
m = 1E-10                     # 粒子質量
q = 2E-8                      # 粒子電量
# 用 dictionary 儲存的粒子資料, 用 list 儲存的粒子名稱
masses = {"C": 12*m, "O": 16*m, "Na": 23*m, "Mg": 24*m, "Cl": 35*m}
charges = {"C": 0, "O": -2*q, "Na": q, "Mg": 2*q, "Cl": -q}
colors = {"C": color.red, "O": color.yellow, "Na": color.orange, "Mg": color.white, "Cl": color.green}
labels = {"C": "C", "O": "<sup>16</sup>O<sup>2-</sup>", "Na": "<sup>23</sup>Na<sup>+</sup>", \
          "Mg": "<sup>24</sup>Mg<sup>2+</sup>", "Cl": "<sup>35</sup>Cl<sup>-</sup>"}
particles = ["C", "O", "Na", "Mg", "Cl"]
v0 = vector(0, 10, 0)         # 粒子初速度
L = 0.4                       # 金屬板長度
B_field = vector(0, 0, -10)   # 磁場
t = 0                         # 時間
dt = 1E-5                     # 時間間隔

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 box 物件產生金屬板 http://www.glowscript.org/docs/VPythonDocs/box.html
    (3) 用 sphere 物件產生帶電粒子 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 label 產生標籤 http://www.glowscript.org/docs/VPythonDocs/label.html
"""
# 產生動畫視窗、金屬板
scene = canvas(title = "Mass Spectrometer", width = 800, height = 600, x = 0, y = 0, center = vector(0, 0, 0), \
               background = color.black)
p1 = box(pos = vector(-0.55*L, 0, 0), length = L, height = 0.01*L, width = 0.1*L, color = color.blue)
p2 = box(pos = vector(0.55*L, 0, 0), length = L, height = 0.01*L, width = 0.1*L, color = color.blue)
# 產生表示磁場的箭頭及標籤
arrow_B = arrow(pos = vector(-L/2, L/2, 0), axis = vector(0, 0, -0.1), shaftwidth = size, color = color.green)
label_B = label(pos = vector(-L/2, L/2, 0), text = "B", xoffset = 25, yoffset = 25, color = color.green, font = "sans")

"""
 3. 用 for 迴圈自動跑完 5 種粒子
"""
for name in particles:
# 產生帶電粒子
    particle = sphere(pos = vector(0, -L/3, 0), v = v0, radius = size, m = masses[name], q = charges[name], \
                      color = colors[name], make_trail = True, retain = 1000)
# 物體運動部分
    while((abs(particle.pos.x) < 0.1*size and particle.pos.y < L/2) or \
          (abs(particle.pos.x) > 0 and particle.pos.y > p1.height/2 + size)):
        rate(1000)
# 計算帶電粒子所受合力, 更新帶電粒子加速度、速度、位置
        if(particle.pos.y > p1.height/2 + size): F = particle.q*cross(particle.v, B_field)
        else: F = vector(0, 0, 0)
        particle.a = F/particle.m
        particle.v += particle.a*dt
        particle.pos += particle.v*dt
# 更新時間
        t += dt
# 粒子標籤
    particle_label = label(pos = particle.pos, text = labels[name], xoffset = 25, yoffset = 25, color = colors[name],\
                           font = "sans")
