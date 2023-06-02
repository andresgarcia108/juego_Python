from tkinter import *
from tkinter import messagebox
import random
# Variable

base = 1000
altura = 480

# Ventana principal

ventana_Principal = Tk()
ventana_Principal.title("Gráficas 2d")
ventana_Principal.resizable(False, False)
ventana_Principal.geometry("1040x520")
ventana_Principal.config(bg="black")
c= Canvas(ventana_Principal, width=base, height=altura)
c.config(bg="green")
c.place(x=20,y=20)

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

carretera1 = c.create_rectangle(base/5+90,96,base-80,205, fill="black")
carretera2 = c.create_rectangle(base/5+90,275,base-80,384, fill="black")
linea1 = c.create_line(base/5+90,150.5,base-80,150.5,width=5,fill="yellow")
linea2 = c.create_line(base/5+90,329.5,base-80,329.5,width=5,fill="yellow")
#holasalida = c.create_rectangle(base/5-10,46,base/5+70,436)




texto_7 = c.create_text(base-50,106, anchor="center", text="M" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_8 = c.create_text(base-50,374-187, anchor="center", text="E" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_9 = c.create_text(base-50,374-93.5, anchor="center", text="T" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")
texto_10 = c.create_text(base-50,altura-106, anchor="center", text="A" , font=("Arial" , 25 ,"bold"), fill="cyan2",
activefill="blue2")


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

carretera1 = c.create_rectangle(base/5+90,96,base-80,205, fill="black")
carretera2 = c.create_rectangle(base/5+90,275,base-80,384, fill="black")
linea1 = c.create_line(base/5+90,150.5,base-80,150.5,width=5,fill="yellow")
linea2 = c.create_line(base/5+90,329.5,base-80,329.5,width=5,fill="yellow")
holasalida = c.create_rectangle(base/5-10,46,base/5+70,436)
carro1png = PhotoImage(file="./img/carro1.png")
carro2png = PhotoImage(file="./img/carro2.png")
carro1 = c.create_image(base/5-60,156,image=carro2png)
carro2 = c.create_image(base/5-60,330,image=carro1png)



"""def mover_carro():
    global velocidad_x1, velocidad_x2

    x_actual, y = c.coords(carro1)
    x_actual2, y2 = c.coords(carro2) 
    velocidad_x1 = random.randint(4, 12)
    velocidad_x2 = random.randint(4, 12)
    if x_actual >= 900 or x_actual2 >= 900:
        velocidad_x1 = 0
        velocidad_x2 = 0
        messagebox.showinfo("Resultado", "Ganó el carro 1")
    elif x_actual2 >= 940:
        messagebox.showinfo("Resultado", "Ganó el carro 2")

    else:
        c.move(carro1, velocidad_x1, 0)
        c.move(carro2, velocidad_x2, 0)


    ventana_Principal.after(60, mover_carro)"""
def mover_carros():
    global velocidad_x1, velocidad_x2

    x_actual, y = c.coords(carro1)
    x_actual2, y2 = c.coords(carro2) 
    velocidad_x1 = random.randint(3, 8)
    velocidad_x2 = random.randint(3, 8)
    if x_actual >= 940:
        velocidad_x1 = 0
        velocidad_x2 = 0
        messagebox.showinfo("Resultado", "El carro 1 ganó")
    elif x_actual2 >= 940:
        messagebox.showinfo("Resultado", "El carro 2 ganó")
        velocidad_x1 = 0
        velocidad_x2 = 0
    else:
        c.move(carro1, velocidad_x1, 0)
        c.move(carro2, velocidad_x2, 0)
        ventana_Principal.after(60, mover_carros)



bt_jugar = Button(ventana_Principal,text="JUGAR",command=mover_carros)
bt_jugar.place(x=460, y=altura-40, width=150, height=40)
ventana_Principal.mainloop()