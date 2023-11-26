# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:23:12 2023

@author: Arribaat
"""

import data as dt
import datetime as dm
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from PIL import Image, ImageTk

custom_font = ("Courier New", 15, "bold")

#main app window
def start():
    global username, usr_data
    username = dt.read_username()
    usr_data = dt.read_data(username)
    global main_window
    main_window = Toplevel()
    widths = 1240
    heights = 700

    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    print(screen_width,screen_height)

    global x,y
    x = (screen_width - widths) // 2
    y = (screen_height - heights) // 2
    print(x,y)

    main_window.geometry(f"{widths}x{heights}+{x}+{y}")

    # Generate Frame 
    frame_upper = Frame(main_window,height=140,width=1240-155,bg="#74B2D6")
    frame_upper.place(anchor=NW,x=155)

    frame_side = Frame(main_window,height=700,width=155,bg="#A4C8DD")
    frame_side.place(anchor=NW,y=140)

    frame_image = Frame(main_window, height=140, width=155, bg="#47A3E6")
    frame_image.place(anchor=NW)

    #<ERROR>
    # Load image
    #image_path = "Z:\\PPROKOM\\Proyek_Wallabi\\sc\\x_bear.jpg"
    #image = Image.open(image_path)
    #photo = ImagePhotoImage(image)

    #icon_image = Label(main_window, image=photo)
    #image = photo
    #icon_image.place(anchor=NW,x=5,y=5)
    #<ERROR>

    # Load buttons down
    laporan_harian = Button(main_window,text="Laporan Keuangan\nHarian",
                                            command=lambda:money_report(), 
                                            width=15,height=2)
    laporan_harian.place(anchor=NW,x=18,y=160)

    eval_keuangan = Button(main_window,text="Evaluasi \nKeuangan",
                                        command=lambda:money_eval(),
                                        width=15,height=2)
    eval_keuangan.place(anchor=NW,x=18,y=220)

    sara_pengeluaran = Button(main_window,text="Saran \nPengeluaran",
                                            command=lambda:money_adv(),
                                            width=15,height=2)
    sara_pengeluaran.place(anchor=NW,x=18,y=280)

    saran_pekerjaan = Button(main_window,text="Saran \nPekerjaan",
                                            command=lambda:job_adv(),
                                            width=15,height=2)
    saran_pekerjaan.place(anchor=NW,x=18,y=340)

    exit_app = Button(main_window,text="Exit",
                                    command=lambda:quit_messagebox(),
                                    width=15)
    exit_app.place(anchor=NW,x=18,y=660)

    global v
    app = main_window
    v = app.mainloop()
    return

# daily money report window
def money_report():
    def report_file_check():
        try:
            dt.read_report(username)
            file_exist = True
            return file_exist
        except FileNotFoundError:
            file_exist = False
            return file_exist

    global state
    state = report_file_check()
    if state:
        global report_arr
        report_arr = dt.read_report(username)
    else:
        dt.add_report(username)
        report_arr = dt.read_report(username)

    global money_report_window
    money_report_window = Toplevel()
    money_report_window.title("Laporan Keuangan Harian")
    widths = 1085
    heights = 530
    money_report_window.geometry(f"{widths}x{heights}+{x+155}+{y+170}")

    money_report_canvas_up = Frame(money_report_window,
                                                height=132,
                                                width=270,
                                                bg="#BEDDF5")
    money_report_canvas_up.place(anchor=NW)

    money_report_canvas_down = Frame(money_report_window,
                                                    height=398,
                                                    width=270,
                                                    bg="#C3F1F7")
    money_report_canvas_down.place(anchor=NW,
                                                y=132)

    money_report_title = Label(money_report_window,
                                            text="Laporan Keuangan\nHarian",
                                            font=custom_font,
                                            bg="#BFCCF5",
                                            fg="#A08C6E")
            
    money_report_title.place(anchor=NW,x=50,y=40)
            
    money_report_add = Button(money_report_window,
                                            text="Tambah \nLaporan",
                                            command=lambda:add_report(),
                                            width=30,height=2)
    money_report_add.place(anchor=NW,x=20,y=159)
            
    money_report_del = Button(money_report_window,
                                            text="Hapus \nLaporan",
                                            command=lambda:del_report(),
                                            width=30,height=2)
    money_report_del.place(anchor=NW,x=20,y=209)
            
    money_report_edit = Button(money_report_window,
                                            text="Cari \nLaporan",
                                            command=lambda:find_report_pass(),
                                            width=30,height=2)
    money_report_edit.place(anchor=NW,x=20,y=259)
            
    money_report_edit = Button(money_report_window,
                                            text="Exit",
                                            command=lambda:exit_all(),
                                            width=20,height=2)
    money_report_edit.place(anchor=NW,x=20,y=480)

    columns = ("Debit","Kredit","Keterangan")
    global display_reports
    display_reports = ttk.Treeview(money_report_window,columns=columns,height=25,show="tree headings")
    display_reports.place(anchor=NW,x=270)

    vsb = ttk.Scrollbar(money_report_window, orient="vertical", command=display_reports.yview)
    vsb.pack(side='right', fill='y')
    display_reports.configure(yscrollcommand=vsb.set)

    display_reports.heading("#0",text="Tanggal")

    for column in columns:
        display_reports.heading(column,text=column)

    display_reports.column("#0",width=135,anchor=W)

    for column in columns:
        display_reports.column(column, width=230,anchor=W)

    for index, line in enumerate(report_arr):
                display_reports.insert('', END, iid = index,
                text = line[0], values = line[1:])

    ttk_style = ttk.Style()
    ttk_style.theme_use('clam')
    ttk_style.configure('Treeview')
    return

def refresh_display():
     money_report_window.withdraw()
     money_report()
     return

def find_report_pass():
    try:
        add_report_window.withdraw()
    except:
        pass
    global tanggal_dicari
    tanggal_dicari = Toplevel()
    tanggal_dicari.geometry(f"250x135+{x+155*3}+{y+250}")
    tanggal_dicari.title("Search")

    def date_on_entry_click(event):
        if tanggal_dicari_input.get() == "DD-MM-YYYY":
                tanggal_dicari_input.delete(0,END)
                tanggal_dicari_input.configure(foreground="black")
                return

    def date_on_focus_out(event):
        if tanggal_dicari_input.get() == "":
                tanggal_dicari_input.insert(0, "DD-MM-YYYY")
                tanggal_dicari_input.configure(foreground="gray")
                return
        
    tanggal_dicari_label = Label(tanggal_dicari,text="Masukkan Tanggal",font=custom_font)
    tanggal_dicari_label.pack(side=TOP)
    tanggal_dicari_input = Entry(tanggal_dicari,width=13,textvariable=StringVar())
    tanggal_dicari_input.pack(side=TOP,pady=10)

    tanggal_dicari_input.insert(0, "DD-MM-YYYY")
    tanggal_dicari_input.configure(foreground="gray")

    tanggal_dicari.bind("<FocusIn>", date_on_entry_click)
    tanggal_dicari.bind("<FocusOut>", date_on_focus_out)

    tanggal_dicari_button = Button(tanggal_dicari,text='Confirm',width=20,command=lambda:ver_search())
    tanggal_dicari_button.pack(side=TOP)

    tanggal_dicari_button_reset = Button(tanggal_dicari,text="Refresh",width=20,command=lambda:reset_search())
    tanggal_dicari_button_reset.pack(side=TOP,pady=3)
    
    def reset_search():
        tanggal_dicari.withdraw()
        refresh_display()

    def ver_search():
        try:
            dm.datetime.strptime(tanggal_dicari_input.get(), "%d-%m-%Y")
            time_input_error = False
        except:
            time_input_error = True

        if time_input_error:
            messagebox.showerror("Error Input","Masukkan Tanggal Dengan Format\n(DD-MM-YYYY)")
            return
        else:
            searched_arr = []
            id_report = display_reports.get_children()
            for index in report_arr:
                if index[0] == tanggal_dicari_input.get():
                    searched_arr.append(index)

            for id in id_report:
                display_reports.delete(id)

            for index, line in enumerate(searched_arr):
                display_reports.insert('', END, iid = index,
                text = line[0], values = line[1:])
            tanggal_dicari.withdraw()
            return
            
def del_report():
    row_id = display_reports.focus()
    print(row_id)
    if row_id != "":
        confirmation = f"Apakah Anda Yakin Untuk Menghapus \nLaporan Tanggal {report_arr[int(row_id)][0]}?"
        confirm_state = messagebox.askyesno("Confirmation",confirmation)
        if confirm_state:
            display_reports.delete(row_id)
            del report_arr[int(row_id)]
            dt.load_report(username,report_arr)
            refresh_display()
            return
    else:
        messagebox.showerror("Error","Laporan Tidak Terpilih\nMohon Pilih Laporan Untuk Dihapus")
        return
            
def add_report():
    try:
        tanggal_dicari.withdraw()
    except:
        pass
    global add_report_window
    add_report_window = Toplevel()
    add_report_window.title("Add Report")
    add_report_window.geometry(f"260x400+{x+155*3}+{y+250}")

    add_report_canvas = Canvas(add_report_window,bg="#74B2D6",
                               width=265,height=75)
    add_report_canvas.place(anchor=NW,x=-2,y=-2)

    add_report_label = Label(add_report_window,text="Tambah\nLaporan",font=custom_font,bg="#74B2D6")
    add_report_label.place(anchor=NW,x=85,y=10)

    add_date_desc = Label(add_report_window,text="Tanggal",justify=LEFT)
    add_date_desc.place(anchor=NW,x=25,y=100)

    def date_on_entry_click(event):
        if add_date_input.get() == "DD-MM-YYYY":
                add_date_input.delete(0,END)
                add_date_input.configure(foreground="black")
                return

    def date_on_focus_out(event):
        if add_date_input.get() == "":
                add_date_input.insert(0, "DD-MM-YYYY")
                add_date_input.configure(foreground="gray")
                return

    add_date_input = Entry(add_report_window,width=21,textvariable=StringVar())
    add_date_input.insert(0, "DD-MM-YYYY")
    add_date_input.configure(foreground="gray")

    add_date_input.bind("<FocusIn>", date_on_entry_click)
    add_date_input.bind("<FocusOut>", date_on_focus_out)
    add_date_input.place(anchor=NW,x=100,y=100)

    #save date function()
    add_debt_desc = Label(add_report_window,text="Debit",justify=LEFT)
    add_debt_desc.place(anchor=NW,x=25,y=150)

    add_debt_input = Entry(add_report_window,width=21,textvariable=StringVar())
    add_debt_input.insert(0,"Rp.")
    add_debt_input.place(anchor=NW,x=100,y=150)

    #save data function without Rp. () for eval

    add_credit_desc = Label(add_report_window,text="Kredit",justify=LEFT)
    add_credit_desc.place(anchor=NW,x=25,y=200)

    add_credit_input = Entry(add_report_window,width=21,textvariable=StringVar())
    add_credit_input.insert(0,"Rp.")
    add_credit_input.place(anchor=NW,x=100,y=200)

    #save data function without Rp. () for eval

    add_desc_desc = Label(add_report_window,text="Keterangan",justify=LEFT)
    add_desc_desc.place(anchor=NW,x=25,y=250)

    global options
    options = ["Gaji","Investasi","Bonus","Refund","Laba","Hadiah","Tagihan","Cicilan",
               "Medis","Edukasi","Hiburan","Belanja","Travel","Other"]

    add_desc_option = ttk.Combobox(add_report_window, values = options,state='readonly',width=18)
    add_desc_option.set("Keterangan")
    add_desc_option.place(anchor=NW,x=100,y=250)

    def what_is(event):
        is_it_other = add_desc_option.get()
        if is_it_other == "Other":
                global add_desc_input
                add_desc_input = Entry(add_report_window,width=20,textvariable=StringVar,state=NORMAL)
                add_desc_input.place(anchor=NW,x=100,y=280)

                def desc_on_entry_click(event):
                    if add_desc_input.get() == "Keterangan":
                            add_desc_input.delete(0,END)
                            add_desc_input.configure(foreground="black")

                def desc_on_focus_out(event):
                    if add_desc_input.get() == "":
                            add_desc_input.insert(0, "Keterangan")
                            add_desc_input.configure(foreground="gray")

                add_desc_input.insert(0, "Keterangan")
                add_desc_input.configure(foreground="gray")

                add_desc_input.bind("<FocusIn>", desc_on_entry_click)
                add_desc_input.bind("<FocusOut>", desc_on_focus_out)
                return
        else:
                add_desc_input = Entry(add_report_window,width=20,textvariable=StringVar,state=DISABLED)
                add_desc_input.place(anchor=NW,x=100,y=280)
                return
    add_desc_option.bind('<<ComboboxSelected>>',what_is)

    def add_conf_conf():
        add_conf_conf = messagebox.askyesno("Confirm","Submit Laporan?")
        if add_conf_conf:
            ver_report()
        else:
            pass

    def ver_report():
        try:
            dm.datetime.strptime(add_date_input.get(), "%d-%m-%Y")
            time_input_error = False
        except:
            time_input_error = True

        if time_input_error:
            messagebox.showerror("Error Input","Masukkan Tanggal Dengan Format\n(DD-MM-YYYY)")
            return
        else:
            int_input_debt = str(add_debt_input.get()[3:])
            int_input_credit = str(add_credit_input.get()[3:])
            input_debt = add_debt_input.get()
            input_credit = add_credit_input.get()
            base_nominal_input_state = "Rp." 
            if input_debt == base_nominal_input_state and input_credit == base_nominal_input_state:
                messagebox.showerror("Error Input","Masukkan Nilai Pada Kolom\nDebit atau Kredit")
                return
            elif input_debt[:3] != "Rp." or input_credit[:3] != "Rp.":
                messagebox.showerror("Error Input","Masukkan Nilai Pada Kolom\nDebit atau Kredit Dengan Mata Uang Rupiah")
                return
            elif int_input_credit.isalpha and int_input_debt.isalpha():
                print(int_input_credit,int_input_debt)
                messagebox.showerror("Error Input","Tidak Menerima Input\nBerupa Huruf Alfabet")
            else:
                global input_desc,input_desc_other
                try:
                    input_desc_other = add_desc_input.get()
                except:
                    pass
                input_desc = add_desc_option.get()
                if input_desc == "Keterangan":
                    messagebox.showerror("Error Input","Pilih Keterangan Untuk\Laporan Ini")
                    return
                else:
                    if input_desc_other == "Keterangan" and "":
                        messagebox.showerror("Error Input","Tulis Keterangan Anda")
                        return
                    else:
                        save_report()
                        return

    def save_report():
            if input_desc == "Other":
                 description = input_desc_other
            else:
                 description = input_desc

            report_list = [add_date_input.get(),add_debt_input.get(),add_credit_input.get(),
                        description]
            report_arr.append(report_list)
            print(report_list)
            dt.load_report(username,report_arr)
            add_report_window.withdraw()
            refresh_display()
            return

    add_confirm_button = Button(add_report_window,text="Confirm",command=lambda:add_conf_conf())
    add_confirm_button.place(anchor=NW,x=25,y=350)

    def exit_add_report_window():
        add_conf_exit = messagebox.askyesno("Exit","Apakah anda yakin ingin kembali?")
        if add_conf_exit:
            add_report_window.withdraw()
            return
        else:
            pass
        return
    
    add_exit_button = Button(add_report_window,text="Back",command=lambda:exit_add_report_window())
    add_exit_button.place(anchor=NW,x=90,y=350)
    return

def exit_all():
        try:
            add_report_window.withdraw()
            money_report_window.withdraw()
            return
        except:
            try:
                tanggal_dicari.withdraw()
                money_report_window()
                return
            except:
                try:
                    money_report_window.withdraw()
                    return
                except:
                     return
            
#money evaluation window 
def money_eval():
    money_eval_window = Toplevel()
    money_eval_window.title("Evaluasi Keuangan")
    widths = 1085
    heights = 530
    money_eval_window.geometry(f"{widths}x{heights}+{x+155}+{y+170}")
    return

#money advice window 
def money_adv():
    money_adv_window = Toplevel()
    money_adv_window.title("Saran Pengeluaran")
    widths = 1085
    heights = 530
    money_adv_window.geometry(f"{widths}x{heights}+{x+155}+{y+170}")
    return

#job advice window
def job_adv():
    job_adv_window = Toplevel()
    job_adv_window.title("Saran Pekerjaan")
    widths = 1085
    heights = 530
    job_adv_window.geometry(f"{widths}x{heights}+{x+155}+{y+170}")

    text = Label(job_adv_window,text="hello",font=("Courier New",10,"bold"))
    text.pack(side=TOP)
    text2 = Label(job_adv_window,text="hello",font=("Courier New",10,"bold"))
    text2.pack(side=TOP)
    return

#quit app func
def quit_messagebox():
    yes = messagebox.askyesno("Quit","Keluar?")
    if yes:
        main_window.quit()
        return
    return

def exitapp():
    main_window.withdraw()
    return

#harus ada cache file
#!cache file = error
if __name__ == "__main__":
    start()