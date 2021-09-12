from tkinter import *

# Création d'un première fenètre
window = Tk()

# Personalisation de la fennètre
window.title("Mon app")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("zevent fond.ico")
window.config(background='#41B77F')

# afficher la fenettre
window.mainloop()