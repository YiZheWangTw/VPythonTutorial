"""
 VPython教學: 25-2.載流線圈產生的磁場
 Ver. 1: 2018/4/10
 Ver. 2: 2018/4/20 可調整範圍
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.4            # 線圈截面的半徑
r = 10                # 線圈的半徑
n = 100               # 線圈分割成 n 等份
part = 1.0            # 完整的線圈 part = 1
d = 2*pi*r*part/n     # 線圈分割後每段的長度
mu = 4*pi*1E-7        # 真空中的磁導率
current = 5E8         # 電流量值
direct = True         # 電流方向, True 為姆指向上, Fasle 為姆指向下, 改變 dr 計算方式
L = 40                # 畫面寬度
N = 5                 # 將顯示的空間每邊切成 N 等份
Bmax = 5              # 顯示的磁場最大值

"""
 2. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 ring 物件產生圓環 http://www.glowscript.org/docs/VPythonDocs/ring.html
    (3) 用 sphere 物件產生小球 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (4) 用 arrow 物件產生表示磁場用的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
"""
# 產生動畫視窗及線圈
scene = canvas(title = "Magnetic Field of Current Loop", width = 600, height = 600, x = 0, y = 0, \
               center = vector(0, L/10, 0), background = color.black)
loop = ring(pos = vector(0, 0, 0), axis = vector(0, 1, 0), radius = r, thickness = 0.2*size, color = color.blue)

# 產生串列 segs, 用 for 迴圈產生圓環分割後的小球並填入串列 segs 中
segs = []
for i in range(n):
    segs.append(sphere(pos = vector(r*cos(i*2*pi*part/n), 0, -r*sin(i*2*pi*part/n)), radius = size, color = color.cyan))

# 計算畫箭頭的位置並加到串列 locations 當中
locations = []
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            location = vector(L/N*i - L/2, L/N*j - L/2, L/N*k - L/2)
            locations.append(location)

# 自訂函式 magnetic, 計算某個位置的磁場
def magnetic(loc, segments):
    field = vector(0, 0, 0)
    for segment in segments:
        axis = loc - segment.pos
        if(direct): dr = norm(vector(segment.pos.z, 0, -segment.pos.x))
        else: dr = norm(vector(-segment.pos.z, 0, segment.pos.x))
        field += mu*current/(4*pi)*d*cross(dr, axis.norm())/axis.mag2
    return field

# 依序讀取串列 locations 的元素, 在對應的位置產生箭頭
fields = []
for location in locations:
    fields.append(arrow(pos = location, axis = vector(0, 0, 0), color = color.green))

# 更新箭頭的長度及方向, 若磁場量值 >= Bmax 則設定為 Bmax, 以避免箭頭蓋住其它東西
# 量值接近 Bmax 偏紅色, 量值接近 0 偏綠色
for field in fields:
    value = magnetic(field.pos, segs)
    if(value.mag >= Bmax): value = value.norm() * Bmax
    field.axis = value
    field.color = vector(value.mag/Bmax, 1 - value.mag/Bmax, 0)
