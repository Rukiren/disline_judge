import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from system.compiler_c import cppCompiler
from system.compiler_py import pythonCompiler
from system.questionOut import printQuestion

filepath = None
language = None

def handle_selection(event):
    text.delete('1.0', 'end')
    # 取得選擇的值
    question = question_selector.get()
    try:
        # 使用 printQuestion() 函數顯示題目和示例
        question_txt, question_test = printQuestion(question=question)
        my_print(question_txt)
        my_print(question_test)
    except:
        my_print("題目不存在\n")
        return

    # 創建文件選擇對話框
    filepath = filedialog.askopenfilename()
    
    # 選擇語言
    language.bind('<<ComboboxSelected>>', lambda event: handle_language_selection(event, language, filepath, question))

    

def handle_language_selection(event, language, filepath, question):
    
    # 取得選擇的值
    language = language.get()

    if language == 'C/C++':
        state, ans, out, err = cppCompiler(question=question, test=filepath)
    elif language == "python" :
        state, ans, out, err = pythonCompiler(question=question, test=filepath)
    my_print(state)
    my_print(err)


# 創建窗口
root = tk.Tk()

# 創建文本區域
text = tk.Text(root)
text.pack()

# 定義自定義 print() 函數
def my_print(string):
    text.insert('end', string)

# 定義全局變量
question = None


# 創建下拉式表單
question_selector = ttk.Combobox(root, values=['1', '2', '3'])
question_selector.pack()
language = ttk.Combobox(root, values=['python', 'C/C++'])
language.pack()
# 綁定事件
question_selector.bind('<<ComboboxSelected>>', handle_selection)
question_selector.mainloop()
root.mainloop()