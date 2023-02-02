from tkinter import *
from tkinter.ttk import *
import json

window = Tk()

window.title('disline Judge @ntcu by Ruki')
window.geometry('400x400')

def load():
    for i in table.get_children():
        table.delete(i)
    with open('system/question_list.json') as f:
        data = json.load(f)
    for i in data:
        for j in data[i]:
            table.insert('', 'end', values=(j['id'], j['name'], j['status']))
            
def choice():
    #創建彈出式視窗
    newWindow = Toplevel(window)
    newWindow.title()

    #獲取題目 ID
    selected_item = table.focus()
    item_details = table.item(selected_item)
    ID = item_details.get("values")[0]

    with open(f'system/questions/{ID}/questionText.txt') as f:
        question_text = f.read() #讀取題目內容
    
    with open(f'system/questions/{ID}/example.txt') as f:
        example = f.read() #讀取題目內容

    pt = Label(newWindow, text=question_text,            
			justify='left',         
			anchor='nw',            
			font=('微软雅黑',18),
            underline = -1)
    example = Label(newWindow, text=example,               	         	         
			justify='left',         
			anchor='nw',            
			font=('微软雅黑',18))

    pt.pack()
    example.pack()



table = Treeview(columns=('id', 'name', 'state'), show='headings')

table.column('id', width=100)
table.column('name', width=200)
table.column('state', width=100)

table.heading('id', text='題目編號')
table.heading('name', text='題目名稱')
table.heading('state', text='難度')

table.pack()

Button(text='題目載入', command=load).pack()
Button(text='選擇題目', command=choice).pack()


window.mainloop()
