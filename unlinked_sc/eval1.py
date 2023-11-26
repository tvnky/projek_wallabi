import tkinter as tk 
from tkinter import ttk

#window
window = tk.Tk()
window.configure(bg="white")
window.geometry("500x600")
window.title("WALLABI : KONSULTAN KEUANGAN DIGITAL")

#frame
input_frame = ttk.Frame(window)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

#label dan entry
tabungan_label = ttk.Label(input_frame,text="TABUNGAN")
tabungan_label.pack(padx=10,fill="x",expand=True)
TABUNGAN = tk.StringVar()
tabungan_entry = tk.Entry(input_frame,textvariable=TABUNGAN)
tabungan_entry.pack(padx=10,fill="x",expand=True)

penghasilan_label = ttk.Label(input_frame,text="Penghasilan saat ini : Rp.")
penghasilan_label.pack(padx=10,fill="x",expand=True)
PENGHASILAN = tk.StringVar()
penghasilan_entry = tk.Entry(input_frame,textvariable=PENGHASILAN)
penghasilan_entry.pack(padx=10,fill="x",expand=True)

pengeluaran_label = ttk.Label(input_frame,text="Pengeluaran saat ini : Rp.")
pengeluaran_label.pack(padx=10,fill="x",expand=True)
PENGELUARAN = tk.StringVar()
pengeluaran_entry = tk.Entry(input_frame,textvariable=PENGELUARAN)
pengeluaran_entry.pack(padx=10,fill="x",expand=True)

#tombol
def evaluasi_keuangan():
    tabungan = int(tabungan_entry.get())
    penghasilan = int(penghasilan_entry.get())
    pengeluaran = int(pengeluaran_entry.get())
    saldo = penghasilan - pengeluaran

    if pengeluaran > penghasilan:
        hasil_label.config(text="MULAI SEKARANG, ANDA HARUS LEBIH HEMAT!!\nANDA SEDANG MENGALAMI DEFISIT KEUANGAN SEBESAR " + str(abs(saldo)) )
        tabungan -= pengeluaran - penghasilan
        # REKOMENDASI_PEKERJAAN()

    elif pengeluaran < penghasilan:
        hasil_label.config(text="WAH!!! HEBATTT!! ANDA KEREN SEKALI!")
        tabungan += penghasilan - pengeluaran
        # PENYALURAN_DANA()

    tabungan_entry.delete(0, tk.END)
    penghasilan_entry.delete(0, tk.END)
    pengeluaran_entry.delete(0, tk.END)

tombol_eval = ttk.Button(input_frame,text="EVALUASI",command=evaluasi_keuangan)
tombol_eval.pack(padx=10,pady=10,fill="x",expand=True)

hasil_label = tk.Label(input_frame,text="")
hasil_label.pack(padx=10,pady=10,fill="x",expand=True)


#loop
window.mainloop()

