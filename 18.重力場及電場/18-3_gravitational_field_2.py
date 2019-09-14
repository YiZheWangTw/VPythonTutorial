"""
 VPython教學: 18-3. 重力場, 2個星球, 自行調整距離
 Ver. 1: 2018/3/2
 Ver. 2: 2019/9/14 箭頭的顏色隨著量值改變
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值, 太陽及行星半徑、質量、遠日距、遠日點速率, 資料來源
"""
radius = {"Mercury": 2439700, "Venus": 6051800, "Earth": 6371000, "Mars": 3389500, "Sun": 696392000}
mass = {"Mercury": 0.33011E24, "Venus": 4.8675E24, "Earth": 5.9723E24, "Mars": 0.64171E24, "Sun": 1988500E24}
G = 6.67408E-11   # 重力常數
N = 5             # 將顯示的空間每邊切成 N 等份

"""
 2. 產生行星類別, 回傳行星產生的重力場
"""
class planet_c(sphere):
    def g(self, pos):
        return -G*self.m / mag2(pos-self.pos) * norm(pos-self.pos)

"""
 3. 畫面設定
"""
# 產生動畫視窗
d = 2E7
L = 2*d
scene = canvas(title="Gravitatinoal Field", width=600, height=600, x=0, y=0, background=color.black, range=L)

# 產生地球及火星
earth = planet_c(pos=vec(-d/2, 0, 0), radius=radius["Earth"], m=mass["Earth"], texture=textures.earth)
mars = planet_c(pos=vec(d/2, 0, 0), radius=radius["Mars"], m=mass["Mars"], color=color.red)

# 計算畫箭頭的位置, 如果不在地球或火星內則加到串列 locations 當中
locations = []
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            location = vec(L/N*i - L/2, L/N*j - L/2, L/N*k - L/2)
            if(mag(location-earth.pos) > earth.radius and mag(location-mars.pos) > mars.radius):
                locations.append(location)

# 依序讀取串列 locations 的元素, 在對應的位置產生箭頭
fields = []
for location in locations:
    fields.append(arrow(pos=location, axis=vec(0, 0, 0), color=color.green))

# 更新箭頭的長度及方向, 長度乘以 1E6 才能看見, 記錄重力場強度最大值, 量值接近最大值偏紅色, 量值接近 0 偏綠色
fmax = 0
for field in fields:
    field.axis = (earth.g(field.pos) + mars.g(field.pos))*1E6
    if(field.axis.mag >= fmax): fmax = field.axis.mag

for field in fields:
    field.color = vec(field.axis.mag/fmax, 1 - field.axis.mag/fmax, 0)
