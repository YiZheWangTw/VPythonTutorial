"""
 VPython教學: 25-1.長直載流導線產生的磁場
 Ver. 1: 2018/4/20
 Ver. 2: 2019/9/19
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
    (1) n = 100, L = 40, N = 5
    (2) n = 200, L = 80, N = 9
"""
size = 0.4            # 導線截面的半徑
n = 200               # 導線分割成 n 等份
L = 80                # 導線長度, 畫面寬度
d = L/n               # 導線分割後每段的長度
mu = 4*pi*1E-7        # 真空中的磁導率
current = 5E8         # 電流量值
direct = True         # 電流方向, True 為姆指向右, Fasle 為姆指向左, 改變 dr 計算方式
N = 9                 # 將顯示的空間每邊切成 N 等份

"""
 2. 畫面設定
"""
# 產生動畫視窗及導線
scene = canvas(title="Magnetic Field of Current Line", width=600, height=600, x=0, y=0, 
               center=vec(0, 0.1*L, 0), background=color.black)
line = cylinder(pos=vec(-0.5*L, 0, 0), axis=vec(L, 0, 0), radius=0.2*size, color=color.blue)

# 產生串列 segs, 用 for 迴圈產生導線分割後的小球並填入串列 segs 中
#segs = []
#for i in range(n+1):
#    segs.append(sphere(pos=line.pos + vec(i*d, 0, 0), radius=size, color=color.cyan))
segs = [sphere(pos=line.pos + vec(i*d, 0, 0), radius=size, color=color.cyan) for i in range(n+1)]

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
        if(direct): dr = vec(1, 0, 0)
        else: dr = vec(-1, 0, 0)
        field += mu*current/(4*pi)*d*cross(dr, axis.norm())/axis.mag2
    return field

# 依序讀取串列 locations 的元素, 在對應的位置產生箭頭
fields = []
for location in locations:
    fields.append(arrow(pos=location, axis=vec(0, 0, 0), color=color.green))

# 更新箭頭的長度及方向, 記錄磁場強度最大值, 量值接近最大值偏紅色, 量值接近 0 偏綠色
Bmax = 0
for field in fields:
    value = magnetic(field.pos, segs)
    if(value.mag >= Bmax): Bmax = value.mag
    field.axis = value

for field in fields:
    field.color = vec(field.axis.mag/Bmax, 1 - field.axis.mag/Bmax, 0)
