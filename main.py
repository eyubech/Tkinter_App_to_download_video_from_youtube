import tkinter as tk
import pytube
from tkinter import messagebox
root = tk.Tk()
root.title('Youtube downloader')
root.geometry('500x150')

lien_var = tk.StringVar()
def url():
    lien = lien_var.get()
    youtube = pytube.YouTube(lien)
    video = youtube.streams.first()
    #video loaction
    video.download('/home/ayoub/')
    lien_var.set("")
    tk.messagebox.showinfo(title='Download', message='Done', )


title = tk.Label(root, text='youtube downloader',font=('Helvatical bold',30,'bold')).pack()
ent = tk.Entry(root, width="50", textvariable = lien_var).pack()
down = tk.Button(root, text='Download',command=url).pack()
l = tk.Label(root, text='By ayoub ech-chetyouy').pack()






root.mainloop()
