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
            

table = Treeview(columns=('id', 'name', 'state'), show='headings')

table.column('id', width=100)
table.column('name', width=200)
table.column('state', width=100)

table.heading('id', text='題目編號')
table.heading('name', text='題目名稱')
table.heading('state', text='難度')

table.pack()

Button(text='題目載入', command=load).pack()

window.mainloop()
