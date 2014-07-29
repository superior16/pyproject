# -*- coding:utf-8 -*-
 
from Tkinter import *
import sqlite3, tkMessageBox
 
class Main:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()
        Label(self.frame,text="Digite o nome da máquina").pack()
        self.nota = Entry(self.frame,width=35)
        self.nota.pack()
        Frame(height=2,bd=3,width=100,relief=SUNKEN).pack(fill=X,padx=5,pady=5)
        self.frame3 = Frame()
        self.frame3.pack()
        self.add = Button(self.frame3,text="Adicionar",command=self.adicionar)
        self.add.pack(side=LEFT)
        self.apagar = Button(self.frame3,text="Apagar",command=self.apagar)
        self.apagar.pack(side=LEFT)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        self.listbox = Listbox(master,height=20,width=50)
        self.listbox.pack()
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
         
        #criar banco
        self.conectar = sqlite3.connect("dados.txt")
        self.cur = self.conectar.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS dados(notas TEXT)")
        self.conectar.commit()
        lista = self.cur.execute("SELECT * FROM dados")
        for i in lista:
            self.listbox.insert(END,i)
    def adicionar(self):
        notas = self.nota.get()
        if notas == "":
            tkMessageBox.showwarning("error","Por favor insira uma máquina.")
        else:
            self.cur.execute("insert into dados values (?)",(notas,))
            self.conectar.commit()
            self.listbox.insert(END,notas)
    def apagar(self):
        notax = str(self.listbox.get(ACTIVE))[3:-3]
        self.cur.execute("DELETE FROM dados WHERE notas=?",(notax,))
        self.conectar.commit()
        self.listbox.delete(ANCHOR)
 
def fechar():
    if tkMessageBox.askyesno("Fechar","Deseja realmente fechar esta aplicação?"):
        exit()
    else:
        pass
root = Tk()
root.protocol("WM_DELETE_WINDOW",fechar)
root.title("INVENTÁRIO DE MÁQUINAS")
root.geometry("300x400")
Main(root)
root.mainloop()