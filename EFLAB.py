from tkinter import *
import sys
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import pandas as pd
from tkinter import Tk, Text, Scrollbar
from tkinter import messagebox 
from tkinter import filedialog

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


#Clase pestañas

#region
class ButtonNotebook(ttk.Notebook):
    _initialized = False

    def __init__(self, *args, **kwargs):
        if not self._initialized:
            self._initialize()
            self._inititialized = True

        kwargs["style"] = "ButtonNotebook"
        super().__init__(*args, **kwargs)
        self._active = None

        self.bind("<ButtonPress-1>", self.on_tab_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_tab_close_release)

    def on_tab_close_press(self, event):
        name = self.identify(event.x, event.y)
        if name == "tab_btn_close":
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_tab_close_release(self, event):
        if not self.instate(['pressed']):
            return None

        name = self.identify(event.x, event.y)

        if name == "tab_btn_close":
            index = self.index("@%d,%d" % (event.x, event.y))
            if self._active == index:
                self.forget(index)
                self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def _initialize(self):
        style = ttk.Style()
        if sys.platform == "win32":
            style.theme_use('winnative')

        self.images = (
            tk.PhotoImage("img_close", data='''
                          R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2f///////////////yH5
                          BAEKAAIALAAAAAAIAAgAAAMUCCAsCmO5OBVl8OKhoV3e9jQOkAAAOw==
                           '''),
            tk.PhotoImage("img_closeactive", data='''
                          R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2f///////////////yH5
                          BAEKAAMALAAAAAAIAAgAAAMPCDA8+gw+GGlVbWKqmwMJADs=
                          '''),
            tk.PhotoImage("img_closepressed", data='''
                          R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2f///////////////yH5B
                          AEKAAMALAAAAAAIAAgAAAMPGDE8+gw+GGlVbWKqmwsJADs=
                          ''')
        )

        style.element_create("tab_btn_close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"), border=8, sticky='')

        style.layout("ButtonNotebook", [
                     ("ButtonNotebook.client", {"sticky": "nswe"})])
        style.layout("ButtonNotebook.Tab", [
            ("ButtonNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("ButtonNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ButtonNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ButtonNotebook.label", {
                                     "side": "left", "sticky": ''}),
                                    ("ButtonNotebook.tab_btn_close",
                                     {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })
        ])

        style.configure("ButtonNotebook.Tab", background="#fdd57e")
        style.map('ButtonNotebook.Tab', background=[("selected", "#f2f2f2"),
                                                      ("active", "#fc9292")],
                  foreground=[("selected", "#000000"),
                                                      ("active", "#000000")]
                 )

#endregion                


if __name__ == "__main__":

    ventana = tk.Tk()
    # ventana.geometry('1560x830')
    ventana.geometry('1480x690')
    ventana.iconbitmap( "eflab.ico")
    ventana.wm_title("")
    nb = ButtonNotebook(width=200, height=200)
    nb.pressed_index = None
    pes0 = tk.Frame(nb)
    nb.add(pes0, text='Welcome')
    nb.pack(fill='both', expand='yes')

    #-------------------------------------------------Frames pestaña inicio ----------------------------------------------
    frame1 = tk.Frame(pes0, width=230, height=1000)
    frame1.grid(column=1, row=0)
  
    frame2 = tk.Frame(pes0, width=1024, height=800)
    frame2.grid(column=0, row=0)
    #---------------------------------------------------------------------------------------------------------------------

   
    #--------------------------------------------------Label frames pestaña de inicio-------------------------------------
    lfhelp = tk.LabelFrame(frame1, text="About")
    lfhelp.grid(padx=60, pady=25, ipadx=200 ,ipady=85)
    lfhelp.grid_propagate(False)

    lfstar = tk.LabelFrame(frame1, text="Star")
    lfstar.grid(padx=60, pady=30 ,ipadx=200 ,ipady=85)
    lfstar.grid_propagate(False)

    lfexamples = tk.LabelFrame(frame1, text="Examples")
    lfexamples.grid(padx=60, pady=30, ipadx=200 ,ipady=85)
    lfexamples.grid_propagate(False)
    #----------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------Frame daportada ---------------------------------------------
    fdatos = tk.LabelFrame(frame2)
    fdatos.grid(padx=50, pady=25,ipadx=360, ipady=300)
    fdatos.grid_propagate(False)
    #----------------------------------------------------------------------------------------------------------------------



    # ---------------------Funcion para crar nueva pestaña cálculo del metodo A(pestaña1) ----------------------------------
    #region
    def pestaña1():
        from class_combobox import ObtenerDatos
        pes1 = tk.Frame(nb)
        pestaña1 = nb.add(pes1, text='Cálculo con el método A')
        
        #-----------------------------------------------Frames pestaña datos necesarios-------------------------------------
        frame3 = tk.Frame(pes1, width=720, height=300)
        frame3.grid(column=0, row=0,ipady=0)
        frame4 = tk.Frame(pes1, width=760, height=105)
        frame4.grid(column=0, row=1, ipady=0)
        frame5 = tk.Frame(pes1, width=800, height=300)
        frame5.grid(column=1, row=0)
        frame6 = tk.Frame(pes1, width=800, height=200)
        frame6.grid(column=1, row=1)
        #-------------------------------------------------------------------------------------------------------------------
        
        #-------------------------------------------------------Label frames pestaña 1--------------------------------------
        lfdatos = tk.LabelFrame(master=frame3, text="Datos:")
        lfdatos.grid(padx=10, pady=0, ipadx=340 ,ipady=130)
        lfdatos.grid_propagate(False)
        lfperfil = tk.LabelFrame(master=frame5, text="Perfil de carga:")
        lfperfil.grid(padx=40, pady=0, ipadx=380 ,ipady=90)
        lfperfil.grid_propagate(False)
        lfmax = tk.LabelFrame(master=frame5, text="")
        # lfmax = tk.LabelFrame(master=frame5, text="Máxima eficiencia:")
        lfmax.grid(padx=40, pady=0, ipadx=380 ,ipady=35)
        lfmax.grid_propagate(False)
        #-------------------------------------------------------------------------------------------------------------------

        #----------------------------------------------------Entradas texto lfdatos-----------------------------------------
        lsn = tk.Label(master=lfdatos, text="Potencia nominal Sn [kVA] ")
        lsn.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        lsn.config(fg="black", font=("Arial", 11)) 
        ensn = tk.Entry(lfdatos)
        ensn.grid(row=0, column=1, padx=5, pady=5)

        lpo = tk.Label(master=lfdatos, text="Potencia de pérdidas en vacio[kW] ")
        lpo.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        lpo.config(fg="black", font=("Arial", 11)) 
        enpo = tk.Entry(lfdatos)
        enpo.grid(row=1, column=1, padx=5, pady=5)

        lpk = tk.Label(master=lfdatos, text="Potencia de pérdidas con carga[kW] ")
        lpk.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        lpk.config(fg="black", font=("Arial", 11)) 
        enpk = tk.Entry(lfdatos)
        enpk.grid(row=2, column=1, padx=5, pady=5)

        lpco = tk.Label(master=lfdatos, text="Potencia de pérdidas sistema de refrigeración en vacío [kW] ")
        lpco.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        lpco.config(fg="black", font=("Arial", 11)) 
        enpco = tk.Entry(lfdatos)
        enpco.grid(row=3, column=1, padx=5, pady=5)
        
        lpkk = tk.Label(master=lfdatos, text="Potencia de pérdidas sistema de refrigeración con carga[kW] ")
        lpkk.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        lpkk.config(fg="black", font=("Arial", 11)) 
        enpkk = tk.Entry(lfdatos)
        enpkk.grid(row=4, column=1, padx=5, pady=5)

        lcbx = tk.Label(master=lfdatos, text="Seleccione el Perfil de carga.. ")
        lcbx.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        lcbx.config(fg="black", font=("Arial", 11)) 
    

        #------------------------------------------------------COMBOBOX PESTAÑA 1------------------------------------------------------ 
        # opciones = ["Perfil de carga 1", "Perfil de carga 2", "Perfil de carga 3", "Perfil Caso 1", "Perfil Caso 2", "Perfil Caso 3", "Perfil Caso 4 T1", "Perfil Caso 4 T2"]
        opciones = ["perfil_1", "perfil_2", "perfil_3", "perfil_CASO_1", "perfil_CASO_2", "perfil_CASO_3", "perfil_CASO_4_T1", "perfil_CASO_4_T2"]
        
        # self.opciones.append("Perfil de carga 4")
        lista_combo = ttk.Combobox(master=lfdatos, values=opciones, state= "readonly")
        lista_combo.configure(width=25)
        lista_combo.grid(row=5, column=1, padx=0, pady=5)
        #--------------------------------------------------------------------------------------------------------------------------------
        
        #------------------------------------------------- INSTANCIAR CLASE ObtenerDatos------------------------------------------------
        obtenerDatos = ObtenerDatos(lista_combo)
        obtenerDatos.SetOpciones(opciones)
        #-------------------------------------------------------------------------------------------------------------------------------

        #----------------------------------------------Función para cargar datos Pestaña 1--------------------------------------------- 
        def cargar():

            # from firebase import firebase
            import numpy as np
            import firebase_admin
            from firebase_admin import credentials
            from firebase_admin import db
                        
            #-----------------------------------------------Condicional para bloquar boton-----------------------------------------------
            if (button5['state'] == tk.NORMAL):
                button5['state'] = tk.DISABLED
            else:
                button5['state'] = tk.NORMAL
            #-----------------------------------------------------------------------------------------------------------------------------    

                      
            #----------------------------------------GET firebase-----Datos para cálculo------perfil de carga-------------------------------
            #método para llamar la base de datos 
            obtenerDatos.ConsumirPerfil()
            np_angulo = obtenerDatos.getAngulo()
            np_kl = obtenerDatos.getKl()
            #-------------------------------------------------------------------------------------------------------------------------------



            #------------------------------------------------------------Graficos 2d pestaña1----------------------------------------------
            
            '''tiempo perfil de carga '''
            t = np.arange(0, 24, 1)
            np_time = np.array(t)
            # print(np_time)
           
            '''perdidas en vacio'''
            v1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            # valorpo = [44.7100225]
            valorpo = [str(enpo.get())]
            # print(valorpo)
            po = np.array(valorpo, dtype='f')
            # print(po)
            np_po = np.array(np.multiply(po, v1))
            # print(np_po)
                        
            '''factor de potencia '''
            rad = np.pi/180
            cos = np.multiply(np_angulo, rad )
            np_fp = np.array(np.cos(cos))
            # print(np_fp)
            
            ''' potencia de la carga'''
            valorsn = [str(ensn.get())]
            sn = np.array(valorsn, dtype='f')
            # valorsn = [168000]
            np_p2c = np.array(sn*np.multiply(np_fp, np_kl))
            # print(np_p2c)
                        
            ''' perdidas devanados'''
            # valorpk = [325.379346]
            valorpk = [str(enpk.get())]
            pk = np.array(valorpk, dtype='f')
            
            np_pk = np.array(np.multiply(pk, v1))
            # print(np_pk)
            
            "potencia sistema de refrigeración sin carga "
            # valorpco = [0]
            valorpco = [str(enpco.get())]
            pco = np.array(valorpco, dtype='f')
            
            np_pco = np.array(np.multiply(pco, v1))
            # print(np_pco)
            
            "potencia sistema de enfriaiento con carga "
            # valorpck = [0]
            valorpck = [str(enpkk.get())]
            pck = np.array(valorpck, dtype='f')
            
            np_pck = np.array(np.multiply(pck, v1))
            # print(np_pck)
                                    
            ''' calculo de la eficiencia metodo A'''
            A = np_po + np_pco
            B = np.multiply(np_pk, np_kl**2)+np_pck
            
            N = np_p2c - A - B
            
            ef = (np.true_divide(N, np_p2c))*100
            np_ef = np.array(ef)
            # print(np_ef)

            print("- valor maximo de los elementos np_ef ANALSIS METODO A:")
            print(np.amax(np_ef)) # 
            print("- valor minimo de los elementos np_ef ANALSIS METODO A:")
            print(np.amin(np_ef)) # 
            print("- promedio (media) de los elementos np_ef ANALSIS METODO A:")
            print(np.mean(np_ef)) # 

            #-----------------------------------------CALCULO EFICIENCIA MAXIMA Pestaña 1 ---------------------------------------

            #----------------------------------------------------Valores maximos--------------------------------------------------
            efmax = np.max(np_ef)
            efmax_r = round(efmax, 2)
            # print(efmax_r)
            
            hora = np.where(np_ef==efmax)[0]
            # print(hora)
            
            h = str(hora)[1:-1]
            # print(h)
            
            klmax = np_kl[int(h)]
            klmax_r =  round(klmax, 2)
            # print(klmax)
            
            fpmax = np_fp[int(h)]
            fpmax_r = round(fpmax, 2)
            # print(fpmax)
            
            angulomax = np_angulo[int(h)]
            angulomax_r = round(angulomax, 2)
            #-------------------------------------------------------------------------------------------------------------------
            #----------------------------------------------------Valores mimimos--------------------------------------------------
            efmin = np.amin(np_ef)
            efmin_r = round(efmin, 2)
            # print(efmax_r)
            
            hora1 = np.where(np_ef==efmin)[0]
            # print(hora)
            
            h1 = str(hora1)[1:-1]
            # print(h)
            
            klmin = np_kl[int(h1)]
            klmin_r =  round(klmin, 2)
            # print(klmax)
            
            fpmin = np_fp[int(h1)]
            fpmin_r = round(fpmin, 2)
            # print(fpmax)
            
            angulomin = np_angulo[int(h1)]
            angulomin_r = round(angulomin, 2)
            #-------------------------------------------------------------------------------------------------------------------
            #----------------------------------------------------Valor medio--------------------------------------------------
            efmed = np.mean(np_ef)
            efmed_r = round(efmed, 2)
            # print(efmax_r)
          
            #-------------------------------------------------------------------------------------------------------------------

            #-----------------------------------------------Stringvar maxima eficiencia ----------------------------------------
            Var_efmax = tk.StringVar()
            Var_efmax.set(efmax_r)
            
            Var_h = tk.StringVar()
            Var_h.set(h)

            Var_Klmax = tk.StringVar()
            Var_Klmax.set(klmax_r)

            Var_fpmax = tk.StringVar()
            Var_fpmax.set(fpmax_r)

            Var_angulomax = tk.StringVar()
            Var_angulomax.set(angulomax_r)
          
          
            Var_efmin = tk.StringVar()
            Var_efmin.set(efmin_r)
            
            Var_h1 = tk.StringVar()
            Var_h1.set(h1)

            Var_Klmin = tk.StringVar()
            Var_Klmin.set(klmin_r)

            Var_fpmin = tk.StringVar()
            Var_fpmin.set(fpmin_r)

            Var_angulomin = tk.StringVar()
            Var_angulomin.set(angulomin_r)


            Var_efmed = tk.StringVar()
            Var_efmed.set(efmed_r)



            
            #------------------------------------------------------------------------------------------------------------------

            #--------------------------------------------------FRAME EFICIENCIA MAX----------------------------------------------
            lefmax = tk.Label(master=lfmax, text="Eficiencia MAX.[%] ")
            lefmax.grid(row=0, column=0, sticky=W, padx=1, pady=5)
            lefmax.config(fg="black", font=("Arial", 11)) 
            enefmax = tk.Entry(lfmax,textvariable = Var_efmax, width=6)
            enefmax.grid(row=0, column=1, ipadx=0.25, pady=5)

            lefmax1 = tk.Label(master=lfmax, text="Eficiencia MIN.[%] ")
            lefmax1.grid(row=1, column=0, sticky=W, padx=1, pady=5)
            lefmax1.config(fg="black", font=("Arial", 11)) 
            enefmax1 = tk.Entry(lfmax,textvariable = Var_efmin, width=6)
            enefmax1.grid(row=1, column=1, ipadx=0.25, pady=5)

            lefmax2 = tk.Label(master=lfmax, text="Eficiencia MED.[%] ")
            lefmax2.grid(row=0, column=16, sticky=W, padx=1, pady=5)
            lefmax2.config(fg="black", font=("Arial", 11)) 
            enefmax2 = tk.Entry(lfmax,textvariable = Var_efmed, width=8)
            enefmax2.grid(row=1, column=16, ipadx=0.25, pady=5)




                
            lklmax = tk.Label(master=lfmax, text="Kl[%]")
            lklmax.grid(row=0, column=3, sticky=W, padx=1, pady=5)
            lklmax.config(fg="black", font=("Arial", 11)) 
            enklmax = tk.Entry(lfmax,textvariable = Var_Klmax, width=6)
            enklmax.grid(row=0, column=4, ipadx=0.25, pady=5)
              
            lklmax1 = tk.Label(master=lfmax, text="Kl[%]")
            lklmax1.grid(row=1, column=3, sticky=W, padx=1, pady=5)
            lklmax1.config(fg="black", font=("Arial", 11)) 
            enklmax1 = tk.Entry(lfmax,textvariable = Var_Klmin, width=6)
            enklmax1.grid(row=1, column=4, ipadx=0.25, pady=5)

         





            
            lfpmax = tk.Label(master=lfmax, text="cosΦ")
            lfpmax.grid(row=0, column=6, sticky=W, padx=5, pady=5)
            lfpmax.config(fg="black", font=("Arial", 11)) 
            enfpmax = tk.Entry(lfmax,textvariable = Var_fpmax, width=6)
            enfpmax.grid(row=0, column=7, ipadx=0.25, pady=5)

            lfpmax1 = tk.Label(master=lfmax, text="cosΦ")
            lfpmax1.grid(row=1, column=6, sticky=W, padx=5, pady=5)
            lfpmax1.config(fg="black", font=("Arial", 11)) 
            enfpmax1 = tk.Entry(lfmax,textvariable = Var_fpmin, width=6)
            enfpmax1.grid(row=1, column=7, ipadx=0.25, pady=5)

     

            
            lfpmax = tk.Label(master=lfmax, text="Angulo[°]")
            lfpmax.grid(row=0, column=9, sticky=W, padx=5, pady=5)
            lfpmax.config(fg="black", font=("Arial", 11)) 
            enfpmax = tk.Entry(lfmax,textvariable = Var_angulomax, width=6)
            enfpmax.grid(row=0, column=10, ipadx=0.25, pady=5)

            lfpmax1 = tk.Label(master=lfmax, text="Angulo[°]")
            lfpmax1.grid(row=1, column=9, sticky=W, padx=5, pady=5)
            lfpmax1.config(fg="black", font=("Arial", 11)) 
            enfpmax1 = tk.Entry(lfmax,textvariable = Var_angulomin, width=6)
            enfpmax1.grid(row=1, column=10, ipadx=0.25, pady=5)

      


    
            lHmax = tk.Label(master=lfmax, text="Hora")
            lHmax.grid(row=0, column=12, sticky=W, padx=5, pady=5)
            lHmax.config(fg="black", font=("Arial", 11)) 
            enHmax = tk.Entry(lfmax,textvariable = Var_h, width=6)
            enHmax.grid(row=0, column=13, ipadx=0.25, pady=5)

            lHmax1 = tk.Label(master=lfmax, text="Hora")
            lHmax1.grid(row=1, column=12, sticky=W, padx=5, pady=5)
            lHmax1.config(fg="black", font=("Arial", 11)) 
            enHmax1 = tk.Entry(lfmax,textvariable = Var_h1, width=6)
            enHmax1.grid(row=1, column=13, ipadx=0.25, pady=5)

 


            lH = tk.Label(master=lfmax, text="horas")
            lH.grid(row=0, column=14, sticky=W, padx=5, pady=5)
            lH.config(fg="black", font=("Arial", 11)) 

            lH1 = tk.Label(master=lfmax, text="horas")
            lH1.grid(row=1, column=14, sticky=W, padx=5, pady=5)
            lH1.config(fg="black", font=("Arial", 11)) 

   
            # buttonReporte = tk.Button(master=lfmax, text="GENERAR REPORTE", borderwidth=5, foreground="black",command=exportCSV)
            # buttonReporte.grid(row=0, column=15, padx=55, pady=5)
            #-------------------------------------------------------------------------------------------------------------------



        
            #-------------------------------------------------------Graficos 2d pestaña 1---------------------------------------- 
            fig = Figure(figsize=(8.1, 4.5))
                        
            # graficos eficiencia
            fig.subplots_adjust(left=0.08, bottom=0.10, right=0.97,
                                top=0.95, wspace=0.32, hspace=0.98)
            fig.add_subplot(321, ylabel="kl",
                            xlabel="time[h]", title="kL vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time, np_kl)
        
            fig.add_subplot(322, ylabel="Power Factor", xlabel="time[h]",
                            title="F.P. vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_fp)
            # fig.add_subplot(322, ylabel="Angle[°]", xlabel="time[h]",
            #                 title="Angle-time", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_angulo)

            fig.add_subplot(323, ylabel="η[%]", xlabel="kl",
                            title="EFFICIENCY vs kL").plot(np_kl, np_ef, 'ko')
            fig.add_subplot(324, ylabel="η[%]", xlabel="Power factor",
                            title="EFFICIENCY vs F.P.").plot(np_fp, np_ef, "ko")
            # fig.add_subplot(324, ylabel="η[%]", xlabel="Angle[°]",
            #                 title="Angle-Efficiency").plot(np_angulo, np_ef, "ko")
            
            fig.add_subplot(325, ylabel="P2c[kw]", xlabel="kl",
                            title="LOAD POWER vs kL").plot(np_kl, np_p2c/1000, 'go')              
            fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Power factor",
                            title="LOAD POWER vs F.P.").plot(np_fp, np_p2c/1000, 'go')
            # fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Angle[°]",
            #                 title="Angle-Load Power").plot(np_angulo, np_p2c/1000, 'go')
            
            canvas = FigureCanvasTkAgg(fig, master=frame6)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.X)
            
            toolbar = NavigationToolbar2Tk( canvas, frame6)
            toolbar.update()
            toolbar.pack()
                        
           
            #-------------------------------------------------------------------------------------------------------------------------

            #------------------------------------------------grafica 3D pestaña1 -----------------------------------------------------
            #region 
            # plt.style.use('dark_background')
            fig2 = plt.figure()
            canvas2 = FigureCanvasTkAgg(fig2, master=frame4)  # A tk.DrawingArea.
            canvas2.draw()
            ax = fig2.gca(projection ="3d")

            '''meshgrid'''
            np_klmesh, np_angulomesh = np.meshgrid(np_kl, np_angulo)
            # print(np_klmesh)
            # print(np_angulomesh)
                        
            '''factor de potencia '''
            np_fpmesh = np.array(np.cos(np_angulomesh * np.pi/180))
            # print(np_fpmesh)
            
            '''perdidas en vacio'''
            valorpo_3d = np_po 
            # print(valorpo)
                        
            ''' potencia de la carga'''
            np_p2cmesh = np.array(sn*np.multiply(np_fpmesh, np_klmesh))
            # print(np_p2cmesh)
                        
            ''' perdidas devanados'''
            valorpk_3d = np_pk
            # # print(valorpk)
            
            "potencia sistema de refrigeración sin carga "
            valorpco_3d = np_pco 
            # print(valorpco )
            
            "potencia sistema de enfriaiento con carga "
            valorpck_3d = np_pck
            # print(valorpck )
                        
            ''' calculo de la eficiencia metodo A'''
            Amesh = valorpo_3d + valorpco_3d
            # print(Amesh)
            
            Bmesh = np.multiply(valorpk_3d, np_klmesh**2)+valorpck_3d
            # print(Bmesh)
            
            N = np_p2cmesh - Amesh - Bmesh
            
            efmesh = (np.true_divide(N, np_p2cmesh))*100
            np_efmesh = np.array(efmesh)
            # print(np_efmesh)
                       
            # surf = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, cmap=cm.coolwarm, linewidth=0, antialiased=False)
            p = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, rstride=1, cstride=1, cmap='hot')
            
            # Customize the z axis.
            # ax.set_zlim(99, 100)
            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
            
            # Add a color bar which maps values to colors.
            
            # fig.colorbar(surf, shrink=0.5, aspect=5)
            
            plt.title('EFICIENCIA TRANSFORMADOR DE POTENCIA')
            plt.xlabel("kl")
            plt.ylabel('Angulo')
            
            fig.colorbar(p, ax=ax)
            
            toolbar = NavigationToolbar2Tk(canvas2, frame4)
            toolbar.update()
            canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            # canvas.get_tk_widget().grid(padx=50, pady=0, ipadx=50 ,ipady=5)
             
            #endregion
            #---------------------------------------------------------------------------------------------------------------------------

            #-------------------------------------------------tabla factor de potencia pestaña1-----------------------------------------
            lfperfil.columnconfigure(0, weight=1) 
            # resize row 0 height when the window is resized
            lfperfil.rowconfigure(0, weight=1)
            
            txt = Text(lfperfil)
            txt.grid(row=0, column=0, sticky="eswn")
            
            # scroll_y = Scrollbar(root, orient="vertical")
            scroll_y = Scrollbar(lfperfil, orient="vertical", command=txt.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            # bind txt to scrollbar
            txt.configure(yscrollcommand=scroll_y.set,)
                       
            very_long_list = pd.DataFrame({"Kl[%]": (np_kl), 
                                           " Angulo[°]": (np_angulo),
                                           "Factor de potencia[cosΦ]": (np_fp),
                                           "  Potencia en la carga[W]": (np_p2c),
                                           "Eficiencia η [%]": (np_ef)                                       
                                           })
            
            txt.insert("1.0", very_long_list)
            # make the text look like a label
            
            txt.configure(state="disabled", relief="flat", bg=lfperfil.cget("bg"))
            #-------------------------------------------------------------------------------------------------------------
            def exportCSV ():
                messagebox.showinfo("REPORTE DE DATOS", "la información calculada se almacena en un docuemento con extención .CSV")
                export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
                very_long_list.to_csv (export_file_path, index = False, header=True)

            buttonReporte = tk.Button(master=lfdatos, text="GUARDAR DATOS", borderwidth=5, foreground="black",command=exportCSV)
            buttonReporte.grid(row=6, column=0, padx=5, pady=5)

            #---------------------------------------------------------------------------------------------------------------

        #-------------------------------------------------------Botones pestaña 1-------------------------------------------------------
        button5 = tk.Button(master=lfdatos, text="Calcular", borderwidth=5, foreground="black",command=cargar)
        button5.grid(row=6, column=1, padx=5, pady=5)
        
        

        # #BOTON CARGAR PERFIL
        # def cargar_perfil():
        #       messagebox.showinfo("Cálculo utilizando el método A", "Para cargar un perfil de carga entrar a las siguiente url https://console.firebase.google.com/u/0/project/eflab-perfiles/database/eflab-perfiles/data?hl=es y colocar las siguientes credenciales:dssadf") 
        
        # # photo=tk.PhotoImage(file="help_question_1566.png")
        # buttonperfil = tk.Button(master=lfdatos,text="CARGAR PERFIL", relief="flat", borderwidth=5, foreground="black",command= cargar_perfil )
        # buttonperfil.config(fg="black", font=("Arial", 10,"bold")) 
        # buttonperfil.grid(row=6, column=0, sticky=W, padx=5, pady=5)
       
        #-------------------------------------------------------------------------------------------------------------------------------

        return set(pestaña1)
        #endregion
    #-------------------------------------------------------------------------------------------------------------------------------







    # ---------------------------------funcion para crar nueva pestaña cálculo del metodo B (pestaña2) ------------------------------------------
    #region
    def pestaña2():
        from class_combobox import ObtenerDatos
        pes4 = tk.Frame(nb)
        pestaña4 = nb.add(pes4, text='Cálculo con el método B')
        
        #-------------------------------------------frames pestaña datos necesarios Pestaña 2----------------------------------------------------
        frame15 = tk.Frame(pes4, width=720, height=300)
        frame15.grid(column=0, row=0,ipady=0)
        frame16 = tk.Frame(pes4, width=720, height=200)
        frame16.grid(column=0, row=1, ipady=0)
        frame17 = tk.Frame(pes4,width=800, height=300)
        frame17.grid(column=1, row=0)
        frame18 = tk.Frame(pes4, width=800, height=200)
        frame18.grid(column=1, row=1)
        #--------------------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------Label frames pestaña 2------------------------------------------------------
        lfdatos = tk.LabelFrame(master=frame15, text="Datos:")
        lfdatos.grid(padx=10, pady=0, ipadx=340 ,ipady=130)
        lfdatos.grid_propagate(False)
        lfperfil = tk.LabelFrame(master=frame17, text="Perfil de carga:")
        lfperfil.grid(padx=40, pady=0, ipadx=380 ,ipady=90)
        lfperfil.grid_propagate(False)
        lfmax = tk.LabelFrame(master=frame17, text="")
        # lfmax = tk.LabelFrame(master=frame5, text="Máxima eficiencia:")
        lfmax.grid(padx=40, pady=0, ipadx=380 ,ipady=35)
        lfmax.grid_propagate(False)
        #------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------Entradas texto lfdatos Pestaña 2-----------------------------------------------
        lsn = tk.Label(master=lfdatos, text="Potencia nominal Sn [KVA] ")
        lsn.grid(row=0, column=0, sticky=W, padx=65, pady=5)
        ensn = tk.Entry(lfdatos)
        ensn.grid(row=0, column=1, padx=5, pady=5)

        lpo = tk.Label(master=lfdatos, text="Potencia de pérdidas en vacio[kW] ")
        lpo.grid(row=1, column=0, sticky=W, padx=65, pady=5)
        enpo = tk.Entry(lfdatos)
        enpo.grid(row=1, column=1, padx=5, pady=5)

        lpk = tk.Label(master=lfdatos, text="Potencia de pérdidas con carga[kW] ")
        lpk.grid(row=2, column=0, sticky=W, padx=65, pady=5)
        enpk = tk.Entry(lfdatos)
        enpk.grid(row=2, column=1, padx=5, pady=5)

        ltf = tk.Label(master=lfdatos, text="Factor de corrección por temperatura tf ")
        ltf.grid(row=3, column=0, sticky=W, padx=65, pady=5)
        entf = tk.Entry(lfdatos)
        entf.grid(row=3, column=1, padx=5, pady=5)

        lcbx = tk.Label(master=lfdatos, text="Seleccione el Perfil de carga.. ")
        lcbx.grid(row=4, column=0, sticky=W, padx=65, pady=5)
        lcbx.config(fg="black", font=("Arial", 11)) 

        #------------------------------------------------------COMBOBOX PESTAÑA 2------------------------------------------------------ 
        # opciones = ["Perfil de carga 1", "Perfil de carga 2", "Perfil de carga 3", "Perfil Caso 1", "Perfil Caso 2", "Perfil Caso 3", "Perfil Caso 4 T1", "Perfil Caso 4 T2"]
        opciones = ["perfil_1", "perfil_2", "perfil_3", "perfil_CASO_1", "perfil_CASO_2", "perfil_CASO_3", "perfil_CASO_4_T1", "perfil_CASO_4_T2"]
        
        # self.opciones.append("Perfil de carga 4")
        lista_combo = ttk.Combobox(master=lfdatos, values=opciones, state= "readonly")
        lista_combo.configure(width=25)
        lista_combo.grid(row=4, column=1, padx=0, pady=5)
        #--------------------------------------------------------------------------------------------------------------------------------
        
        #------------------------------------------------- INSTANCIAR CLASE ObtenerDatos------------------------------------------------
        obtenerDatos = ObtenerDatos(lista_combo)
        obtenerDatos.SetOpciones(opciones)
        #-------------------------------------------------------------------------------------------------------------------------------

        #--------------------------------------------Función para cargar datos Pestaña 2------------------------------------------------ 
        def cargar():

            # from firebase import firebase
            import firebase_admin
            from firebase_admin import credentials
            from firebase_admin import db
            import numpy as np
            #-----CONDICIONAL PARA BLOQUEAR EL BOTON
            if (button5['state'] == tk.NORMAL):
                button5['state'] = tk.DISABLED
            else:
                button5['state'] = tk.NORMAL

                      
            #-------------------------------------------------Datos para cálculo-----------------------------------------------------------

            #----------------------------------------GET firebase-----Datos para cálculo------perfil de carga-------------------------------
            #método para llamar la base de datos 
            obtenerDatos.ConsumirPerfil()
            np_angulo = obtenerDatos.getAngulo()
            np_kl = obtenerDatos.getKl()
            #-------------------------------------------------------------------------------------------------------------------------------
            #-------------------------------------------------------------------------------------------------------------------------------


            #-----------------------------------------------Graficos 2d pestaña2------------------------------------------------------------
            #region 
            
            '''tiempo perfil de carga '''
            t = np.arange(0, 24, 1)
            np_time = np.array(t)
            # print(np_time)
            
            
            '''perdidas en vacio'''
            v1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                        
            # valorpo = [44.7100225]
            valorpo = [str(enpo.get())]
            # print(valorpo)

            po = np.array(valorpo, dtype='f')
            # print(po)
         
            np_po = np.array(np.multiply(po, v1))
            # print(np_po)
                        
            '''factor de potencia '''
            rad = np.pi/180
            cos = np.multiply(np_angulo, rad )
            np_fp = np.array(np.cos(cos))
            # print(np_fp)
            
            ''' potencia de la carga'''
            valorsn = [str(ensn.get())]
            sn = np.array(valorsn, dtype='f')
            # valorsn = [168000]
            
            np_p2c = np.array(sn*np.multiply(np_fp, np_kl))
            # print(np_p2c)
                        
            ''' perdidas devanados'''
            # valorpk = [325.379346]
            valorpk = [str(enpk.get())]
            pk = np.array(valorpk, dtype='f')
            
            np_pk = np.array(np.multiply(pk, v1))
            # print(np_pk)
          
             
            "factor de corrección de temperatura tf "
            # tf = [0.91]
            
            valortf = [str(entf.get())]
            
            Tf = np.array(valortf, dtype='f')
            
            ''' calculo de la eficiencia metodo B'''
            A = np_po 
            B = np.multiply(np_pk*Tf, np_kl**2)
            
            N = np_p2c + A + B
            
            ef = (np.true_divide(np_p2c, N))*100
            np_ef = np.array(ef)
      
        
            #-----------------------------------------CALCULO EFICIENCIA MAXIMA Pestaña 2- ---------------------------------------

            #----------------------------------------------------Valores maximos--------------------------------------------------
            efmax = np.max(np_ef)
            efmax_r = round(efmax, 2)
            # print(efmax_r)
            
            hora = np.where(np_ef==efmax)[0]
            # print(hora)
            
            h = str(hora)[1:-1]
            # print(h)
            
            klmax = np_kl[int(h)]
            klmax_r =  round(klmax, 2)
            # print(klmax)
            
            fpmax = np_fp[int(h)]
            fpmax_r = round(fpmax, 2)
            # print(fpmax)
            
            angulomax = np_angulo[int(h)]
            angulomax_r = round(angulomax, 2)
            #-------------------------------------------------------------------------------------------------------------------
            #----------------------------------------------------Valores mimimos--------------------------------------------------
            efmin = np.amin(np_ef)
            efmin_r = round(efmin, 2)
            # print(efmax_r)
            
            hora1 = np.where(np_ef==efmin)[0]
            # print(hora)
            
            h1 = str(hora1)[1:-1]
            # print(h)
            
            klmin = np_kl[int(h1)]
            klmin_r =  round(klmin, 2)
            # print(klmax)
            
            fpmin = np_fp[int(h1)]
            fpmin_r = round(fpmin, 2)
            # print(fpmax)
            
            angulomin = np_angulo[int(h1)]
            angulomin_r = round(angulomin, 2)
            #-------------------------------------------------------------------------------------------------------------------
            #----------------------------------------------------Valor medio--------------------------------------------------
            efmed = np.mean(np_ef)
            efmed_r = round(efmed, 2)
            # print(efmax_r)
          
            #-------------------------------------------------------------------------------------------------------------------

            #-----------------------------------------------Stringvar maxima eficiencia ----------------------------------------
            Var_efmax = tk.StringVar()
            Var_efmax.set(efmax_r)
            
            Var_h = tk.StringVar()
            Var_h.set(h)

            Var_Klmax = tk.StringVar()
            Var_Klmax.set(klmax_r)

            Var_fpmax = tk.StringVar()
            Var_fpmax.set(fpmax_r)

            Var_angulomax = tk.StringVar()
            Var_angulomax.set(angulomax_r)
          
          
            Var_efmin = tk.StringVar()
            Var_efmin.set(efmin_r)
            
            Var_h1 = tk.StringVar()
            Var_h1.set(h1)

            Var_Klmin = tk.StringVar()
            Var_Klmin.set(klmin_r)

            Var_fpmin = tk.StringVar()
            Var_fpmin.set(fpmin_r)

            Var_angulomin = tk.StringVar()
            Var_angulomin.set(angulomin_r)


            Var_efmed = tk.StringVar()
            Var_efmed.set(efmed_r)



            
            #------------------------------------------------------------------------------------------------------------------

            #--------------------------------------------------FRAME EFICIENCIA MAX----------------------------------------------
            lefmax = tk.Label(master=lfmax, text="Eficiencia MAX.[%] ")
            lefmax.grid(row=0, column=0, sticky=W, padx=1, pady=5)
            lefmax.config(fg="black", font=("Arial", 11)) 
            enefmax = tk.Entry(lfmax,textvariable = Var_efmax, width=6)
            enefmax.grid(row=0, column=1, ipadx=0.25, pady=5)

            lefmax1 = tk.Label(master=lfmax, text="Eficiencia MIN.[%] ")
            lefmax1.grid(row=1, column=0, sticky=W, padx=1, pady=5)
            lefmax1.config(fg="black", font=("Arial", 11)) 
            enefmax1 = tk.Entry(lfmax,textvariable = Var_efmin, width=6)
            enefmax1.grid(row=1, column=1, ipadx=0.25, pady=5)

            lefmax2 = tk.Label(master=lfmax, text="Eficiencia MED.[%] ")
            lefmax2.grid(row=0, column=16, sticky=W, padx=1, pady=5)
            lefmax2.config(fg="black", font=("Arial", 11)) 
            enefmax2 = tk.Entry(lfmax,textvariable = Var_efmed, width=8)
            enefmax2.grid(row=1, column=16, ipadx=0.25, pady=5)




                
            lklmax = tk.Label(master=lfmax, text="Kl[%]")
            lklmax.grid(row=0, column=3, sticky=W, padx=1, pady=5)
            lklmax.config(fg="black", font=("Arial", 11)) 
            enklmax = tk.Entry(lfmax,textvariable = Var_Klmax, width=6)
            enklmax.grid(row=0, column=4, ipadx=0.25, pady=5)
              
            lklmax1 = tk.Label(master=lfmax, text="Kl[%]")
            lklmax1.grid(row=1, column=3, sticky=W, padx=1, pady=5)
            lklmax1.config(fg="black", font=("Arial", 11)) 
            enklmax1 = tk.Entry(lfmax,textvariable = Var_Klmin, width=6)
            enklmax1.grid(row=1, column=4, ipadx=0.25, pady=5)

         





            
            lfpmax = tk.Label(master=lfmax, text="cosΦ")
            lfpmax.grid(row=0, column=6, sticky=W, padx=5, pady=5)
            lfpmax.config(fg="black", font=("Arial", 11)) 
            enfpmax = tk.Entry(lfmax,textvariable = Var_fpmax, width=6)
            enfpmax.grid(row=0, column=7, ipadx=0.25, pady=5)

            lfpmax1 = tk.Label(master=lfmax, text="cosΦ")
            lfpmax1.grid(row=1, column=6, sticky=W, padx=5, pady=5)
            lfpmax1.config(fg="black", font=("Arial", 11)) 
            enfpmax1 = tk.Entry(lfmax,textvariable = Var_fpmin, width=6)
            enfpmax1.grid(row=1, column=7, ipadx=0.25, pady=5)

     

            
            lfpmax = tk.Label(master=lfmax, text="Angulo[°]")
            lfpmax.grid(row=0, column=9, sticky=W, padx=5, pady=5)
            lfpmax.config(fg="black", font=("Arial", 11)) 
            enfpmax = tk.Entry(lfmax,textvariable = Var_angulomax, width=6)
            enfpmax.grid(row=0, column=10, ipadx=0.25, pady=5)

            lfpmax1 = tk.Label(master=lfmax, text="Angulo[°]")
            lfpmax1.grid(row=1, column=9, sticky=W, padx=5, pady=5)
            lfpmax1.config(fg="black", font=("Arial", 11)) 
            enfpmax1 = tk.Entry(lfmax,textvariable = Var_angulomin, width=6)
            enfpmax1.grid(row=1, column=10, ipadx=0.25, pady=5)

      


    
            lHmax = tk.Label(master=lfmax, text="Hora")
            lHmax.grid(row=0, column=12, sticky=W, padx=5, pady=5)
            lHmax.config(fg="black", font=("Arial", 11)) 
            enHmax = tk.Entry(lfmax,textvariable = Var_h, width=6)
            enHmax.grid(row=0, column=13, ipadx=0.25, pady=5)

            lHmax1 = tk.Label(master=lfmax, text="Hora")
            lHmax1.grid(row=1, column=12, sticky=W, padx=5, pady=5)
            lHmax1.config(fg="black", font=("Arial", 11)) 
            enHmax1 = tk.Entry(lfmax,textvariable = Var_h1, width=6)
            enHmax1.grid(row=1, column=13, ipadx=0.25, pady=5)

 


            lH = tk.Label(master=lfmax, text="horas")
            lH.grid(row=0, column=14, sticky=W, padx=5, pady=5)
            lH.config(fg="black", font=("Arial", 11)) 

            lH1 = tk.Label(master=lfmax, text="horas")
            lH1.grid(row=1, column=14, sticky=W, padx=5, pady=5)
            lH1.config(fg="black", font=("Arial", 11)) 


            # buttonReporte = tk.Button(master=lfmax, text="GENERAR REPORTE", borderwidth=5, foreground="black")
            # buttonReporte.grid(row=0, column=15, padx=55, pady=5)
            #-----------------------------------------------------------------------------------------------------------------------------
            
            #-------------------------------------------------------Graficos 2d pestaña 2-------------------------------------------------
            fig = Figure(figsize=(8.1, 5))
                        
            # graficos eficiencia
            fig.subplots_adjust(left=0.08, bottom=0.10, right=0.97,
                                top=0.95, wspace=0.32, hspace=0.98)
            fig.add_subplot(321, ylabel="kl",
                            xlabel="time[h]", title="kL vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time, np_kl)
        
            fig.add_subplot(322, ylabel="Power Factor", xlabel="time[h]",
                            title="F.P. vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_fp)
            # fig.add_subplot(322, ylabel="Angle[°]", xlabel="time[h]",
            #                 title="Angle-time", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_angulo)

            fig.add_subplot(323, ylabel="η[%]", xlabel="kl",
                            title="EFFICIENCY vs kL").plot(np_kl, np_ef, 'ko')
            fig.add_subplot(324, ylabel="η[%]", xlabel="Power factor",
                            title="EFFICIENCY vs F.P.").plot(np_fp, np_ef, "ko")
            # fig.add_subplot(324, ylabel="η[%]", xlabel="Angle[°]",
            #                 title="Angle-Efficiency").plot(np_angulo, np_ef, "ko")
            
            fig.add_subplot(325, ylabel="P2c[kw]", xlabel="kl",
                            title="LOAD POWER vs kL").plot(np_kl, np_p2c/1000, 'go')              
            fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Power factor",
                            title="LOAD POWER vs F.P.").plot(np_fp, np_p2c/1000, 'go')
            # fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Angle[°]",
            #                 title="Angle-Load Power").plot(np_angulo, np_p2c/1000, 'go')
            
            canvas = FigureCanvasTkAgg(fig, master=frame18)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.X)
            
            toolbar = NavigationToolbar2Tk( canvas, frame18)
            toolbar.update()
            toolbar.pack()
                        
            #endregion
            #-------------------------------------------------------------------------------------------------------------------------


            #------------------------------------------------grafica 3D pestaña2 -----------------------------------------------------
            #region 
            # plt.style.use('dark_background')
            fig2 = plt.figure()
            canvas2 = FigureCanvasTkAgg(fig2, master=frame16)  # A tk.DrawingArea.
            canvas2.draw()
            
            ax = fig2.gca(projection ="3d")

            '''meshgrid'''
            np_klmesh, np_angulomesh = np.meshgrid(np_kl, np_angulo)
            # print(np_klmesh)
            # print(np_angulomesh)
                        
            '''factor de potencia '''
            np_fpmesh = np.array(np.cos(np_angulomesh * np.pi/180))
            # print(np_fpmesh)
            
            '''perdidas en vacio'''
            valorpo_3d = np_po 
            # print(valorpo)
                        
            ''' potencia de la carga'''
            np_p2cmesh = np.array(sn*np.multiply(np_fpmesh, np_klmesh))
            # print(np_p2cmesh)
                        
            ''' perdidas devanados'''
            valorpk_3d = np_pk
            # # print(valorpk)
         
            '''factor de corrección de temperatura tf '''

            # tf = [0.91]
            valortf = [str(entf.get())]
            Tf = np.array(valortf, dtype='f')
                                           
            ''' calculo de la eficiencia metodo B'''
                       
            Bmesh = np.multiply(valorpk_3d*Tf, np_klmesh**2)
            # print(Bmesh)
            
            N = np_p2cmesh + valorpo_3d + Bmesh
            efmesh = (np.true_divide(np_p2cmesh, N))*100
            np_efmesh = np.array(efmesh)
            # print(np_efmesh)
                        
            # surf = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, cmap=cm.coolwarm, linewidth=0, antialiased=False)
            p = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, rstride=1, cstride=1, cmap='hot')
            
            # Customize the z axis.
            # ax.set_zlim(99, 100)

            ax.zaxis.set_major_locator(LinearLocator(10))
            ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
            
            # Add a color bar which maps values to colors.
            
            # fig.colorbar(surf, shrink=0.5, aspect=5)
            
            plt.title('EFICIENCIA TRANSFORMADOR DE POTENCIA')
            plt.xlabel("kl")
            plt.ylabel('Angulo')
            
            fig.colorbar(p, ax=ax)
            
            toolbar = NavigationToolbar2Tk(canvas2, frame16)
            toolbar.update()
            canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            # canvas.get_tk_widget().grid(padx=50, pady=0, ipadx=50 ,ipady=5)
             
            #endregion
            #---------------------------------------------------------------------------------------------------------------------------



            #------------------------------------tabla factor de potencia pestaña2---------------------------------------
            lfperfil.columnconfigure(0, weight=1) 
            # resize row 0 height when the window is resized
            lfperfil.rowconfigure(0, weight=1)
            
            txt = Text(lfperfil)
            txt.grid(row=0, column=0, sticky="eswn")
            
            # scroll_y = Scrollbar(root, orient="vertical")
            scroll_y = Scrollbar(lfperfil, orient="vertical", command=txt.yview)
            scroll_y.grid(row=0, column=1, sticky="ns")
            # bind txt to scrollbar
            txt.configure(yscrollcommand=scroll_y.set,)
                                    
            very_long_list = pd.DataFrame({"Kl[%]": (np_kl), 
                                           " Angulo[°]": (np_angulo),
                                           "Factor de potencia[cosΦ]": (np_fp),
                                           "  Potencia en la carga[W]": (np_p2c),
                                           "Eficiencia η [%]": (np_ef)                                       
                                           })
            
            txt.insert("1.0", very_long_list)
            # make the text look like a label
            
            txt.configure(state="disabled", relief="flat", bg=lfperfil.cget("bg"))
            #-------------------------------------------------------------------------------------------------------------
            #-------------------------------------------------------------------------------------------------------------
            def exportCSV ():
                messagebox.showinfo("REPORTE DE DATOS", "la información calculada se almacena en un docuemento con extención .CSV")
                export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
                very_long_list.to_csv (export_file_path, index = False, header=True)

            buttonReporte = tk.Button(master=lfdatos, text="GUARDAR DATOS", borderwidth=5, foreground="black",command=exportCSV)
            buttonReporte.grid(row=6, column=0, padx=55, pady=5)

            #---------------------------------------------------------------------------------------------------------------
         
        #-------------------------------------------------------Botones pestaña 2-------------------------------------------------------
        button5 = tk.Button(master=lfdatos, text="Calcular", borderwidth=5, foreground="black",command=cargar)
        button5.grid(row=6, column=1, padx=5, pady=5)
        
        # buttonperfil = tk.Button(master=lfdatos, text="CARGAR PERFIL", relief="flat", borderwidth=5, foreground="black" )
        # buttonperfil.grid(row=6, column=0, padx=0, pady=5)
       
        #-------------------------------------------------------------------------------------------------------------------------------+

        return set(pestaña2)
        #endregion
    #-------------------------------------------------------------------------------------------------------------------------------------------- 







    #-------------------------------- función para abrir pestaña ejemplo 1(MétodoA)--------------------------------------------------------------
    #region
    def ejemplo1():
        pes2 = tk.Frame(nb)
        pestaña2 = nb.add(pes2, text='Ejemplo método A')
        
        #frames pestaña datos necesarios 
        frame7 = tk.Frame(pes2, width=720, height=100)
        frame7.grid(column=0, row=0,ipady=0)

        frame8 = tk.Frame(pes2, width=500, height=315)
        frame8.grid(column=0, row=1, ipady=0,padx=10, pady=10)
    
        frame9 = tk.Frame(pes2, width=720, height=5)
        frame9.grid(column=1, row=0)

        frame10 = tk.Frame(pes2, width=800, height=300)
        frame10.grid(column=1, row=1,padx=10, pady=10)

        #---------------------------------------------------label frames pestaña Ejemplo 1---------------------------------------------------
        lfdatos1 = tk.LabelFrame(master=frame7, text="Datos:")
        lfdatos1.grid(padx=1, pady=1, ipadx=5 ,ipady=0)

        lfperfil1 = tk.LabelFrame(master=frame9, text="Perfil de carga:")
        lfperfil1.grid(padx=40, pady=0, ipadx=380 ,ipady=90)
        lfperfil1.grid_propagate(False)
        lfmax = tk.LabelFrame(master=frame9, text="Máxima eficiencia:")
        lfmax.grid(padx=40, pady=0, ipadx=280 ,ipady=30)
        lfmax.grid_propagate(False)
        #-----------------------------------------------------------------------------------------------------------------------------------
        
        #entradas texto lfdatos
        lsn = tk.Label(master=lfdatos1, text="Ptencia nominal Sn [KVA] ")
        lsn.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        ensn = tk.Entry(lfdatos1)
        ensn.insert(0, "168000")
        ensn.grid(row=0, column=1, padx=5, pady=5)

        lpo = tk.Label(master=lfdatos1, text="Potencia de perdidas en vacio[kW] ")
        lpo.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        enpo = tk.Entry(lfdatos1)
        enpo.insert(0, "44.7100")
        enpo.grid(row=1, column=1, padx=5, pady=5)

        lpk = tk.Label(master=lfdatos1, text="Potencia de perdidas con carga[kW] ")
        lpk.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        enpk = tk.Entry(lfdatos1)
        enpk.insert(0, "325.3793")
        enpk.grid(row=2, column=1, padx=5, pady=5)

        lpco = tk.Label(master=lfdatos1, text="Potencia de perdidas sistema de refrigeración en vacío [kW] ")
        lpco.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        enpco = tk.Entry(lfdatos1)
        enpco.insert(0, "8")
        enpco.grid(row=3, column=1, padx=5, pady=5)
        
        lpkk = tk.Label(master=lfdatos1, text="Potencia de perdidas sistema de refrigeración en vacío [kW] ")
        lpkk.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        enpkk = tk.Entry(lfdatos1)
        enpkk.insert(0, "10")
        enpkk.grid(row=4, column=1, padx=5, pady=5)
        
        # aquí datos para calculo
        Kl = [0.8000,
                  0.2900,
                  0.2700,
                  0.2600,
                  0.2800,
                  0.3700,
                  0.5100,
                  0.5100,
                  0.4600,
                  0.5000,
                  0.5300,
                  0.5500,
                  0.5800,
                  0.5500,
                  0.5100,
                  0.4800,
                  0.4600,
                  0.4800,
                  0.5900,
                  0.9000,
                  1,
                  0.9300,
                  0.7600,
                  0.5300, ]
        
        Angulo = [-56.00,
                      - 20.30,
                      - 18.90,
                      - 18.20,
                      - 19.60,
                      - 25.90,
                      - 35.70,
                      - 35.70,
                      - 32.20,
                      - 35.00,
                      - 37.10,
                      - 38.50,
                      - 40.60,
                      - 38.50,
                      - 35.70,
                      - 33.60,
                      - 32.20,
                      - 33.60,
                      - 41.30,
                      - 63.00,
                      - 70.00,
                      - 65.10,
                      - 53.20,
                      - 37.10,
                      ]
        
        
        
        #-----------------------------------------------Graficos 2d pestaña ejemplo 1----------------------------------------------
        #region 
        
        "convierte en array los vectores "
        np_kl = np.array(Kl)
        # print(np_kl)
        
        np_angulo = np.array(Angulo)
        # print(np_angulo)
        
        '''tiempo perfil de carga '''
        t = np.arange(0, 24, 1)
        np_time = np.array(t)
        # print(np_time)
        
        '''perdidas en vacio'''
        v1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                    
        valorpo = [44.7100225]
        print(valorpo)
        po = np.array(valorpo, dtype='f')
        # print(po)
        
        np_po = np.array(np.multiply(po, v1))
        # print(np_po)
                    
        '''factor de potencia '''
        def fp(a):
            return np.cos(a * np.pi/180)
        
        np_fp = np.array(fp(np_angulo))
        # print(np_fp)
        
        ''' potencia de la carga'''
        valorsn = [168000]
        sn = np.array(valorsn, dtype='f')
      
        
        np_p2c = np.array(sn*np.multiply(np_fp, np_kl))
        # print(np_p2c)
                    
        ''' perdidas devanados'''
        valorpk = [325.379346]
        pk = np.array(valorpk, dtype='f')
        
        np_pk = np.array(np.multiply(pk, v1))
        # print(np_pk)
        
        "potencia sistema de refrigeración sin carga "
        valorpco = [8]
        pco = np.array(valorpco, dtype='f')
        
        np_pco = np.array(np.multiply(pco, v1))
        # print(np_pco)
        
        "potencia sistema de enfriaiento con carga "
        valorpck = [10]
        pck = np.array(valorpck, dtype='f')
        
        np_pck = np.array(np.multiply(pck, v1))
        # print(np_pck)
                                
        ''' calculo de la eficiencia metodo A'''
        A = np_po + np_pco
        B = np.multiply(np_pk, np_kl**2)+np_pck
        
        N = np_p2c - A - B
        
        ef = (np.true_divide(N, np_p2c))*100
        np_ef = np.array(ef)
        # print(np_ef)
        #endregion
        #----------------------------------------------------------------------------------------------------------------------------
    
        
        #-----------------------------------------CALCULO EFICIENCIA MAXIMA Pestaña EJEMPLO 1- ---------------------------------------
        #----------------------------------------------------Valores maximos--------------------------------------------------
        efmax = np.max(np_ef)
        efmax_r = round(efmax, 2)
        # print(efmax_r)
        
        hora = np.where(np_ef==efmax)[0]
        # print(hora)
        
        h = str(hora)[1:-1]
        # print(h)
        
        klmax = np_kl[int(h)]
        klmax_r =  round(klmax, 2)
        # print(klmax)
        
        fpmax = np_fp[int(h)]
        fpmax_r = round(fpmax, 2)
        # print(fpmax)
        
        angulomax = np_angulo[int(h)]
        angulomax_r = round(angulomax, 2)
        #-------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------Stringvar maxima eficiencia ----------------------------------------
        Var_efmax = tk.StringVar()
        Var_efmax.set(efmax_r)
        
        Var_h = tk.StringVar()
        Var_h.set(h)
        Var_Klmax = tk.StringVar()
        Var_Klmax.set(klmax_r)
        Var_fpmax = tk.StringVar()
        Var_fpmax.set(fpmax_r)
        Var_angulomax = tk.StringVar()
        Var_angulomax.set(angulomax_r)
        #--------------------------------------------------------------------------------------------------------------------

        #--------------------------------------------------FRAME EFICIENCIA MAX----------------------------------------------
        lefmax = tk.Label(master=lfmax, text="Eficiencia[%] ")
        lefmax.grid(row=0, column=0, sticky=W, padx=1, pady=5)
        lefmax.config(fg="black", font=("Arial", 11)) 
        enefmax = tk.Entry(lfmax,textvariable = Var_efmax, width=6)
        enefmax.grid(row=0, column=1, ipadx=0.25, pady=5)
            
        lklmax = tk.Label(master=lfmax, text="Kl[%]")
        lklmax.grid(row=0, column=3, sticky=W, padx=1, pady=5)
        lklmax.config(fg="black", font=("Arial", 11)) 
        enklmax = tk.Entry(lfmax,textvariable = Var_Klmax, width=6)
        enklmax.grid(row=0, column=4, ipadx=0.25, pady=5)
          
        lfpmax = tk.Label(master=lfmax, text="cosΦ")
        lfpmax.grid(row=0, column=6, sticky=W, padx=5, pady=5)
        lfpmax.config(fg="black", font=("Arial", 11)) 
        enfpmax = tk.Entry(lfmax,textvariable = Var_fpmax, width=6)
        enfpmax.grid(row=0, column=7, ipadx=0.25, pady=5)
        
        lfpmax = tk.Label(master=lfmax, text="Angulo[°]")
        lfpmax.grid(row=0, column=9, sticky=W, padx=5, pady=5)
        lfpmax.config(fg="black", font=("Arial", 11)) 
        enfpmax = tk.Entry(lfmax,textvariable = Var_angulomax, width=6)
        enfpmax.grid(row=0, column=10, ipadx=0.25, pady=5)

        lHmax = tk.Label(master=lfmax, text="Hora")
        lHmax.grid(row=0, column=12, sticky=W, padx=5, pady=5)
        lHmax.config(fg="black", font=("Arial", 11)) 
        enHmax = tk.Entry(lfmax,textvariable = Var_h, width=6)
        enHmax.grid(row=0, column=13, ipadx=0.25, pady=5)
        #---------------------------------------------------------------------------------------------------------------------------------


        #-------------------------------------------------------Graficos 2d pestaña Ejemplo 1----------------------------------------------
        fig = Figure(figsize=(8.1, 5))
                    
        #graficos eficiencia
        fig.subplots_adjust(left=0.08, bottom=0.10, right=0.97,
                            top=0.95, wspace=0.32, hspace=0.98)
        fig.add_subplot(321, ylabel="kl",
                        xlabel="time[h]", title="kL vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time, np_kl)
        
        fig.add_subplot(322, ylabel="Power Factor", xlabel="time[h]",
                        title="F.P. vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_fp)
        # fig.add_subplot(322, ylabel="Angle[°]", xlabel="time[h]",
        #                 title="Angle-time", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_angulo)

        fig.add_subplot(323, ylabel="η[%]", xlabel="kL",
                        title="EFFICIENCY vs kL").plot(np_kl, np_ef, 'ko')
        fig.add_subplot(324, ylabel="η[%]", xlabel="Power factor",
                        title="EFFICIENCY vs F.P.").plot(np_fp, np_ef, "ko")
        # fig.add_subplot(324, ylabel="η[%]", xlabel="Angle[°]",
        #                 title="Angle-Efficiency").plot(np_angulo, np_ef, "ko")
        
        fig.add_subplot(325, ylabel="P2c[kw]", xlabel="kl",
                        title="LOAD POWER vs kL").plot(np_kl, np_p2c/1000, 'go')              
        fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Power factor",
                        title="LOAD POWER vs F.P.").plot(np_fp, np_p2c/1000, 'go')
        # fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Angle[°]",
        #                 title="Angle-Load Power").plot(np_angulo, np_p2c/1000, 'go')
        
        canvas = FigureCanvasTkAgg(fig, master=frame10)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.X)
        
        toolbar = NavigationToolbar2Tk( canvas, frame10)
        toolbar.update()
        toolbar.pack()
                    
        
        #-----------------------------------------------------------------------------------------------------------------------------------


        #------------------------------------------------grafica 3D  pestaña ejemplo 1 -----------------------------------------------------
        #region 
        # plt.style.use('dark_background')
        fig2 = plt.figure()
        
        canvas2 = FigureCanvasTkAgg(fig2, master=frame8)  # A tk.DrawingArea.
        canvas2.draw()
        
        ax = fig2.gca(projection ="3d")
        '''meshgrid'''
        np_klmesh, np_angulomesh = np.meshgrid(np_kl, np_angulo)
        # print(np_klmesh)
        # print(np_angulomesh)
                    
        '''factor de potencia '''
        np_fpmesh = np.array(np.cos(np_angulomesh * np.pi/180))
        # print(np_fpmesh)
        
        '''perdidas en vacio'''
        valorpo_3d = np_po 
        # print(valorpo)
                    
        ''' potencia de la carga'''
        np_p2cmesh = np.array(sn*np.multiply(np_fpmesh, np_klmesh))
        # print(np_p2cmesh)
                    
        ''' perdidas devanados'''
        valorpk_3d = np_pk
        # # print(valorpk)
        
        "potencia sistema de refrigeración sin carga "
        valorpco_3d = np_pco 
        # print(valorpco )
        
        "potencia sistema de enfriaiento con carga "
        valorpck_3d = np_pck
        # print(valorpck )
                    
        ''' calculo de la eficiencia metodo A'''
        Amesh = valorpo_3d + valorpco_3d
        # print(Amesh)
        
        Bmesh = np.multiply(valorpk_3d, np_klmesh**2)+valorpck_3d
        # print(Bmesh)
        
        N = np_p2cmesh - Amesh - Bmesh
        
        efmesh = (np.true_divide(N, np_p2cmesh))*100
        np_efmesh = np.array(efmesh)
        # print(np_efmesh)
                   
        
        # surf = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        p = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, rstride=1, cstride=1, cmap='hot')
        
        # Customize the z axis.
        ax.set_zlim(99, 100)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        
        # Add a color bar which maps values to colors.
        
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        
        plt.title('EFICIENCIA')
        plt.xlabel("kl")
        plt.ylabel('Angulo')
        
        fig.colorbar(p, ax=ax)
        
        toolbar = NavigationToolbar2Tk(canvas2, frame8)
        toolbar.update()
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # canvas.get_tk_widget().grid(padx=50, pady=0, ipadx=50 ,ipady=5)
         
        #endregion
        #---------------------------------------------------------------------------------------------------------------------------


        #-------------------------------------tabla perfil de carga pestaña ejemplo 1-----------------------------------------------

        
        lfperfil1.columnconfigure(0, weight=1) 
        # resize row 0 height when the window is resized
        lfperfil1.rowconfigure(0, weight=1)
        
        txt = Text(lfperfil1)
        txt.grid(row=0, column=0, sticky="eswn")
        
        # scroll_y = Scrollbar(root, orient="vertical")
        scroll_y = Scrollbar(lfperfil1, orient="vertical", command=txt.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        # bind txt to scrollbar
        txt.configure(yscrollcommand=scroll_y.set,)

        
        very_long_list = pd.DataFrame({"Kl[%]": (np_kl), 
                                       " Angulo[°]": (np_angulo),
                                       "Factor de potencia[cosΦ]": (np_fp),
                                       "  Potencia en la carga[W]": (np_p2c),
                                       "Eficiencia η [%]": (np_ef)                                       
                                       })
        
        txt.insert("1.0", very_long_list)
        # make the text look like a label
        
        txt.configure(state="disabled", relief="flat", bg=lfperfil1.cget("bg"))

        #--------------------------------------------------------------------------------------------------------------------

        return set(ejemplo1)
    #endregion

    #--------------------------------------------------------------------------------------------------------------------------------------------








  #-------------------------------- función para abrir pestaña ejemplo 2 (Método B)--------------------------------------------------------------
    #region
    def ejemplo2():

        pes3 = tk.Frame(nb)
        pestaña3 = nb.add(pes3, text='Ejemplo método B')
        
        #-------------------------------------------------Frames pestaña  Ejemplo 2---------------------------------------------------- 

        frame11 = tk.Frame(pes3, width=720, height=300)
        frame11.grid(column=0, row=0,ipady=0)

        frame12 = tk.Frame(pes3, width=720, height=200)
        frame12.grid(column=0, row=1, ipady=0,padx=10, pady=10)
    
        frame13 = tk.Frame(pes3, width=800, height=300)
        frame13.grid(column=1, row=0)

        frame14 = tk.Frame(pes3, width=800, height=200)
        frame14.grid(column=1, row=1,padx=10, pady=10)
        #--------------------------------------------------------------------------------------------------------------------------------

      

        #-----------------------------------------------------------Label frames Pestaña Ejemplo 2-----------------------------------
        lfdatos1 = tk.LabelFrame(master=frame11, text="Datos:")
        lfdatos1.grid(padx=50, pady=10, ipadx=50 ,ipady=5)

        lfperfil1 = tk.LabelFrame(master=frame13, text="Perfil de carga:")
        lfperfil1.grid(padx=40, pady=0, ipadx=380 ,ipady=90)
        lfperfil1.grid_propagate(False)
        lfmax = tk.LabelFrame(master=frame13, text="Máxima eficiencia:")
        lfmax.grid(padx=40, pady=0, ipadx=260 ,ipady=30)
        lfmax.grid_propagate(False)
        #-----------------------------------------------------------------------------------------------------------------------------
        
        #------------------------------------Entradas texto lfdatos Pestaña Ejemplo 2-------------------------------------------------
        lsn = tk.Label(master=lfdatos1, text="Ptencia nominal Sn [KVA] ")
        lsn.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        ensn = tk.Entry(lfdatos1)
        ensn.insert(0, "200000")
        ensn.grid(row=0, column=1, padx=5, pady=5)

        lpo = tk.Label(master=lfdatos1, text="Potencia de perdidas en vacio[kW] ")
        lpo.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        enpo = tk.Entry(lfdatos1)
        enpo.insert(0, "62.5223")
        enpo.grid(row=1, column=1, padx=5, pady=5)

        lpk = tk.Label(master=lfdatos1, text="Potencia de perdidas con carga[kW] ")
        lpk.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        enpk = tk.Entry(lfdatos1)
        enpk.insert(0, "394.186")
        enpk.grid(row=2, column=1, padx=5, pady=5)

                
        # aquí datos para calculo
        Kl = [0.8000,
                  0.2900,
                  0.2700,
                  0.2600,
                  0.2800,
                  0.3700,
                  0.5100,
                  0.5100,
                  0.4600,
                  0.5000,
                  0.5300,
                  0.5500,
                  0.5800,
                  0.5500,
                  0.5100,
                  0.4800,
                  0.4600,
                  0.4800,
                  0.5900,
                  0.9000,
                  1,
                  0.9300,
                  0.7600,
                  0.5300, ]
        
        Angulo = [ 50.2451,
            47.0338, 
            36.2500, 
            38.3751, 
            33.0966, 
            27.4247, 
            21.5631, 
            15.6698, 
            12.2900, 
            10.0000, 
            10.0000, 
             9.0000, 
            13.2320, 
            15.0600, 
            24.9992, 
            30.7731, 
            36.2409, 
            41.1959, 
            45.4749, 
            49.0003, 
            51.7848, 
            53.9021, 
            52.0026, 
            49.0032, 
                      ]
        
        #-----------------------------------------------Graficos 2d pestaña ejemplo 2----------------------------------------------
        #region 
        
        "convierte en array los vectores "
        np_kl = np.array(Kl)
        # print(np_kl)
        
        np_angulo = np.array(Angulo)
        # print(np_angulo)
        
        '''tiempo perfil de carga '''
        t = np.arange(0, 24, 1)
        np_time = np.array(t)
        # print(np_time)
        
        
        '''perdidas en vacio'''
        v1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                    
        valorpo = [62.5223]
        # valorpo = [str(enpo.get())]
        # print(valorpo)
        po = np.array(valorpo, dtype='f')
        # print(po)
        
        np_po = np.array(np.multiply(po, v1))
        # print(np_po)
                    
        '''factor de potencia '''
        def fp(a):
            return np.cos(a * np.pi/180)
        
        np_fp = np.array(fp(np_angulo))
        # print(np_fp)
        
        ''' potencia de la carga'''
        valorsn = [200000]
        # valorsn = [str(ensn.get())]
        sn = np.array(valorsn, dtype='f')
      
        
        np_p2c = np.array(sn*np.multiply(np_fp, np_kl))
        # print(np_p2c)
                    
        ''' perdidas devanados'''
        valorpk = [394.186]
        # valorpk = [str(enpk.get())]
        pk = np.array(valorpk, dtype='f')
        
        np_pk = np.array(np.multiply(pk, v1))
        # print(np_pk)
        
        "factor de corrección de temperatura tf "
        tf = [0.91]
        # valorpco = [str(enpco.get())]
        Tf = np.array(tf, dtype='f')
        
        
                                

        ''' calculo de la eficiencia metodo B'''
        A = np_po 
        B = np.multiply(np_pk*Tf, np_kl**2)
        
        N = np_p2c + A + B
        
        ef = (np.true_divide(np_p2c, N))*100
        np_ef = np.array(ef)
        # print(np_ef)
        
        #-----------------------------------------CALCULO EFICIENCIA MAXIMA Pestaña 2- ---------------------------------------

        #----------------------------------------------------Valores maximos--------------------------------------------------
        efmax = np.max(np_ef)
        efmax_r = round(efmax, 2)
        # print(efmax_r)
        
        hora = np.where(np_ef==efmax)[0]
        # print(hora)
        
        h = str(hora)[1:-1]
        # print(h)
        
        klmax = np_kl[int(h)]
        klmax_r =  round(klmax, 2)
        # print(klmax)
        
        fpmax = np_fp[int(h)]
        fpmax_r = round(fpmax, 2)
        # print(fpmax)
        
        angulomax = np_angulo[int(h)]
        angulomax_r = round(angulomax, 2)
        #-------------------------------------------------------------------------------------------------------------------

        #-----------------------------------------------Stringvar maxima eficiencia ----------------------------------------
        Var_efmax = tk.StringVar()
        Var_efmax.set(efmax_r)
        
        Var_h = tk.StringVar()
        Var_h.set(h)

        Var_Klmax = tk.StringVar()
        Var_Klmax.set(klmax_r)

        Var_fpmax = tk.StringVar()
        Var_fpmax.set(fpmax_r)

        Var_angulomax = tk.StringVar()
        Var_angulomax.set(angulomax_r)
        #------------------------------------------------------------------------------------------------------------------

        #--------------------------------------------------FRAME EFICIENCIA MAX----------------------------------------------
        lefmax = tk.Label(master=lfmax, text="Eficiencia[%] ")
        lefmax.grid(row=0, column=0, sticky=W, padx=1, pady=5)
        lefmax.config(fg="black", font=("Arial", 11)) 
        enefmax = tk.Entry(lfmax,textvariable = Var_efmax, width=6)
        enefmax.grid(row=0, column=1, ipadx=0.25, pady=5)
            
        lklmax = tk.Label(master=lfmax, text="Kl[%]")
        lklmax.grid(row=0, column=3, sticky=W, padx=1, pady=5)
        lklmax.config(fg="black", font=("Arial", 11)) 
        enklmax = tk.Entry(lfmax,textvariable = Var_Klmax, width=6)
        enklmax.grid(row=0, column=4, ipadx=0.25, pady=5)
          
        lfpmax = tk.Label(master=lfmax, text="cosΦ")
        lfpmax.grid(row=0, column=6, sticky=W, padx=5, pady=5)
        lfpmax.config(fg="black", font=("Arial", 11)) 
        enfpmax = tk.Entry(lfmax,textvariable = Var_fpmax, width=6)
        enfpmax.grid(row=0, column=7, ipadx=0.25, pady=5)
        
        lfpmax = tk.Label(master=lfmax, text="Angulo[°]")
        lfpmax.grid(row=0, column=9, sticky=W, padx=5, pady=5)
        lfpmax.config(fg="black", font=("Arial", 11)) 
        enfpmax = tk.Entry(lfmax,textvariable = Var_angulomax, width=6)
        enfpmax.grid(row=0, column=10, ipadx=0.25, pady=5)
    
        lHmax = tk.Label(master=lfmax, text="Hora")
        lHmax.grid(row=0, column=12, sticky=W, padx=5, pady=5)
        lHmax.config(fg="black", font=("Arial", 11)) 
        enHmax = tk.Entry(lfmax,textvariable = Var_h, width=6)
        enHmax.grid(row=0, column=13, ipadx=0.25, pady=5)
        #-----------------------------------------------------------------------------------------------------------------------------
        #-------------------------------------------------------Graficos 2d pestaña Ejemplo 2-------------------------------------------------
        fig = Figure(figsize=(8.1, 5))
                    
        # graficos eficiencia
        fig.subplots_adjust(left=0.08, bottom=0.10, right=0.97,
                            top=0.95, wspace=0.32, hspace=0.98)
        fig.add_subplot(321, ylabel="kl",
                        xlabel="time[h]", title="kL vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time, np_kl)
    
        fig.add_subplot(322, ylabel="Power Factor", xlabel="time[h]",
                        title="F.P. vs TIME", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_fp)
        # fig.add_subplot(322, ylabel="Angle[°]", xlabel="time[h]",
        #                 title="Angle-time", xlim=(0,23),xticks=([0,3,6,9,12,15,17,20,23])).plot(np_time,  np_angulo
        fig.add_subplot(323, ylabel="η[%]", xlabel="kl",
                        title="EFFICIENCY vs kL").plot(np_kl, np_ef, 'ko')
        fig.add_subplot(324, ylabel="η[%]", xlabel="Power factor",
                        title="EFFICIENCY vs F.P.").plot(np_fp, np_ef, "ko")
        # fig.add_subplot(324, ylabel="η[%]", xlabel="Angle[°]",
        #                 title="Angle-Efficiency").plot(np_angulo, np_ef, "ko")
        
        fig.add_subplot(325, ylabel="P2c[kw]", xlabel="kl",
                        title="LOAD POWER vs kL").plot(np_kl, np_p2c/1000, 'go')              
        fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Power factor",
                        title="LOAD POWER vs F.P.").plot(np_fp, np_p2c/1000, 'go')
        # fig.add_subplot(326, ylabel="P2c[kw]", xlabel="Angle[°]",
        #                 title="Angle-Load Power").plot(np_angulo, np_p2c/1000, 'go')
        
        canvas = FigureCanvasTkAgg(fig, master=frame14)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.X)
        
        toolbar = NavigationToolbar2Tk( canvas, frame14)
        toolbar.update()
        toolbar.pack()
                    
        #endregion
        #-------------------------------------------------------------------------------------------------------------------------

        #------------------------------------------------grafica 3D  pestaña ejemplo 2 -----------------------------------------------------
        #region 
        # plt.style.use('dark_background')
        fig2 = plt.figure()
        
        canvas2 = FigureCanvasTkAgg(fig2, master=frame12)  # A tk.DrawingArea.
        canvas2.draw()
        
        ax = fig2.gca(projection ="3d")
        '''meshgrid'''
        np_klmesh, np_angulomesh = np.meshgrid(np_kl, np_angulo)
        # print(np_klmesh)
        # print(np_angulomesh)
                    
        '''factor de potencia '''
        np_fpmesh = np.array(np.cos(np_angulomesh * np.pi/180))
        # print(np_fpmesh)
        
        '''perdidas en vacio'''
        valorpo_3d = np_po 
        # print(valorpo)
                    
        ''' potencia de la carga'''
        np_p2cmesh = np.array(sn*np.multiply(np_fpmesh, np_klmesh))
        # print(np_p2cmesh)
                    
        ''' perdidas devanados'''
        valorpk_3d = np_pk
        # # print(valorpk)

        '''factor de corrección de temperatura tf '''
        tf = [0.91]
                                           
        ''' calculo de la eficiencia metodo B'''
               
        Bmesh = np.multiply(valorpk_3d*tf, np_klmesh**2)
        # print(Bmesh)
        
        N = np_p2cmesh + valorpo_3d + Bmesh
        
        efmesh = (np.true_divide(np_p2cmesh, N))*100
        np_efmesh = np.array(efmesh)
        # print(np_efmesh)
                   
        
        # surf = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, cmap=cm.coolwarm, linewidth=0, antialiased=False)
        p = ax.plot_surface(np_klmesh, np_angulomesh, np_efmesh, rstride=1, cstride=1, cmap='hot')
        
        # Customize the z axis.
        ax.set_zlim(99.33, 100)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        
        # Add a color bar which maps values to colors.
        
        # fig.colorbar(surf, shrink=0.5, aspect=5)
        
        plt.title('Eficiencia')
        plt.xlabel("kl")
        plt.ylabel('Angulo')
        
        fig.colorbar(p, ax=ax)
        
        toolbar = NavigationToolbar2Tk(canvas2, frame12)
        toolbar.update()
        canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # canvas.get_tk_widget().grid(padx=50, pady=0, ipadx=50 ,ipady=5)
         
        #endregion
        #---------------------------------------------------------------------------------------------------------------------------

        #------------ -------------------------------------- -tabla Perfil de carga  pestaña ejemplo 2-  --------------------------
        
        lfperfil1.columnconfigure(0, weight=1) 
        # resize row 0 height when the window is resized
        lfperfil1.rowconfigure(0, weight=1)
        
        txt = Text(lfperfil1)
        txt.grid(row=0, column=0, sticky="eswn")
        
        # scroll_y = Scrollbar(root, orient="vertical")
        scroll_y = Scrollbar(lfperfil1, orient="vertical", command=txt.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")
        # bind txt to scrollbar
        txt.configure(yscrollcommand=scroll_y.set,)
        
  
        very_long_list = pd.DataFrame({"Kl[%]": (np_kl), 
                                       " Angulo[°]": (np_angulo),
                                       "Factor de potencia[cosΦ]": (np_fp),
                                       "  Potencia en la carga[W]": (np_p2c),
                                       "Eficiencia η [%]": (np_ef)                                       
                                       })
        
        txt.insert("1.0", very_long_list)
        # make the text look like a label
        
        txt.configure(state="disabled", relief="flat", bg=lfperfil1.cget("bg"))


        #----------------------------------------------------------------------------------------------------------------
        return set(ejemplo2)
        #endregion
  #----------------------------------------------------------------------------------------------------------------------------------------------










    #----------------------------  -------------------------  cuadro portada Pestaña principal-----------------------------------------------
    # #labels
    # ldatos0 = tk.Label(master=fdatos, text='UNIVERSIDAD DEL VALLE')
    # # ldatos0.grid( padx=0, pady=0, ipadx=0, ipady=0)
    # ldatos0.grid(padx=0, pady=0)
    # ldatos0.config(fg="black", font=("Arial", 20)) 


    # ldatos1 = tk.Label(master=fdatos, text='Grupo de investigación en Alta Tensión (GRALTA)')
    # ldatos1.grid( padx=0, pady=1)
    # ldatos1.config(fg="black", font=("Arial", 15)) 
 
    #imagen
    # img2 = tk.PhotoImage(file = 'logo_eflab(2).png')
    img2 = tk.PhotoImage(file = 'img/LOGO.png')
    ltlogo = tk.Label(master=fdatos, image= img2) 
    ltlogo.grid()

    ldatos2 = tk.Label(master=fdatos, text='TRABAJO DE GRADO')
    ldatos2.grid( padx=0, pady=2)
    ldatos2.config(fg="black", font=("Arial", 15)) 


    ldatos3 = tk.Label(master=fdatos, text='GUSTAVO ADOLFO ARTEAGA ESTACIO')
    ldatos3.grid( padx=0, pady=3)
    ldatos3.config(fg="black", font=("Arial", 15)) 

    ldatos4 = tk.Label(master=fdatos, text='DIRECTORES: EDUARDO MARLÉS SÁENZ M.Sc, EDUARDO GÓMEZ LUNA PhD.')
    ldatos4.grid( padx=0, pady=0)
    ldatos4.config(fg="black", font=("Arial", 13)) 

    ldatos5 = tk.Label(master=fdatos, text='2020')
    ldatos5.grid( padx=0, pady=0)
    ldatos5.config(fg="black", font=("Arial", 13)) 
    #---------------------------------------------------------------------------------------------------------------------------------












    #------------------------------------------------------Botones pagina principal--------------------------------------------------------------------
    #-------------------------------------------------BOTON METODO A-----------------------------------------------------------------------------------
    button1 = tk.Button(master=lfstar, text="Calcular eficiencia con el método A", borderwidth=5, command=pestaña1)
    button1.grid( padx=35, pady=15)
    button1.config(fg="black", font=("Arial", 11,"bold")) 
    button1.grid(column=0, row=0)

    #BOTON AYUDA
    def ayudaMA():
          messagebox.showinfo("Cálculo utilizando el método A", "Utilizar este metodo si conoce la potencia de pérdidas del sistema de refigeración") 
    
    photo=tk.PhotoImage(file="img/help_question_1566.png")
    button_perfil1 = tk.Button(master=lfstar,image=photo, text="",  relief="flat", foreground="black",command= ayudaMA)
    button_perfil1.grid(column=1, row=0)
    button_perfil1.config(fg="black", font=("Arial", 11,"bold")) 
    #------------------------------------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------BOTON METODO B-----------------------------------------------------------------------------------
    button0 = tk.Button(master=lfstar, text="Calcular eficiencia con el método B", borderwidth=5, foreground="black", command=pestaña2)
    button0.grid( padx=35, pady=18)
    button0.config(fg="black", font=("Arial", 11,"bold")) 
    button0.grid(column=0, row=1)
    #BOTON AYUDA
    def ayudaMB():
          messagebox.showinfo("Cálculo utilizando el método B", "Utilizar este metodo si NO conoce la potencia de pérdidas del sistema de refigeración") 
    
    photo1=tk.PhotoImage(file="img/help_question_1566.png")
    button_ayuda1 = tk.Button(master=lfstar,image=photo1, text="", relief="flat",foreground="black",command= ayudaMB)
    button_ayuda1.grid(column=1, row=1)
    button_ayuda1.config(fg="black", font=("Arial", 11,"bold")) 
    #------------------------------------------------------------------------------------------------------------------------------------------------


    button3 = tk.Button(master=lfexamples, text="Ejemplo eficiencia con el método B", borderwidth=5, foreground="black",command=ejemplo2 )
    # button3 = tk.Button(master=lfexamples, text="Ejemplo eficiencia con el método B", borderwidth=5, foreground="black",command=ejemplo2 )
    # button3.grid(padx=15,pady=15)
    button3.grid( padx=65, pady=15)
    button3.config(fg="black", font=("Arial", 11,"bold")) 
    button3.grid(column=0, row=0)
    
    button5 = tk.Button(master=lfexamples, text="Ejemplo eficiencia con el método A", borderwidth=5, foreground="black",command=ejemplo1 )
    # button5 = tk.Button(master=lfexamples, text="Ejemplo eficiencia con el método A", borderwidth=5, foreground="black",command=ejemplo1 )
    button5.grid( padx=65, pady=18)
    button5.config(fg="black", font=("Arial", 11,"bold")) 
    button5.grid(column=0, row=1)
    #-----------------------------------------------------------------------------------------------------------------------------------------------------

   #------------------------------------------------texto about Pagina principal--------------------------------------------------------------------------
    texto = tk.Label(master=lfhelp,text=("EFLAB es una aplicación de escritorio  "))
    texto.grid( ipadx=10, pady=9)
    texto.config(fg="black", font=("Arial", 11)) 
    texto = tk.Label(master=lfhelp,text=("desarollada en PYTHON que estima las regiones"))
    texto.grid( ipadx=10, pady=2)
    texto.config(fg="black", font=("Arial", 11)) 
    texto = tk.Label(master=lfhelp,text=("eficientes de un transfromador de potencia"))
    texto.grid( ipadx=10, pady=2)
    texto.config(fg="black", font=("Arial", 11)) 
    texto = tk.Label(master=lfhelp,text=(" basado en el estandar internacional IEC60076-20"))
    texto.grid( ipadx=10, pady=2)
    texto.config(fg="black", font=("Arial", 11)) 
   #----------------------------------------------------------------------------------------------------------------------------------------------------


    ventana.mainloop()
