from mmap import mmap
from tkinter import messagebox, ttk
from tkinter import *
import sqlite3
from Member.Member import Member

def showInfo():
    try:
        db = sqlite3.connect("MemberData.db")
        cr = db.cursor()
        cr.execute("select * from MemberInfo")
        data = cr.fetchall()
        tv.delete(*tv.get_children())
        for i in range(len(data)):
            tv.insert("", 'end', values=data[i])

    except Exception as e:
        messagebox.showerror("Message Error", f"something worng {str(e)}")
    finally:
        db.close()


def Ajouter():
    reponse = messagebox.askokcancel("Question", "Do you want to continue ?")
    if reponse == True:
        nomAdh = valuerNom.get()
        cotisationAdh = valeurCotisation.get()
        Member(nomAdh, cotisationAdh)
        showInfo()
    else:
        messagebox.showerror("Member added", "Member non added...")

def search():
    num = valeurCher.get()
    Member.search(num)


def delete():
    num = valeurSupp.get()
    Member.delete(num)

def modify():
    name = val_nom.get()
    contribution = val_cot.get()
    num = val_num.get()
    Member.modify(name,contribution,num)

def  showTrash():
    top = Toplevel()
    top.geometry("600x550")

    dataTrash = Member.showDeletMenber()
    # --------------- Treeview trash member
    treeVTrash = LabelFrame(top, borderwidth=0)
    treeVTrash.pack()

    titleTrash = Label(treeVTrash, text='List of Trash members'.title(), font=("Verdana", 16),
                      anchor=SW, fg="#f90")
    titleTrash.grid(row=0 , column=0,)

    area = ('Num', 'Name', 'Contribution')
    tableTrash = ttk.Treeview(treeVTrash, columns=area, show='headings')

    for i in range(len(area)):
        tableTrash.column(area[i], width=150,anchor='center')
        tableTrash.heading(area[i], text=area[i])

    tableTrash.grid(row=1 , column=0, columnspan=2)
    # fill in the member table delete
    tableTrash.delete(*tableTrash.get_children())
    for i in range(len(dataTrash)):
        tableTrash.insert("", 'end', values=dataTrash[i])

    # lable member Recover
    labelRec = Label(top, text="member number to Recover".title())
    labelRec.pack( padx=10, pady=10)

    # input  for number Recover
    valRec = StringVar()
    inputRec = Entry(top, textvariable=valRec, width=30)
    inputRec.pack(padx=10, pady=10)

    # button Recover member
    btnRec = Button(top, text="Recover",bg="#ffeaa7", fg="black",anchor=W, command=lambda : Member.recover(valRec.get()))
    btnRec.pack(padx=10, pady=10)



# ----------- GUI OF APP 
app = Tk()
app.title("membership management".upper())
app.iconbitmap("icon.ico")
app.geometry("900x600")

# ------------ frame 
fr1 = LabelFrame(app, text="add membership".title(),padx=10, pady=10)
fr1.grid(row=0, column=0, padx=10, pady=10)

# lable1
nomL = Label(fr1, text="Name :  ")
nomL.grid(row=0, column=0, padx=10, pady=10)
# input 1
valuerNom = StringVar()
nomAdh = Entry(fr1, textvariable=valuerNom, width=30)
nomAdh.grid(row=0, column=1, padx=10, pady=10)

# lable 2
cotisation = Label(fr1, text="Contribution : ")
cotisation.grid(row=1, column=0, padx=10, pady=10)
# input 2
valeurCotisation = StringVar()
CotisationAdh = Entry(fr1, textvariable=valeurCotisation, width=30)
CotisationAdh.grid(row=1, column=1, padx=10, pady=10)

# button ajouter Adherent
btn = Button(fr1, text="Add",bg="#ffeaa7", fg="black", command=Ajouter)
btn.grid(row=2, column=0, padx=10, pady=10)


# -------------- frame 2 
fr2 = LabelFrame(app, text="Delete Or Search")
fr2.grid(row=0, column=1, padx=10, pady=10)

# lable Adherent supprimer
labelS = Label(fr2, text="Membership number to delete".title())
labelS.grid(row=0, column=0, padx=10, pady=10)

# input  pour le numero supprimer
valeurSupp = StringVar()
inputS = Entry(fr2, textvariable=valeurSupp, width=30)
inputS.grid(row=0, column=1, padx=10, pady=10)

# button supprimer Adherent
btnS = Button(fr2, text="Delete",bg="#ffeaa7", fg="black",anchor=W, command=delete)
btnS.grid(row=1, column=0, padx=10, pady=10)


# lable Rechercher
label3 = Label(fr2, text="Membership number to search".title())
label3.grid(row=2, column=0, padx=10, pady=10)

# input  pour le numero Rechercher
valeurCher = StringVar()
input3 = Entry(fr2, textvariable=valeurCher, width=30)
input3.grid(row=2, column=1, padx=10, pady=10)

# button rechercher Adherent
btnR = Button(fr2, text="Search",bg="#ffeaa7", fg="black", command=search)
btnR.grid(row=3, column=0, padx=10, pady=10)


# ------------ frame 3

fr3 = LabelFrame(app, text="Modify Member")
fr3.grid(row=1, column=0, padx=10, pady=10)

# lable nom Modifier
nom_Mdf = Label(fr3, text="Name:  ")
nom_Mdf.grid(row=0, column=0, padx=10, pady=10)

# input nom Modifier
val_nom = StringVar()
Entry_nom_mdf = Entry(fr3, textvariable=val_nom, width=30)
Entry_nom_mdf.grid(row=0, column=1, padx=10, pady=10)

# lable cotisation Modifier
cotisation_mdf = Label(fr3, text="contribution ")
cotisation_mdf.grid(row=1, column=0, padx=10, pady=10)

# input cotisation Modifier
val_cot = StringVar()
Entry_cot_mdf = Entry(fr3, textvariable=val_cot, width=30)
Entry_cot_mdf.grid(row=1, column=1, padx=10, pady=10)

# lable  numero modfier
num_mdf = Label(fr3, text="Membership Number Edit")
num_mdf.grid(row=2, column=0, padx=10, pady=10)

# input  numero modifier
val_num = StringVar()
Entry_num_mdf = Entry(fr3, textvariable=val_num, width=30)
Entry_num_mdf.grid(row=2, column=1, padx=10, pady=10)

btn = Button(fr3, text="Modify",bg="#ffeaa7", fg="black", command=modify)
btn.grid(row=3, column=0, padx=10, pady=10)

# --------------- Treeview
treeV = LabelFrame(app, borderwidth=0)
treeV.grid(row=1 , column=1)

t = Label(treeV, text='List of members '.title(), font=("Verdana", 16),anchor=SW)
t.grid(row=0 , column=0,)

area = ('Num', 'Name', 'Contribution')

tv = ttk.Treeview(treeV, columns=area, show='headings')
for i in range(len(area)):
    tv.column(area[i], width=150,anchor='center')
    tv.heading(area[i], text=area[i])
tv.grid(row=1 , column=0, columnspan=2)
showInfo()
btn = Button(treeV, text="refresh Table",bg="#ffeaa7", fg="black",padx=10, pady=10, command=showInfo)
btn.grid(row=2, column=0, padx=10, pady=10)

# ------------ frame 4
fr4 = LabelFrame(app)
fr4.grid(row=2, column=0, padx=10, pady=10)

infobtn = "Show Member delete".title()
btn = Button(fr4, text=infobtn,bg="#ffeaa7", fg="black",padx=10, pady=10, command=showTrash)
btn.grid(row=0, column=0, padx=10, pady=10)

btn = Button(fr4, text="Exit",bg="#ffeaa7", fg="black",padx=10, pady=10, command=app.quit)
btn.grid(row=0, column=1, padx=10, pady=10)

app.mainloop()