from tkinter import *
import random
# Variable

base = 560
altura = 480

# Ventana principal

ventana_Principal = Tk()
ventana_Principal.title("Gráficas 2d")
ventana_Principal.resizable(False, False)
ventana_Principal.geometry("600x520")
ventana_Principal.config(bg="black")
c= Canvas(ventana_Principal, width=base, height=altura)
c.config(bg="white")
c.place(x=20,y=20)

"""frame_Salida = Frame(c)
frame_Salida.config(height=460,width=80, bg="dark turquoise")
frame_Salida.place(x=90, y=10)"""

carro1png = PhotoImage(file="./img/carro1.png")
carro2png = PhotoImage(file="./img/carro2.png")
carro1 = c.create_image(base/5-60,156,image=carro2png)
carro2 = c.create_image(base/5-60,330,image=carro1png)

texto_1 = c.create_text(base/5+30,76, anchor="center", text="S" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_2 = c.create_text(base/5+30,140, anchor="center", text="A" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_3 = c.create_text(base/5+30,214, anchor="center", text="L" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_4 = c.create_text(base/5+30,280, anchor="center", text="I" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_5 = c.create_text(base/5+30,344, anchor="center", text="D" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_6 = c.create_text(base/5+30,406, anchor="center", text="A" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")

carretera1 = c.create_rectangle(base/5+90,106,base-80,196)
holasalida = c.create_rectangle(base/5-10,46,base/5+70,436)
ventana_Principal.mainloop()