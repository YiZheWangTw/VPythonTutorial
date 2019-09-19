"""
 VPython教學: 25-4.載流螺線管產生的磁場
 Ver. 1: 2018/4/21
 Ver. 2: 2019/9/19
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 0.4            # 螺線管截面的半徑
point_size = 0.2*size # 螺線管導線分割後標示位置用的小球半徑, 若要使小球較明顯設為1倍, 若要隱藏設為0.2倍
seg_size = 1.0*size   # 螺線管導線分割後每一小段導線的半徑, 若要使導線較明顯設為1倍, 若要隱藏設為0.2倍
r = 10                # 螺線管的半徑
n = 500               # 螺線管分割成 n 等份
num = 10              # 螺線管匝數
mu = 4*pi*1E-7        # 真空中的磁導率
current = 1E8         # 電流量值
direct = True         # 電流方向, True 為姆指向右, Fasle 為姆指向左, 改變 segment.axis 計算方式
L = 40                # 畫面寬度
N = 5                 # 將顯示的空間每邊切成 N 等份
Bmax = 5              # 顯示的磁場最大值

"""
 2. 畫面設定
"""
# 產生動畫視窗
scene = canvas(title="Magnetic Field of Current Solenoid", width=600, height=600, x=0, y=0, 
               center=vec(0, 0.1*L, 0), background=color.black)

# 產生空白串列 points, 在螺線管上等距離取點並填入 points 中
points = [sphere(pos=vec(L/2 - i*L/n, r*cos(2*pi/n*num*i), r*sin(2*pi/n*num*i)), radius=point_size, color=color.cyan) for i in range(n)]

# 產生空白串列 segs, 從 points 依序一次讀取兩個點, 計算軸向量, 中點位置, 將螺線管切成很多小圓柱並填入 segs 中
segs = []
for i in range(n-1):
    if(direct): dis = points[i+1].pos - points[i].pos
    else: dis = points[i].pos - points[i+1].pos
    mid = (points[i+1].pos + points[i].pos)/2
    segs.append(cylinder(pos = mid, axis = dis, radius = seg_size, color = color.yellow))

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
        field += mu*current/(4*pi)*segment.axis.mag*cross(segment.axis, axis.norm())/axis.mag2
    return field

# 依序讀取串列 locations 的元素, 在對應的位置產生箭頭
fields = [arrow(pos=location, axis=vec(0, 0, 0), color=color.green) for location in locations]

# 更新箭頭的長度及方向, 若磁場量值 >= Bmax 則設定為 Bmax, 以避免箭頭蓋住其它東西
# 量值接近 Bmax 偏紅色, 量值接近 0 偏綠色
for field in fields:
    value = magnetic(field.pos, segs)
    if(value.mag >= Bmax): value = value/value.mag * Bmax
    field.axis = value
    field.color = vec(value.mag/Bmax, 1 - value.mag/Bmax, 0)
