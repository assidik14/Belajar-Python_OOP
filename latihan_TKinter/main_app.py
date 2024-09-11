import tkinter

# Membuat object window
window = tkinter.Tk()

# Method object window
window.configure(bg="white")
window.geometry("300x300")
window.title("Latihan OOP")

# Membuat object frame
frame1 = tkinter.Frame(window, height=200, width=200)

# Membuat object label
label1 = tkinter.Label(frame1, text="Label 1")
label2 = tkinter.Label(window, text="Label 2")

# Membuat object tombol
tombol1 = tkinter.Button(frame1, text="Tombol 1")
tombol2 = tkinter.Button(window, text="Tombol 2")

# Menampilkan object
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()
frame1.pack()

# Methode loop, untuk menampilkan layar
window.mainloop()