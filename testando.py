#-*- coding:latin1-*-
import numpy as np
import scipy.stats as spst
import scipy.optimize as spop
import scipy.interpolate as spint
import pylab
import scipy

click = 0
s = 0
soma = []
	

b=(int(raw_input("digite o numero de dias:")))+1
dia = range(1,b)


import pygtk
pygtk.require('2.0')
import gtk

def main():
	janelinha = gtk.Window()
	label = gtk.Label("Escolha entre Lucro e Funcionarios")
	botao1 = gtk.Button("Lucro")
	botao2 = gtk.Button("Concluir")
	botao3 = gtk.Button("Funcionarios")

	vbox = gtk.VBox()
	hbox = gtk.HBox()

	janelinha.add(vbox)

	vbox.add(label)
	vbox.add(hbox)

	hbox.pack_start(botao1, True, True, 3)
	"""hbox.pack_start(botao2,True,True, 3)"""
	hbox.pack_start(botao3,True,True, 3)
	
	"""def destruir(widget):
		gtk.main_quit()"""
		
	def Funcionarios(widget):
	        print "voce escolheu funcionarios."
	        label.set_text('computado')
	        global click
	        click = 0
	        gtk.main_quit()
                
	def lucro(widget):
		print 'voce escolheu lucro.'
		label.set_text('computado')
	        global click
	        click = 1
	        gtk.main_quit()
	        
	"""def fechar(widget):
		janelinha.destroy()"""

	botao1.connect('clicked',lucro)
	"""botao2.connect('clicked',destruir)"""
        botao3.connect("clicked",Funcionarios)

	

	janelinha.show_all()
	gtk.main()
	

if __name__ == '__main__':
	main()

if click==1:
        nomey = "lucro"
elif click==0:
        nomey = "funcionario"
x=0

lucro = []
print("digite quanto(s)",nomey,"a empresa registrou nos ultimos",len(dia),"dias, esse eh o numero de",nomey,"registrados ate o momento : ",x)
while x<len(dia):
        c=float(raw_input())
        s+=c
        soma.append(s)
        lucro.append(c)
        x+=1
        print "numero de",nomey,"registrados ate o momento : ",x
print ("voce ja preencheu todos os",len(dia)," espacos.")

pylab.plot (dia,lucro, color = "black", label = 'F=Diario' +str(nomey))
pylab.plot (dia, soma, color = "red", label = 'F=Soma'+str(nomey))
pylab.title (nomey)
pylab.xlabel ('dia')
pylab.legend (loc = 'upper left')
if nomey == 'lucro':
        pylab.ylabel ('lucro em R$')
else:
        pylab.ylabel ('Numeros de funcionarios')
pylab.grid (True)
pylab.show()

