"""
 VPython教學: 25-3.2個載流線圈產生的磁場
 Ver. 1: 2018/4/11
 Ver. 2: 2018/4/20 可調整範圍
 Ver. 3: 2019/9/19
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
delta = r             # 線圈圓心之間的距離為 2*delta
mu = 4*pi*1E-7        # 真空中的磁導率
current = 5E8         # 電流量值
direct = True         # 電流方向, True 為姆指向上, Fasle 為姆指向下, 改變 dr 計算方式
L = 40                # 畫面寬度
N = 5                 # 將顯示的空間每邊切成 N 等份
Bmax = 5              # 顯示的磁場最大值

"""
 2. 畫面設定
"""
# 產生動畫視窗及線圈
scene = canvas(title="Magnetic Field of Two Current Loops", width=600, height=600, x=0, y=0, 
               center=vec(0, 0.1*L, 0), background=color.black)
loop1 = ring(pos=vec(0, delta, 0), axis=vec(0, 1, 0), radius=r, thickness=0.2*size, color=color.blue)
loop2 = ring(pos=vec(0, -delta, 0), axis=vec(0, 1, 0), radius=r, thickness=0.2*size, color=color.blue)

# 產生串列 segs, 用 for 迴圈產生圓環分割後的小球並填入串列 segs 中
segs1, segs2 = [], []
for i in range(n):
    segs1.append(sphere(pos=vec(r*cos(i*2*pi*part/n), delta, -r*sin(i*2*pi*part/n)), radius=size, color=color.cyan))
    segs2.append(sphere(pos=vec(r*cos(i*2*pi*part/n), -delta, -r*sin(i*2*pi*part/n)), radius=size, color=color.cyan))

# 計算畫箭頭的位置並加到串列 locations 當中
locations = []
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            location = vec(L/N*i - L/2, L/N*j - L/2, L/N*k - L/2)
            locations.append(location)

# 自訂函式 magnetic, 計算某個位置的磁場
def magnetic(loc, segments):
    field = vec(0, 0, 0)
    for segment in segments:
        axis = loc - segment.pos
        if(direct): dr = norm(vec(segment.pos.z, 0, -segment.pos.x))
        else: dr = norm(vec(-segment.pos.z, 0, segment.pos.x))
        field += mu*current/(4*pi)*d*cross(dr, axis.norm())/axis.mag2
    return field

# 依序讀取串列 locations 的元素, 在對應的位置產生箭頭
fields = [arrow(pos = location, axis = vec(0, 0, 0), color = color.green) for location in locations]

# 更新箭頭的長度及方向, 若磁場量值 >= Bmax 則設定為 Bmax, 以避免箭頭蓋住其它東西
# 量值接近 Bmax 偏紅色, 量值接近 0 偏綠色
for field in fields:
    value1 = magnetic(field.pos, segs1)
    value2 = magnetic(field.pos, segs2)
    value = value1 + value2
    if(value.mag >= Bmax): value = value/value.mag * Bmax
    field.axis = value
    field.color = vec(value.mag/Bmax, 1 - value.mag/Bmax, 0)
