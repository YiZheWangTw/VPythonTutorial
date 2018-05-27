"""
 VPython教學: 18-4. 電場, 2個球狀帶電體
 日期: 2018/3/2
 作者: 王一哲
"""
from vpython import *

"""
 1. 參數設定, 設定變數及初始值
"""
size = 1                 # 帶電球體半徑
d = 10                   # 帶電球體連心線距離
L = 1.8*d                # 畫面寬度
q1, c1 = 5, color.blue   # 帶電球體1電量、顏色
q2, c2 = -1, color.red   # 帶電球體2電量、顏色
ke = 8.989E9             # 靜電力常數
N = 6                    # 將顯示的空間每邊切成 N 等份

"""
 2. 產生帶電球體類別, 回傳帶電球體產生的電場
"""
class ball_c(sphere):
    def charge(self, charge):
        self.charge = charge
    def electric(self, pos):
        return ke*self.charge / mag2(pos - self.pos) * norm(pos - self.pos)

"""
 3. 畫面設定
    (1) 用 canvas 物件作為顯示動畫用的視窗 http://www.glowscript.org/docs/VPythonDocs/canvas.html
    (2) 用 sphere 物件產生帶電球體 http://www.glowscript.org/docs/VPythonDocs/sphere.html
    (3) 用 arrow 物件產生表示電場的箭頭 http://www.glowscript.org/docs/VPythonDocs/arrow.html
"""

# 產生動畫視窗
scene = canvas(title = "Electric Field", width = 600, height = 600, x = 0, y = 0, background = color.black, range = L)

# 產生帶電球體1、2
b1 = ball_c(pos = vector(-d/2, 0, 0), radius = size, color = c1, charge = q1)
b2 = ball_c(pos = vector(d/2, 0, 0), radius = size, color = c2, charge = q2)

# 計算畫箭頭的位置, 如果不在帶電球體內則加到串列 locations 當中
locations = []
for i in range(N+1):
    for j in range(N+1):
        for k in range(N+1):
            location = vector(L/N*i - L/2, L/N*j - L/2, L/N*k - L/2)
            if(mag(location - b1.pos) > 2*size and mag(location - b2.pos) > 2*size):
                locations.append(location)

# 依序讀取串列 locations 的元素, 在對應的位置產生箭頭
fields = []
for location in locations:
    fields.append(arrow(pos = location, axis = vector(0, 0, 0), color = color.green))

# 更新箭頭的長度及方向, 長度乘以 1E-9 才不會太長
for field in fields:
    field.axis = (b1.electric(field.pos) + b2.electric(field.pos))*1E-9
