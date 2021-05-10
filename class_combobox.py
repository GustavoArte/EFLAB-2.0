# from firebase import firebase
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db



class ObtenerDatos:

    def __init__(self, lista_combo):
        self.lista_combo = lista_combo
        # self.widgets()

        # self.firebase = firebase.FirebaseApplication(
        #     "https://eflab-perfiles.firebaseio.com/", None)

        self.cred = credentials.Certificate("eflab-perfiles-firebase-adminsdk-0mnlw-eb92679d69.json")
        firebase_admin.initialize_app(self.cred,{'databaseURL': 'https://eflab-perfiles.firebaseio.com'})



    def widgets(self):
        # self.opciones = ["Perfil de carga 1", "Perfil de carga 2", "Perfil de carga 3", "Perfil Caso 1", "Perfil Caso 2", "Perfil Caso 2", "Perfil Caso 4 T1", "Perfil Caso 4 T2"]
        self.opciones = ["perfil_1", "perfil_2", "perfil_3", "perfil_CASO_1", "perfil_CASO_2", "perfil_CASO_3", "perfil_CASO_4_T1", "perfil_CASO_4_T2"]
        # self.opciones.append("Perfil de carga 4")
        self.lista_combo = ttk.Combobox(master=self.combobox, values=self.opciones, state= "readonly")
        self.lista_combo.configure(width=25)
        self.lista_combo.grid(row=5, column=1, padx=0, pady=5)
                

        # self.button0 = ttk.Button(text='Cargar', command=self.ConsumirPerfil)
        # self.button0.grid(row=5, column=4, padx=2, pady=3)

        # #condicional para bloquar boton
        # if (self.button0['state'] == tk.NORMAL):
        #     self.button0['state'] = tk.DISABLED
            
        # else:
        #     self.button0['state'] = tk.NORMAL
     
    def SetOpciones(self,opciones):
        self.opciones = opciones
        

    def ConsumirPerfil(self):
 
        #--------------------PERFIL 1----------------
        if self.lista_combo.get() == self.opciones[0]:

            self.ref = db.reference("perfil_1")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')

            
            # A = self.firebase.get(
            #     '/perfil_1/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_1/Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]

        #--------------------PERFIL 2----------------
        elif self.lista_combo.get() == self.opciones[1]:
            # A = self.firebase.get(
            #     '/perfil_2/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_2/Kl', '')
            self.ref = db.reference("perfil_2")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]
        
        
        #--------------------PERFIL 3----------------
        elif self.lista_combo.get() == self.opciones[2]:
            # A = self.firebase.get(
            #     '/perfil_3/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_3/Kl', '')
            self.ref = db.reference("perfil_3")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]

        #--------------------PERFIL CASO 1----------------
        elif self.lista_combo.get() == self.opciones[3]:
            # A = self.firebase.get(
            #     '/perfil_CASO_1/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_CASO_1/Kl', '')
            self.ref = db.reference("perfil_CASO_1")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]

        #--------------------PERFIL CASO 2----------------
        elif self.lista_combo.get() == self.opciones[4]:
            # A = self.firebase.get(
            #     '/perfil_CASO_2/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_CASO_2/Kl', '')
            self.ref = db.reference("perfil_CASO_2")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]

        #--------------------PERFIL CASO 3----------------
        elif self.lista_combo.get() == self.opciones[5]:
            # A = self.firebase.get(
            #     '/perfil_CASO_3/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_CASO_3/Kl', '')
            self.ref = db.reference("perfil_CASO_3")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]

        #--------------------PERFIL CASO 4 T1----------------
        elif self.lista_combo.get() == self.opciones[6]:
            # A = self.firebase.get(
            #     '/perfil_CASO_4_T1/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_CASO_4_T1/Kl', '')
            self.ref = db.reference("perfil_CASO_4_T1")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]

        #--------------------PERFIL CASO 4 T2----------------
        elif self.lista_combo.get() == self.opciones[7]:
            # A = self.firebase.get(
            #     '/perfil_CASO_4_T2/Angulo', '')
            # K = self.firebase.get(
            #     '/perfil_CASO_4_T2/Kl', '')
            self.ref = db.reference("perfil_CASO_4_T2")
            self.best_sellers = self.ref.get()

            A = self.best_sellers.get('Angulo', '')
            K = self.best_sellers.get('Kl', '')


            self.Angulo = [np.array(A['A01'], dtype='f'),
                      np.array(A['A02'], dtype='f'),
                      np.array(A['A03'], dtype='f'),
                      np.array(A['A04'], dtype='f'),
                      np.array(A['A05'], dtype='f'),
                      np.array(A['A06'], dtype='f'),
                      np.array(A['A07'], dtype='f'),
                      np.array(A['A08'], dtype='f'),
                      np.array(A['A09'], dtype='f'),
                      np.array(A['A10'], dtype='f'),
                      np.array(A['A11'], dtype='f'),
                      np.array(A['A12'], dtype='f'),
                      np.array(A['A13'], dtype='f'),
                      np.array(A['A14'], dtype='f'),
                      np.array(A['A15'], dtype='f'),
                      np.array(A['A16'], dtype='f'),
                      np.array(A['A17'], dtype='f'),
                      np.array(A['A18'], dtype='f'),
                      np.array(A['A19'], dtype='f'),
                      np.array(A['A20'], dtype='f'),
                      np.array(A['A21'], dtype='f'),
                      np.array(A['A22'], dtype='f'),
                      np.array(A['A23'], dtype='f'),
                      np.array(A['A24'], dtype='f'), ]

            self.Kl = [np.array(K['K01'], dtype='f'),
                  np.array(K['K02'], dtype='f'),
                  np.array(K['K03'], dtype='f'),
                  np.array(K['K04'], dtype='f'),
                  np.array(K['K05'], dtype='f'),
                  np.array(K['K06'], dtype='f'),
                  np.array(K['K07'], dtype='f'),
                  np.array(K['K08'], dtype='f'),
                  np.array(K['K09'], dtype='f'),
                  np.array(K['K10'], dtype='f'),
                  np.array(K['K11'], dtype='f'),
                  np.array(K['K12'], dtype='f'),
                  np.array(K['K13'], dtype='f'),
                  np.array(K['K14'], dtype='f'),
                  np.array(K['K15'], dtype='f'),
                  np.array(K['K16'], dtype='f'),
                  np.array(K['K17'], dtype='f'),
                  np.array(K['K18'], dtype='f'),
                  np.array(K['K19'], dtype='f'),
                  np.array(K['K20'], dtype='f'),
                  np.array(K['K21'], dtype='f'),
                  np.array(K['K22'], dtype='f'),
                  np.array(K['K23'], dtype='f'),
                  np.array(K['K24'], dtype='f'), ]


    def getAngulo(self):
        np_angulo = np.array(self.Angulo)
        return np_angulo

    def getKl(self):
        np_kl = np.array(self.Kl)
        return np_kl


 
