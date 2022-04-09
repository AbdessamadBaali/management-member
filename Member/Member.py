import random
from tkinter import messagebox
import sqlite3

class Member:
    
    def __init__(self, name,contribution):
        self.__name = name
        self.__numero = random.randint(1, 999)
        self.__contribution = contribution
        
        try:
            db = sqlite3.connect("MemberData.db")
            cr = db.cursor()
            cr.execute("""create table if not exists MemberInfo
                    (num integer primary key autoincrement,
                    name varchar(25) not null,
                    contribution int not null);""")
            cr.execute(f"insert into MemberInfo(name,contribution) values('{self.__name}', {self.__contribution})")
            messagebox.showinfo("Member Added", "Member Added...")
            db.commit()

        except Exception as e:
            messagebox.showwarning("Member Added", f"Member non Added\n{str(e)}")
        
        finally:
            db.close()

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name

    def getcontribution(self):
        return self.__contribution

    def setcontribution(self, contribution):
        self.__contribution = contribution

    def getNumero(self):
        return self.__numero

    def setNumero(self, Numero):
        self.__numero = Numero

    def __str__(self):
        return f"{self.__numero};{self.__name};{self.__contribution} "


    @staticmethod
    def delete(num):
        
        try:
            db = sqlite3.connect("MemberData.db")
            cr = db.cursor()
            cr.execute(f"select * from MemberInfo where num = {num}")
            data = cr.fetchall()
            
            if len(data) > 0:
                reponse = messagebox.askokcancel("Delete Member", f"Do You Want To Delete This Member\n{data[0]}")
                
                if reponse == True:
                    cr.execute(f"delete from MemberInfo where num = {num}")
                    cr.execute(f"insert into membertrash values('{data[0][0]}','{data[0][1]}','{data[0][2]}' )")
                    db.commit()
                    messagebox.showinfo("Delete Member" , "Deleted with succussfully!")
                
                else:
                    messagebox.showinfo("Delete Member" , "Member Not Deleted")

            else :
                messagebox.showerror("Message Errore", "Member is not defined")

        except Exception as e:
            messagebox.showerror("Message Errore", f"Something wrong {str(e)}")
        
        finally:
            db.close()
        

    @staticmethod
    def search(num):
        
        try:
            db = sqlite3.connect("MemberData.db")
            cr = db.cursor()
            cr.execute(f"select * from MemberInfo where num = {num}")
            data = cr.fetchall()
            
            if len(data) > 0:
                messagebox.showinfo("Information Member" , data[0])
            
            else :
                messagebox.showerror("Message Errore", "Member is not defined")

        except Exception as e:
            messagebox.showerror("Message Errore", f"Something wrong {str(e)}")
        
        finally:
            db.close()

    @staticmethod
    def modify(name, contribution, num):
        
        try:
            db = sqlite3.connect("MemberData.db")
            cr = db.cursor()
            cr.execute("select * from MemberInfo")
            cr.execute(f"""update MemberInfo set name = '{name}', 
            contribution ='{contribution}' where num = {num}""")
            db.commit()
            messagebox.showinfo("Update Member", "Member Update with successfully!")
        
        except Exception as e:
            messagebox.showerror("Message Error", f"Something wrong {str(e)}")
        
        finally:
            db.close()

    @staticmethod
    def showDeletMenber():
        try:
            db = sqlite3.connect("MemberData.db")
            cr = db.cursor()
            cr.execute("""create table if not exists MemberTrash
                    (num integer,
                    name varchar(25) ,
                    contribution int );""")
            cr.execute("select * from membertrash")
            data = cr.fetchall()
        except Exception as e:
            messagebox.showerror("Message Error", f"Something wrong {str(e)}")
        
        finally:
            db.close()
        return data

    @staticmethod
    def recover(num):

        try:
            db = sqlite3.connect("MemberData.db")
            cr = db.cursor()
            cr.execute(f"select * from membertrash where num = {num}")
            data = cr.fetchall()
            
            if len(data) > 0:
                reponse = messagebox.askokcancel("Recover Member", f"Do You Want To Recover This Member\n{data[0]}")
                
                if reponse == True:
                    cr.execute(f"delete from membertrash where num = {num}")
                    cr.execute(f"insert into memberinfo values('{data[0][0]}','{data[0][1]}','{data[0][2]}' )")
                    db.commit()
                    messagebox.showinfo("Recover Member" , "Recover with succussfully!")
                
                else:
                    messagebox.showinfo("Recover Member" , "Member Not Recover")

            else :
                messagebox.showerror("Message Errore", "Member is not defined")

        except Exception as e:
            messagebox.showerror("Message Errore", f"Something wrong {str(e)}")
        
        finally:
            db.close()
