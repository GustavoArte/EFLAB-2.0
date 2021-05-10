import numpy as np

import tkinter as tk
from tkinter import ttk
import pandas as pd


root = tk.Tk()
root.config(width=60300, height=200)



#----------------------------------------------------------frames-------------------------------------------------------------

# frame1 = tk.Frame(pes0, width=530, height=850, background="Blue" )
frame1 = tk.Frame(root, width=300, height=200)
frame1.grid(column=0, row=0)
  
# # frame2 = tk.Frame(pes0, width=990, height=850, background="Green" )
# frame2 = tk.Frame(root, width=50000, height=200)
# frame2.grid(column=1, row=0)

texto = tk.Label(master=frame1,text=("PERFIL DE CARGA "))
texto.grid( ipadx=10, pady=9)
texto.config(fg="black", font=("Arial", 11)) 

Botoncagar = tk.Button(master=frame1, text="CARGAR PERFIL", borderwidth=5, foreground="black")
Botoncagar.grid(row=2, column=0, padx=55, pady=5)


datos = pd.read_csv('cargar_perfil.csv')
df = pd.DataFrame(datos)
print(datos)
# num = df['Kl[%]'].str.extract('(\d+(?:\.\d+)?)')
# print(num)

num = df.groupby("Kl[%]").count()

print(num )


# #LISTA ELEMENTOS KL 
# lKL = tk.Label(master=frame1, text="kl")
# lKL.grid(row=2, column=1, padx=0, pady=5)
# lKL.config(fg="black", font=("Arial", 11)) 



# lKL00 = tk.Label(master=frame1, text="00")
# lKL00.grid(row=3, column=0, padx=0, pady=5)
# lKL00.config(fg="black", font=("Arial", 11)) 
# eKL00 = tk.Entry(frame1, width=13)
# eKL00.grid(row=3, column=1, padx=0, pady=5)

# lKL01 = tk.Label(master=frame1, text="01")
# lKL01.grid(row=4, column=0, padx=0, pady=5)
# lKL01.config(fg="black", font=("Arial", 11)) 
# eKL01 = tk.Entry(frame1, width=13)
# eKL01.grid(row=4, column=1, padx=0, pady=5)

# lKL02 = tk.Label(master=frame1, text="02")
# lKL02.grid(row=5, column=0, padx=0, pady=5)
# lKL02.config(fg="black", font=("Arial", 11)) 
# eKL02 = tk.Entry(frame1, width=13)
# eKL02.grid(row=5, column=1, padx=0, pady=5)

# lKL03 = tk.Label(master=frame1, text="03")
# lKL03.grid(row=6, column=0, padx=0, pady=5)
# lKL03.config(fg="black", font=("Arial", 11)) 
# eKL03 = tk.Entry(frame1, width=13)
# eKL03.grid(row=6, column=1, padx=0, pady=5)

# lKL04 = tk.Label(master=frame1, text="04")
# lKL04.grid(row=7, column=0, padx=0, pady=5)
# lKL04.config(fg="black", font=("Arial", 11)) 
# eKL04 = tk.Entry(frame1, width=13)
# eKL04.grid(row=7, column=1, padx=0, pady=5)

# lKL05 = tk.Label(master=frame1, text="05")
# lKL05.grid(row=8, column=0, padx=0, pady=5)
# lKL05.config(fg="black", font=("Arial", 11)) 
# eKL05 = tk.Entry(frame1, width=13)
# eKL05.grid(row=8, column=1, padx=0, pady=5)

# lKL06 = tk.Label(master=frame1, text="06")
# lKL06.grid(row=9, column=0, padx=0, pady=5)
# lKL06.config(fg="black", font=("Arial", 11)) 
# eKL06 = tk.Entry(frame1, width=13)
# eKL06.grid(row=9, column=1, padx=0, pady=5)

# lKL07 = tk.Label(master=frame1, text="07")
# lKL07.grid(row=10, column=0, padx=0, pady=5)
# lKL07.config(fg="black", font=("Arial", 11)) 
# eKL07 = tk.Entry(frame1, width=13)
# eKL07.grid(row=10, column=1, padx=0, pady=5)

# lKL08 = tk.Label(master=frame1, text="08")
# lKL08.grid(row=11, column=0, padx=0, pady=5)
# lKL08.config(fg="black", font=("Arial", 11)) 
# eKL08 = tk.Entry(frame1, width=13)
# eKL08.grid(row=11, column=1, padx=0, pady=5)

# lKL09 = tk.Label(master=frame1, text="09")
# lKL09.grid(row=12, column=0, padx=0, pady=5)
# lKL09.config(fg="black", font=("Arial", 11)) 
# eKL09 = tk.Entry(frame1, width=13)
# eKL09.grid(row=12, column=1, padx=0, pady=5)

# lKL10 = tk.Label(master=frame1, text="10")
# lKL10.grid(row=13, column=0, padx=0, pady=5)
# lKL10.config(fg="black", font=("Arial", 11)) 
# eKL10 = tk.Entry(frame1, width=13)
# eKL10.grid(row=13, column=1, padx=0, pady=5)

# lKL11 = tk.Label(master=frame1, text="11")
# lKL11.grid(row=14, column=0, padx=0, pady=5)
# lKL11.config(fg="black", font=("Arial", 11)) 
# eKL11 = tk.Entry(frame1, width=13)
# eKL11.grid(row=14, column=1, padx=0, pady=5)

# lKL12= tk.Label(master=frame1, text="12")
# lKL12.grid(row=15, column=0, padx=0, pady=5)
# lKL12.config(fg="black", font=("Arial", 11)) 
# eKL12= tk.Entry(frame1, width=13)
# eKL12.grid(row=15, column=1, padx=0, pady=5)

# lKL13 = tk.Label(master=frame1, text="13")
# lKL13.grid(row=16, column=0, padx=0, pady=5)
# lKL13.config(fg="black", font=("Arial", 11)) 
# eKL13 = tk.Entry(frame1, width=13)
# eKL13.grid(row=16, column=1, padx=0, pady=5)

# lKL14 = tk.Label(master=frame1, text="14")
# lKL14.grid(row=17, column=0, padx=0, pady=5)
# lKL14.config(fg="black", font=("Arial", 11)) 
# eKL14 = tk.Entry(frame1, width=13)
# eKL14.grid(row=17, column=1, padx=0, pady=5)

# lKL15 = tk.Label(master=frame1, text="15")
# lKL15.grid(row=18, column=0, padx=0, pady=5)
# lKL15.config(fg="black", font=("Arial", 11)) 
# eKL15 = tk.Entry(frame1, width=13)
# eKL15.grid(row=18, column=1, padx=0, pady=5)

# lKL16 = tk.Label(master=frame1, text="16")
# lKL16.grid(row=19, column=0, padx=0, pady=5)
# lKL16.config(fg="black", font=("Arial", 11)) 
# eKL16 = tk.Entry(frame1, width=13)
# eKL16.grid(row=19, column=1, padx=0, pady=5)

# lKL17 = tk.Label(master=frame1, text="17")
# lKL17.grid(row=20, column=0, padx=0, pady=5)
# lKL17.config(fg="black", font=("Arial", 11)) 
# eKL17 = tk.Entry(frame1, width=13)
# eKL17.grid(row=20, column=1, padx=0, pady=5)

# lKL18 = tk.Label(master=frame1, text="18")
# lKL18.grid(row=21, column=0, padx=0, pady=5)
# lKL18.config(fg="black", font=("Arial", 11)) 
# eKL18 = tk.Entry(frame1, width=13)
# eKL18.grid(row=21, column=1, padx=0, pady=5)

# lKL19 = tk.Label(master=frame1, text="19")
# lKL19.grid(row=22, column=0, padx=0, pady=5)
# lKL19.config(fg="black", font=("Arial", 11)) 
# eKL19 = tk.Entry(frame1, width=13)
# eKL19.grid(row=22, column=1, padx=0, pady=5)

# lKL20 = tk.Label(master=frame1, text="20")
# lKL20.grid(row=23, column=0, padx=0, pady=5)
# lKL20.config(fg="black", font=("Arial", 11)) 
# eKL20 = tk.Entry(frame1, width=13)
# eKL20.grid(row=23, column=1, padx=0, pady=5)

# lKL21 = tk.Label(master=frame1, text="21")
# lKL21.grid(row=24, column=0, padx=0, pady=5)
# lKL21.config(fg="black", font=("Arial", 11)) 
# eKL21 = tk.Entry(frame1, width=13)
# eKL21.grid(row=24, column=1, padx=0, pady=5)

# lKL22 = tk.Label(master=frame1, text="22")
# lKL22.grid(row=25, column=0, padx=0, pady=5)
# lKL22.config(fg="black", font=("Arial", 11)) 
# eKL22 = tk.Entry(frame1, width=13)
# eKL22.grid(row=25, column=1, padx=0, pady=5)

# lKL23 = tk.Label(master=frame1, text="23")
# lKL23.grid(row=26, column=0, padx=0, pady=5)
# lKL23.config(fg="black", font=("Arial", 11)) 
# eKL23 = tk.Entry(frame1, width=13)
# eKL23.grid(row=26, column=1, padx=0, pady=5)


























root.mainloop()