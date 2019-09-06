# Python基本語法

> 作者：王一哲
> 日期：2018/3/6

<br />

## 判斷條件：if

最簡單的語法為

```python
if(條件):
    條件成立時執行的程式碼
```

當條件成立時執行冒號下的程式碼，程式碼必須從 if 的位置開始縮排，假設使用的縮排為 4 個空格，則在條件成立時要執行的程式碼每行都要縮排 4 個空格，若某一行沒有縮排，從此行開始會被視為 if 的部分已經結束。如果條件成立時執行的程式碼只有一行，可以直接放在冒號之後不需換行。

如果要加上條件不成立時執行的程式碼，語法為

```python
if(條件):
    條件成立時執行的程式碼
else:
    條件不成立時執行的程式碼
```

<img style="display: block; margin-left: auto; margin-right: auto" height="50%" width="50%" src="https://i.imgur.com/U9pZTof.png">
<div style="text-align:center">if … else … 流程圖</div>
<br />

如果條件不只有一個，可以使用多層的 if，語法為

```python
if(條件1):
    條件1成立時執行的程式碼
elif(條件2):
    條件1不成立、條件2成立時執行的程式碼
else:
    條件1、2皆不成立時執行的程式碼
```

<img style="display: block; margin-left: auto; margin-right: auto" height="80%" width="80%" src="https://i.imgur.com/GwFGMDg.png">
<div style="text-align:center">if … elif … else … 流程圖</div>
<br />


## 程式 2-1：if 的使用方法

```python=
a = int(input("a = "))
b = int(input("b = "))

if(a > b):
    print("a > b")
else:
    print("a <= b")

if(a > b):
    print("a > b")
elif(a == b):
    print("a = b")
else:
    print("a < b")
```

執行時先由使用者用鍵盤輸入 a、b 的值，由於輸入的資料會被視為字串，加上 int 將字串轉換為整數。雖然 Python 在輸入的資料看起來很像數字時，會自動將輸入的資料格式轉換為數字，但是加上 int 強制轉換為數字是比較保險的作法。第一個 if 是：當 a > b 時印出文字 a > b，若條件不成立則印出文字 a <= b。第二個 if 是：當 a > b 時印出文字 a > b，當 a == b 時印出文字 a = b，若條件不成立則印出文字 a < b。

在 Python、C、C++及大部分的程式語言當中，**等號 = 用來指定數值給變數**，例如 a = 2 是將 2 這個數值指定給變數 a；**若要比較兩個變數是否相等，要使用 ==**，這與數學式子的寫法不相同，需要適應一下。
<br />

## 重複執行：while 迴圈

在程式語言當中經常會重複執行某一段程式碼，這樣的語法稱為**迴圈(loop)**，其中一種迴圈稱為 **while**，語法為

```python
while(條件):
    條件成立時執行的程式碼
```

當條件成立時執行冒號下的程式碼，一直重複執行到條件不成立時為止。條件成立時執行的程式碼一樣要注意程式碼縮排的空格數。while 迴圈的流程圖如下

<img style="display: block; margin-left: auto; margin-right: auto" height="50%" width="50%" src="https://i.imgur.com/onwukK4.png">
<div style="text-align:center">while 迴圈流程圖</div>
<br />


## 程式 2-2：while 的使用方法

```python=
result = 0
i = 1
n = 10

while(i <= n):
    print("i = ", i)
    result += i
    i += 1

print("result = ", result)
```

先定義變數 i、n、result 指定數值。當 i <= n 時執行 while 迴圈中的程式碼，印出 i 的數值、將 result 的數值 +i 並重新指定給 result，將 i 數值 +1 並重新指定給 i。當 while 迴圈執行完之後印出文字 result = 以及 result 的數值。這個程式是用來計算 1 + 2 + 3 + … + 10 = ?

> 問題：如果想計算的是 1 + 3 + 5 + 7 +  9 = ? 要怎麼寫呢？（提示：只要改一個地方即可。）

<br />

## 重複執行：for 迴圈

Python 的 for 迴圈和其它的程式語言很不一樣，比較像是用來從一串資料中依序讀取當中的元素來運算，經常搭配 range 或串列(list)資料一起使用。以搭配 range 為例

```python
for i in range(5):
    print(i)
```

range是用來產生數列的函式，格式為
```python
range(起始值, 結束值, 增量)
```
起始值預設為0，增量預設為1，但產生的數列不包含結束值。因此上面的程式碼執行時，會將 ragne(5) 產生的數列 (0, 1, 2, 3, 4) 依序讀取出來並指定給變數 i，最後將印出 i 的數值，因此執行結果為

```python
0
1
2
3
4
```

<img style="display: block; margin-left: auto; margin-right: auto" height="50%" width="50%" src="https://i.imgur.com/vG3fbS8.png">
<div style="text-align:center">for 迴圈流程圖</div>
<br />


## 程式 2-3：for 的使用方法

```python=
result = 0

for i in range(1, 11):
    result += i

print("result = ", result)
```

這個程式和程式 2-2 一樣是用來計算 1 + 2 + 3 + … + 10 = ?


> 問題：如果想計算的是 1 + 3 + 5 + 7 +  9 = ? 要怎麼寫呢？（提示：只要改一個地方即可。）

<br />

## 結語

Python 的功能非常多，但是我們的目標是利用 VPython 做物理模擬動畫，我們只需要 if、while、for 再加上一些儲存資料的容器就夠用了，在之後的動畫教學中會慢慢介紹更多不同的格式。

---

###### tags: `VPython`
