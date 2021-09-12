from tkinter import *
import webbrowser

def open_over44_channel():
    webbrowser.open_new("https://www.youtube.com/channel/UCfA_pq-YZo8yWDAm6MrkzqQ")


# Création d'un première fenètre
window = Tk()

# Personalisation de la fennètre
window.title("Mon app")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("zevent fond.ico")
window.config(background='#41B77F')

# Création d'un boite
frame = Frame(window, bg='#41B77F')

# Ajout d'un texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Dimbo", 40), bg='#41B77F', fg='white')
label_title.pack()

# Ajout d'un second texte
label_subtitle = Label(frame, text="Hey salut à toi !", font=("Dimbo", 25), bg='#41B77F', fg='white')
label_subtitle.pack()

# Ajout d'un boutton
yt_button = Button(frame, text="Ouvrir Youtube", font=("Dimbo", 25), bg='white', fg='#41B77F', command=open_over44_channel)
yt_button.pack(pady=25, fill=X)

# Pack la frame
frame.pack(expand=True)

# afficher la fenettre
window.mainloop()