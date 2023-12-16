import tkinter as tk

def enviar_formulario():
  nome = entry_nome.get()
  idade = entry_idade.get()
  celular = entry_celular.get()
  email = entry_email.get()
  list.insert(tk.END, nome, idade, celular, email)


janela = tk.Tk()
janela.title('Formulario De Cadastro')
janela.geometry('500x500')

label_nome = tk.Label(janela, text='Nome:')
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_idade = tk.Label(janela, text='Idade:')
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

label_celular = tk.Label(janela, text='Celular:')
label_celular.pack()
entry_celular = tk.Entry(janela)
entry_celular.pack()

label_email = tk.Label(janela, text='Email:')
label_email.pack()
entry_email = tk.Entry(janela)
entry_email.pack()

button_enviar = tk.Button(janela, text='Enviar', command=enviar_formulario)
button_enviar.pack()

list= tk.Listbox()
list.pack()


janela.mainloop()

