from Tkinter import *
import random
class Janela:
	def __init__(self,toplevel):
		self.first = Frame(toplevel)
		self.first2 = Frame(toplevel)
		self.first3 = Frame(toplevel)
		self.first.pack()
		self.first2.pack()
		self.first3.pack()

		self.botao=Button(self.first3, text='aperte aqui',background='green')
		self.botao.bind("<Button-1>",self.troca)
		self.botao.pack()
		
		self.texto=Label(self.first, text='Esses sao alunos')
		self.texto.pack()

		self.botao4=Button(self.first2, text='jonatas',background='blue')
		self.botao1=Button(self.first2, text='heroi',background='gray')
		self.botao2=Button(self.first, text='moral',background='red')
		self.botao3=Button(self.first, text='Van dame',background='purple')
		
		self.botao2.pack(side=LEFT)
		self.botao4.pack(side=RIGHT)
		self.botao1.pack(side=RIGHT)
		self.botao3.pack(side=LEFT)
	def troca(self,Button):
		self.botao1['background']=random.choice(lista)
		self.botao2['background']=random.choice(lista)
		self.botao3['background']=random.choice(lista)
		self.botao4['background']=random.choice(lista)
lista=[]
lista=['green','red','blue','gray','yellow','pink','purple']
raiz=Tk()
Janela(raiz)
raiz.mainloop()