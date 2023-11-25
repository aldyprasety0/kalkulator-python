# Project akhir semester Wayan Aldy 10.6
import tkinter as tk

def tambah_angka():
    angka = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, angka + "+")

def kurang_angka():
    angka = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, angka + "-")

def kali_angka():
    angka = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, angka + "*")

def bagi_angka():
    angka = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, angka + "/")

def hitung():
    ekspresi = entry.get()
    try:
        hasil = eval(ekspresi)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(hasil))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def tambahkan_angka(angka):
    entry.insert(tk.END, angka)

def hapus():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Kalkulator Project Akhir Semester")
root.configure(bg='#333333') # Ngubah warna
root.resizable(False, False)

entry = tk.Entry(root, width=20, font=('Arial', 18), bg='#555555', fg='white', bd=0, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_list = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in button_list:
    if text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, bg='#FF6347', fg='white', font=('Arial', 12),
                           command=hapus)
    elif text == '=':
        button = tk.Button(root, text=text, width=5, height=2, bg='#2E8B57', fg='white', font=('Arial', 12),
                           command=hitung)
    else:
        button = tk.Button(root, text=text, width=5, height=2, bg='#666666', fg='white', font=('Arial', 12),
                           command=lambda t=text: tambahkan_angka(t))
    button.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()