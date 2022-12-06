import tkinter as tk
from tkinter import ttk

# 創建窗口
root = tk.Tk()

# 創建文本區域
text = tk.Text(root)
text.pack()

# 定義自定義 print() 函數
def my_print(string):
    text.insert('end', string)

# 使用自定義的 print() 函數顯示輸出
my_print('Hello, World!\n')
my_print('This is a test.\n')

root.mainloop()
# 執行窗口