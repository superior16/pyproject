#-*-coding: latin1-*-
import pygtk
pygtk.require('2.0')
import gtk
import sqlite3





class progm(object):


    def __init__(self):

        self.conectar = sqlite3.connect("dadosfunc.db")
        self.cur= self.conectar.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS dadosfunc(nome TEXT, cargo TEXT ,carteira TEXT)")
        self.conectar.commit()

        self.conectar = sqlite3.connect("dadosmaq.db")
        self.cur= self.conectar.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS dadosmaq( TEXT)")
        self.conectar.commit()

        builder= gtk.Builder()
        builder.add_from_file("pjt.glade")

        self.window= builder.get_object("window1")
        self.window.show_all()


        self.window2= builder.get_object("window2")
        self.window3= builder.get_object("window3")
        self.window4= builder.get_object("window4")
        self.window5= builder.get_object("window5")
        self.window6= builder.get_object("window6")
        self.window7= builder.get_object("window7")

        self.but1= builder.get_object("button1")
        self.but1.connect("clicked",self.func,)

        self.but2= builder.get_object("button2")
        self.but2.connect("clicked",self.mqna,)

        self.but3= builder.get_object("button3")
        self.but3.connect("clicked",self.cpta,)

        self.but4= builder.get_object("button4")
        self.but4.connect("clicked",self.gfco,)

        self.but5= builder.get_object("button5")
        self.but5.connect("clicked",self.delete_event2,)

        self.but6= builder.get_object("button6")
        self.but6.connect("clicked",self.cad_func,)

        self.but10= builder.get_object("button10")
        self.but10.connect("clicked",self.hide_event,)

        self.but11= builder.get_object("button11")
        self.but11.connect("clicked",self.cad_mqna,)

        self.but15= builder.get_object("button15")
        self.but15.connect("clicked",self.hide_event2,)

        self.but19= builder.get_object("button19")
        self.but19.connect("clicked",self.hide_event3,)

        self.but23= builder.get_object("button23")
        self.but23.connect("clicked",self.hide_event4,)

        self.but25= builder.get_object("button25")
        self.but25.connect("clicked",self.ent_func,)

        self.but26= builder.get_object("button26")
        self.but26.connect("clicked",self.hide_event5,)

        self.but29= builder.get_object("button29")
        self.but29.connect("clicked",self.hide_event6,)



        self.entfunc= builder.get_object("entry1")
        self.entfunc2= builder.get_object("entry2")
        self.entfunc3= builder.get_object("entry3")

    def ent_func (self,widget):
        nome_func= self.entfunc.get_chars(0,-1)
        cargo_func= self.entfunc.get_chars(0,-1)
        n_c_t_func= self.entfunc.get_chars(0,-1)
        self.cur.execute('INSERT INTO self.dadosfunc VALUES(?,?,?)',(nome_func.decode("latin1"),cargo_func.decode("latin1"),n_c_t_func.decode("latin1")))
        conectar.commit()

    def func (self,widget,):
        self.window2.show_all()

    def mqna (self,widget,):
        self.window3.show_all()

    def cpta (self,widget,):
        self.window4.show_all()

    def gfco (self,widget,):
        self.window5.show_all()

    def hide_event(self,widget,):
        self.window2.hide_all()

    def hide_event2(self,widget,):
        self.window3.hide_all()

    def hide_event3(self,widget,):
        self.window4.hide_all()

    def hide_event4(self,widget,):
        self.window5.hide_all()

    def hide_event5(self,widget,):
        self.window6.hide_all()

    def hide_event6(self,widget,):
        self.window7.hide_all()

    def delete_event2(self,widget,):
        gtk.main_quit()

    def cad_func (self,widget,):
        self.window6.show_all()

    def cad_mqna (self,widget,):
        self.window7.show_all()

p=progm()
gtk.main()