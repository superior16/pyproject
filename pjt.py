#-*-coding: latin1-*-
import pygtk
pygtk.require('2.0')
import gtk
import sqlite3
import numpy as np
import scipy.stats as spst
import scipy.optimize as spop
import scipy.interpolate as spint
import pylab
import scipy





class progm(object):


    def __init__(self):
        queryCriar = """CREATE TABLE IF NOT EXISTS dadosfunc (nome text, cargo text, numero_carteira text)"""
        self.conectar = sqlite3.connect("dadosfunc.db")
        self.cur= self.conectar.cursor()
        self.cur.execute(queryCriar)
        self.conectar.commit()

        queryCriar2 = """CREATE TABLE IF NOT EXISTS dadosbruto (valor text, mes text)"""
        self.conectar = sqlite3.connect("dadosfunc.db")
        self.cur= self.conectar.cursor()
        self.cur.execute(queryCriar2)
        self.conectar.commit()

        queryCriar3 = """CREATE TABLE IF NOT EXISTS dadosdesp (valor text, mes text)"""
        self.conectar = sqlite3.connect("dadosfunc.db")
        self.cur= self.conectar.cursor()
        self.cur.execute(queryCriar3)
        self.conectar.commit()


        queryCriar4 = """CREATE TABLE IF NOT EXISTS dadosmaq (nome text, funcao text, numero_maquina text)"""
        self.conectar = sqlite3.connect("dadosfunc.db")
        self.cur= self.conectar.cursor()
        self.cur.execute(queryCriar4)
        self.conectar.commit()

        queryCriar5 = """CREATE TABLE IF NOT EXISTS dadoscont (nome text, numero text)"""
        self.conectar = sqlite3.connect("dadosfunc.db")
        self.cura= self.conectar.cursor()
        self.cura.execute(queryCriar5)
        self.cura.execute('INSERT INTO dadoscont VALUES(?,?)',('a','0'))
        self.cura.execute('INSERT INTO dadoscont VALUES(?,?)',('b','0'))
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
        self.window8= builder.get_object("window8")
        self.window9= builder.get_object("window9")
        self.window10= builder.get_object("window10")
        self.window11= builder.get_object("window11")
        self.window12= builder.get_object("window12")

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

        self.but7= builder.get_object("button7")
        self.but7.connect("clicked",self.atu_func,)

        self.but8= builder.get_object("button8")
        self.but8.connect("clicked",self.dec_func,)

        self.but9= builder.get_object("button9")
        self.but9.connect("clicked",self.hide_event,)

        self.but10= builder.get_object("button10")
        self.but10.connect("clicked",self.cad_mqna,)

        self.but11= builder.get_object("button11")
        self.but11.connect("clicked",self.dec_mqna,)

        self.but12= builder.get_object("button12")
        self.but12.connect("clicked",self.hide_event2,)

        self.but13= builder.get_object("button13")
        self.but13.connect("clicked",self.valor_bruto,)

        self.but14= builder.get_object("button14")
        self.but14.connect("clicked",self.despesas,)

        self.but15= builder.get_object("button15")
        self.but15.connect("clicked",self.hide_event3,)

        self.but16= builder.get_object("button16")
        self.but16.connect("clicked",self.gra_prod,)

        self.but17= builder.get_object("button17")
        self.but17.connect("clicked",self.hide_event4,)

        self.but18= builder.get_object("button18")
        self.but18.connect("clicked",self.save_cn_func,)

        self.but19= builder.get_object("button19")
        self.but19.connect("clicked",self.ent_func,)

        self.but20= builder.get_object("button20")
        self.but20.connect("clicked",self.hide_event5,)

        self.but21= builder.get_object("button21")
        self.but21.connect("clicked",self.save_cn_maq,)

        self.but22= builder.get_object("button22")
        self.but22.connect("clicked",self.ent_maq,)

        self.but23= builder.get_object("button23")
        self.but23.connect("clicked",self.hide_event6,)

        self.but24= builder.get_object("button24")
        self.but24.connect("clicked",self.del_func,)

        self.but25= builder.get_object("button25")
        self.but25.connect("clicked",self.con_func,)

        self.but26= builder.get_object("button26")
        self.but26.connect("clicked",self.hide_event7,)

        self.but27= builder.get_object("button27")
        self.but27.connect("clicked",self.del_maq,)

        self.but28= builder.get_object("button28")
        self.but28.connect("clicked",self.con_maq,)

        self.but29= builder.get_object("button29")
        self.but29.connect("clicked",self.hide_event8,)

        """self.but30= builder.get_object("button30")
        self.but30.connect("clicked",self.atu_func,)"""

        self.but31= builder.get_object("button31")
        """self.but31.connect("clicked",self.hide_event9,)"""

        self.but32= builder.get_object("button32")
        self.but32.connect("clicked",self.add_bruto,)

        self.but33= builder.get_object("button33")
        self.but33.connect("clicked",self.hide_event10,)

        self.but34= builder.get_object("button34")
        self.but34.connect("clicked",self.add_despesas,)

        self.but35= builder.get_object("button35")
        self.but35.connect("clicked",self.hide_event11,)

        self.entfunc= builder.get_object("entry1")
        self.entfunc2= builder.get_object("entry2")
        self.entfunc3= builder.get_object("entry3")
        self.entmaq= builder.get_object("entry4")
        self.entmaq2= builder.get_object("entry5")
        self.entmaq3= builder.get_object("entry6")
        self.dec_func= builder.get_object("entry7")
        self.dec_maq= builder.get_object("entry8")
        self.atu_func_pesq= builder.get_object("entry9")
        """self.atu_func_cargo= builder.get_object("entry10")"""
        self.valor_bruto_valor= builder.get_object("entry11")
        self.valor_bruto_mes= builder.get_object("entry12")
        self.desp_valor= builder.get_object("entry13")
        self.desp_mes= builder.get_object("entry14")


        self.label_name_func= builder.get_object("label17")
        self.label_carg_func= builder.get_object("label18")
        self.label_n_func= builder.get_object("label19")
        self.label_name_maq= builder.get_object("label23")
        self.label_func_maq= builder.get_object("label25")
        self.label_n_maq= builder.get_object("label27")


    def ent_func (self,widget):
        nome_func= self.entfunc.get_chars(0,-1)
        cargo_func= self.entfunc2.get_chars(0,-1)
        n_c_t_func= self.entfunc3.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        cur.execute('INSERT INTO dadosfunc VALUES(?,?,?)', (nome_func.decode("latin1"), cargo_func.decode("latin1"),n_c_t_func.decode("latin1")))
        conectar.commit()
        self.window6.hide_all()

    def add_bruto (self,widget):
        valor_bruto= self.valor_bruto_valor.get_chars(0,-1)
        valor_bruto_mes= self.valor_bruto_mes.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql2="""SELECT * FROM dadoscont WHERE nome = 'a'"""
        cur.execute(sql2)
        quasea= cur.fetchone()
        a=int(quasea[1])

        if a==0:
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Janeiro'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Fevereiro'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Marco'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Abril'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Maio'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Junho'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Julho'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Agosto'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Setembro'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Outubro'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Novembro'))
            cur.execute("INSERT INTO dadosbruto VALUES(?,?)",('0','Dezembro'))




        sql2="""UPDATE dadoscont SET numero='1'WHERE nome='a'"""
        cur.execute(sql2)


        valor_bruto=float(valor_bruto.decode("latin1"))
        sql = """SELECT * FROM dadosbruto WHERE mes = '"""+str(valor_bruto_mes.decode("latin1"))+"""'"""
        cur.execute(sql)
        valor_anterior= cur.fetchone()
        valor_bruto+= float(valor_anterior[0])
        valor_bruto=str(valor_bruto)
        cur.execute("""UPDATE dadosbruto SET valor= '"""+str(valor_bruto)+"""'WHERE mes='"""+str(valor_anterior[1].decode("latin1"))+"""'""")
        conectar.commit()
        self.valor_bruto_mes.set_text("")
        self.valor_bruto_valor.set_text("")

    def add_despesas (self,widget):
        valor_despesa= self.desp_valor.get_chars(0,-1)
        valor_despesa_mes= self.desp_mes.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql2="""SELECT * FROM dadoscont WHERE nome = 'b'"""
        cur.execute(sql2)
        quaseb= cur.fetchone()
        b=int(quaseb[1])

        if b==0:
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Janeiro'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Fevereiro'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Marco'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Abril'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Maio'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Junho'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Julho'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Agosto'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Setembro'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Outubro'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Novembro'))
            cur.execute("INSERT INTO dadosdesp VALUES(?,?)",('0','Dezembro'))




        sql2="""UPDATE dadoscont SET numero='1'WHERE nome='b'"""
        cur.execute(sql2)


        valor_despesa=float(valor_despesa.decode("latin1"))
        sql = """SELECT * FROM dadosdesp WHERE mes = '"""+str(valor_despesa_mes.decode("latin1"))+"""'"""
        cur.execute(sql)
        valor_anterior= cur.fetchone()
        valor_despesa+= float(valor_anterior[0])
        valor_despesa=str(valor_despesa)
        cur.execute("""UPDATE dadosdesp SET valor= '"""+str(valor_despesa)+"""'WHERE mes='"""+str(valor_anterior[1].decode("latin1"))+"""'""")
        conectar.commit()
        self.desp_mes.set_text("")
        self.desp_valor.set_text("")




    def ent_maq(self,widget):
        nome_maq= self.entmaq.get_chars(0,-1)
        funcao_maq= self.entmaq2.get_chars(0,-1)
        n_m_maq= self.entmaq3.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        cur.execute('INSERT INTO dadosmaq VALUES(?,?,?)',(nome_maq.decode("latin1"),funcao_maq.decode("latin1"),n_m_maq.decode("latin1")))
        conectar.commit()
        self.window7.hide_all()

    def save_cn_maq(self,widget):
        nome_maq= self.entmaq.get_chars(0,-1)
        funcao_maq= self.entmaq2.get_chars(0,-1)
        n_m_maq= self.entmaq3.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        cur.execute('INSERT INTO dadosmaq VALUES(?,?,?)',(nome_maq.decode("latin1"),funcao_maq.decode("latin1"),n_m_maq.decode("latin1")))
        conectar.commit()
        self.entmaq.set_text("")
        self.entmaq2.set_text("")
        self.entmaq3.set_text("")

    def save_cn_func(self,widget):
        nome_func= self.entfunc.get_chars(0,-1)
        cargo_func= self.entfunc2.get_chars(0,-1)
        n_c_t_func= self.entfunc3.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        cur.execute('INSERT INTO dadosfunc VALUES(?,?,?)',(nome_func.decode("latin1"),cargo_func.decode("latin1"),n_c_t_func.decode("latin1")))
        conectar.commit()
        self.entfunc.set_text("")
        self.entfunc2.set_text("")
        self.entfunc3.set_text("")

    def gra_prod(self,widget):
        mes=['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro',]
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        lista_eixo_valor=[0]
        lista_eixo_meses =[0]
        lista_eixo_despesa =[0]
        lista_eixo_lucro =[0]
        i =0
        while i<12:
            sql = """SELECT * FROM dadosbruto WHERE mes = '"""+mes[i]+"""'"""
            cur.execute(sql)
            eixo_valor =cur.fetchone()
            lista_eixo_meses.append((1+i))
            lista_eixo_valor.append(float(eixo_valor[0]))
            sql = """SELECT * FROM dadosdesp WHERE mes = '"""+mes[i]+"""'"""
            cur.execute(sql)
            eixo_desp =cur.fetchone()
            lista_eixo_despesa.append(float(eixo_desp[0]))
            lista_eixo_lucro.append(float(lista_eixo_valor[i]) - float(lista_eixo_despesa[i]))
            i+=1

        pylab.plot (lista_eixo_meses,lista_eixo_lucro, color = "green", label = 'F=Lucro')
        pylab.plot (lista_eixo_meses,lista_eixo_valor, color = "black", label = 'F=Valor Bruto')
        pylab.plot (lista_eixo_meses,lista_eixo_despesa, color = "red", label = 'F=Despesas')
        pylab.title ('Grafico de lucro')
        pylab.xlabel ('mes')
        pylab.legend (loc = 'upper left')
        pylab.ylabel ('Valor em R$')
        pylab.grid (True)
        pylab.show()


    def del_func(self,widget):
        del_fun=self.dec_func.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql = """DELETE FROM dadosfunc WHERE nome = '"""+str(del_fun.decode("latin1"))+"""'"""
        cur.execute(sql)
        conectar.commit()
        self.dec_func.set_text("")

    def con_func(self,widget):
        con_fun=self.dec_func.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql = """SELECT * FROM dadosfunc WHERE nome = '"""+str(con_fun.decode("latin1"))+"""'"""
        cur.execute(sql)
        label_n=self.label_carg=label_name=cur.fetchone()
        self.label_name_func.set_text(str(label_name[0]))

        self.label_carg_func.set_text(str(self.label_carg[1]))

        self.label_n_func.set_text(str(label_n[2]))

        conectar.commit()
        self.dec_func.set_text("")


    def del_maq(self,widget):
        del_mac=self.dec_maq.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql = """DELETE FROM dadosmaq WHERE nome = '"""+str(del_mac.decode("latin1"))+"""'"""
        cur.execute(sql)
        conectar.commit()
        self.dec_maq.set_text("")

    def con_maq(self,widget):
        con_maq=self.dec_maq.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql = """SELECT * FROM dadosmaq WHERE nome = '"""+str(con_maq.decode("latin1"))+"""'"""
        cur.execute(sql)
        label_n =label_func =label_name =cur.fetchone()
        self.label_name_maq.set_text(str(label_name[0]))

        self.label_func_maq.set_text(str(label_func[1]))

        self.label_n_maq.set_text(str(label_n[2]))

        conectar.commit()
        self.dec_maq.set_text("")

    def atu_func(self,widget):

        atu_fun =self.atu_func_pesq.get_chars(0,-1)
        conectar = sqlite3.connect("dadosfunc.db")
        cur= conectar.cursor()
        sql = """UPDATE dadosfunc SET cargo = '"""+str(atu_fun.decode("latin1"))+"""'WHERE cargo ='"""+str(self.label_carg[1])+"""'"""
        cur.execute(sql)
        conectar.commit()
        self.atu_func_pesq.set_text("")



    """def atum_func(self,widget):
        self.window10.show_all()
        self.atu_func_pesq.set_text("")
        self.atu_func_cargo.set_text("")"""

    def dec_func(self,widget):
        self.window8.show_all()
        self.label_name_func.set_text("")
        self.label_carg_func.set_text("")
        self.label_n_func.set_text("")
        self.dec_func.set_text("")

    def dec_mqna(self,widget):
        self.window9.show_all()
        self.label_func_maq.set_text("")
        self.label_name_maq.set_text("")
        self.label_n_maq.set_text("")
        self.dec_maq.set_text("")

    def valor_bruto(self,widget):
        self.window11.show_all()
        self.valor_bruto_valor.set_text("")
        self.valor_bruto_mes.set_text("")

    def despesas(self,widget):
        self.window12.show_all()
        self.desp_valor.set_text("")
        self.desp_mes.set_text("")


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

    def hide_event7(self,widget,):
        self.window8.hide_all()

    def hide_event8(self,widget,):
        self.window9.hide_all()

    def hide_event9(self,widget,):
        self.window10.hide_all()

    def hide_event10(self,widget,):
        self.window11.hide_all()

    def hide_event11(self,widget,):
        self.window12.hide_all()

    def delete_event2(self,widget,):
        gtk.main_quit()

    def cad_func (self,widget,):
        self.window6.show_all()
        self.entfunc.set_text("")
        self.entfunc2.set_text("")
        self.entfunc3.set_text("")

    def cad_mqna (self,widget,):
        self.window7.show_all()
        self.entmaq.set_text("")
        self.entmaq2.set_text("")
        self.entmaq3.set_text("")


p=progm()

gtk.main()