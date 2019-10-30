"""
 VPython教學: 5-5.水平抛射, 用for迴圈改變h, 記錄t、R
 Ver. 1: 2018/3/21
 Ver. 2: 2018/6/13  加上用 matplotlib.pyplot 繪圖的部分
 Ver. 3: 2019/10/10 改用 with 開啟檔案, 上課用的版本
 作者: 王一哲
"""
from vpython import *
import matplotlib.pyplot as plt

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1     # 小球半徑
v0 = 5       # 小球水平初速
L = 50       # 地板長度
g = 9.8      # 重力加速度 9.8 m/s^2
dt = 0.001   # 時間間隔
data_y, data_x = [], []     # 儲存繪圖資料的串列

"""
 2. 畫面設定
"""
scene = canvas(title="Projectile", width=800, height=600, x=0, y=0, center=vec(0, 5, 0), background=vec(0, 0.6, 0.6))
floor = box(pos=vec(0, -size, 0), size=vec(L, 0.01, 10), texture=textures.metal)

# 開啟檔案 5-5_data.csv, 屬性為寫入, 先寫入欄位的標題
with open("5-5_data.csv", "w", encoding="UTF-8") as file:
    file.write("h(m), t(s), R(m)\n")

"""
 3. 主程式
"""
def main(h):
    t = 0
    ball = sphere(pos=vec(-L/2, h, 0), radius=size, texture=textures.wood, make_trail=True,
                  v=vec(v0, 0, 0), a=vec(0, -g, 0))
    while ball.pos.y - floor.pos.y > size + 0.5*floor.height:
        ball.v += ball.a*dt
        ball.pos += ball.v*dt
        t += dt
    return t, ball.pos.x + L/2

"""
 4. 用for迴圈改變h, 計算t、R, 寫入檔案
"""
for h in range(5, 51, 1):
    t, r = main(h)
    with open("5-5_data.csv", "a", encoding="UTF-8") as file:
        file.write(str(h) + "," + str(t) + "," + str(r) + "\n")
    data_y.append(t)
    data_x.append(h)

# 用 matplotlib.pyplot 繪圖
plt.figure(figsize=(8, 6), dpi=100)                   # 設定圖片尺寸
plt.xlabel(r'$h ~\mathrm{(m)}$', fontsize=16)         # 設定坐標軸標籤
plt.ylabel(r'$t ~\mathrm{(s)}$', fontsize=16)
plt.xticks(fontsize=12)                               # 設定坐標軸數字格式
plt.yticks(fontsize=12)
plt.grid(color='red', linestyle='--', linewidth=1)    # 設定格線顏色、種類、寬度
plt.plot(data_x, data_y, marker='o', markerfacecolor='blue', markersize=8, color='skyblue', linewidth=3)   # 繪圖並設定線條顏色、寬度
plt.savefig('t-h_plot.svg')                           # 儲存圖片
plt.savefig('t-h_plot.png')
plt.show()                                            # 顯示圖片
