import tkinter as tk
from tkinter import ttk

# 創建窗口
root = tk.Tk()

# 創建下拉式表單
combo = ttk.Combobox(root, values=['Option 1', 'Option 2', 'Option 3'])
combo.pack()

# 設置事件處理程序
def handle_selection(event):
    # 取得選擇的值
    value = combo.get()
    print('Selected value:', value)

# 綁定事件
combo.bind('<<ComboboxSelected>>', handle_selection)

# 執行窗口
root.mainloop()
