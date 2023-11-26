from tkinter import *
import data
import re  
from tkinter import messagebox

def main():
    global usr_data,username
    username = data.read_username()
    usr_data = data.read_data(username)

    global root
    root = Toplevel()
    root.title("Register")
    root.geometry("300x600")

    changefont = ("Courier New", 15, "bold")
    judul = Label(root, text="Daftar", font=changefont)
    judul.place(x=100, y=10)

    global labelfr
    labelfr = LabelFrame(root, text="result", padx=20, pady=20)
    labelfr.place(x=60, y=380)

    nama = Label(root, text="Nama Lengkap")
    umur = Label(root, text="Umur")
    alamat = Label(root, text="Alamat")
    email = Label(root, text="Email")
    nohp = Label(root, text="Nomor Hp")

    global e1,e2,e3,e4,e5
    e1 = Entry(root, width=40)
    e2 = Entry(root)
    e3 = Entry(root, width=40)
    e4 = Entry(root, width=40)
    e5 = Entry(root, width=40)

    nama.place(x=20, y=50)
    umur.place(x=20, y=90)
    alamat.place(x=20, y=130)
    email.place(x=20, y=170)
    nohp.place(x=20, y=210)

    e1.place(x=20, y=70)
    e2.place(x=20, y=110)
    e3.place(x=20, y=150)
    e4.place(x=20, y=190)
    e5.place(x=20, y=230)

    global r
    r = StringVar()

    rb = Radiobutton(root, text="male", variable=r, value="male")
    rb.place(x=20, y=310)
    rb2 = Radiobutton(root, text="female", variable=r, value="female")
    rb2.place(x=80, y=310)

    btn = Button(root, text="submit", command=lambda:cetak())
    btn.place(x=100, y=350)

    root.mainloop()
    return

# menampung input
def cetak():
    class orang:
        def __init__(self, nama, umur, alamat, email, nohp, gender):
            self.nama = nama
            self.umur = umur
            self.alamat = alamat
            self.email = email
            self.nohp = nohp
            self.gender = gender

        def hasil(self):
            lbl = Label(
                labelfr,
                text="Nama Lengkap = "
                + self.nama
                + "\numur = "
                + self.umur
                + "\nalamat = "
                + self.alamat
                + "\nemail = "
                + self.email
                + "\nohp = "
                + self.nohp
                + "\ngender = "
                + self.gender,
                )
            lbl.grid()
            return

    umur_value = e2.get()
    nohp_value = e5.get()
    email_value = e4.get()

    # Validate Umur
    if not umur_value.isdigit():
        messagebox.showinfo("Error", "Umur harus berupa angka")
        return

    # Validate Nomor Hp
    if not re.match(r'^08[0-9]{9}$', nohp_value):
        messagebox.showinfo("Error", "Nomor Hp harus diawali 08 dan diikuti 9 angka")
        return

    # Validate Email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email_value):
        messagebox.showinfo("Error", "Email tidak valid")
        return

    ditampilkan = orang(e1.get(), umur_value, e3.get(), email_value, nohp_value, r.get())
    ditampilkan.hasil()
    save_data()
    return

def save_data():
    class dataz:
        def __init__(self,nama,umur,alamat,email_value,nohp_value,gender):
            self.nama = nama
            self.umur = umur
            self.alamat = alamat
            self.email_value = email_value
            self.nohp_value = nohp_value
            self.gender = gender
            
        def save(self):
            datadiri = [self.nama,self.umur,self.alamat,self.email_value,self.nohp_value,self.gender]
            listkey = ["nama","umur","alamat","email","no_hp","gender"]
            for key in range(len(listkey)):
                usr_data[0][listkey[key]] = datadiri[key]
            data.load_data(username,usr_data)
            return

    save = dataz(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), r.get())
    save.save()
    quit_messagebox()
    return

def quit_messagebox():
    yes = messagebox.showinfo("Succeed","Login Berhasil\nKembali Ke Halaman Utama")
    if yes:
        root.quit()
    return

def quits():
    root.withdraw()
    return
