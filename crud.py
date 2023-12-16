import tkinter as tk
from tkinter import messagebox

def create():
  item = item_entry.get()
  if item:
    items_listbox.insert(tk.END, item)
    item_entry.delete(0, tk.END)

def read():
  selecte_item = items_listbox.curselection()
  if selecte_item:
    item = items_listbox.get(selecte_item)
    messagebox.showinfo('Selecionado', f'Dados - {item}')

def update():
  selecte_index = items_listbox.curselection()
  if selecte_index:
    new_item = item_entry.get()
    if new_item:
      items_listbox.delete(selecte_index)
      items_listbox.insert(selecte_index[0], new_item)
      item_entry.delete(0, tk.END)

def delete1():
  selecte_item = items_listbox.curselection()
  if selecte_item:
    items_listbox.delete(selecte_item)

root = tk.Tk()
root.title('CRUD')
root.geometry('350x150')

item_label = tk.Label(root, text = 'Digite o e-mail', font = ('Arial', 30))
item_label.pack()
item_entry = tk.Entry(root, width = 80)
item_entry.pack()

btn_create = tk.Button(root, text = 'Salvar', command = create)
btn_create.pack()

btn_read = tk.Button(root, text = 'Ler', command = read)
btn_read.pack()

items_listbox = tk.Listbox(root, width = 50, height = 40)
items_listbox.pack()

btn_update = tk.Button(root, text = 'Atualizar', command = update)
btn_update.pack()

btn_delete = tk.Button(root, text = 'Deletar', command = delete1)
btn_delete.pack()



root.mainloop()