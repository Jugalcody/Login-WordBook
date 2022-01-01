import tkinter as tk
root=tk.Tk()

from tkinter import messagebox
name=tk.Label(text="user id : ")
name.place(relx=0.13,rely=0.4)

name_entry=tk.Entry()
name_entry.place(relx=0.18,rely=0.4)


pas=tk.Label(text="password : ")
pas.place(relx=0.12,rely=0.45)

pas_entry=tk.Entry()
pas_entry.place(relx=0.18,rely=0.45)
f=open("word.txt","a+")

import mysql.connector as mycon
my=mycon.connect(user="jugal",passwd="Jugal2002@" ,host="localhost")
cursor=my.cursor(buffered="True")
cursor.execute("create database if not exists logindb")
cursor.execute("use logindb")
cursor.execute("create table if not exists logindb ( sno varchar(100)primary key,name varchar(100)unique key,password varchar(100))")                                             
store={}                                           
cursor.execute("select * from logindb")
pp=cursor.fetchall()
jj=list(pp)
for i in jj:
      cc=list(i)
      store[cc[1]]=cc[2]
           
print(store)
def click():
       name=name_entry.get()
       pas=pas_entry.get()
       
       for i in range(len(store)):
                    if store[name]==pas:
                                 rr=messagebox.askquestion("user exist!!","Do you want to continue?")
                                 if rr=="yes":
                                             
                                            a=f"Welcome {name}"
                                            
                                            tk.Label(text=a,font="Bold").place(relx=0.1,rely=0.55)
                                            tk.Label(text="Word Notebook").place(relx=0.09,rely=0.65)
                                            tk.Label(text="Enter a word : ").place(relx=0.09,rely=0.75)
                                            c=tk.Entry()
                                            c.place(relx=0.3,rely=0.75)
                                            b=tk.Label(text="Meaning : ")
                                            b.place(relx=0.09,rely=0.8)
                                            t=tk.Entry()
                                            t.place(relx=0.26,rely=0.8)
                                            
                                            def submit():
                                                   
                                                    v=c.get()
                                                    oo=t.get()
                                                    
                                                    f.write(v+"      "+oo+"\n")
                                                        
                                            tk.Button(text="Submit",command=submit,bg="skyblue").place(relx=0.09,rely=0.85)
                                            
                                 break;           
                                              
                                            

                    else:
                                 h=tk.Label(text="Wrong password").place(relx=0.14,rely=0.34)
                                 

                             
name1=tk.Label(text="user id : ")
name1.place(relx=0.50,rely=0.40) 
name2_entry=tk.Entry()
name2_entry.place(relx=0.55,rely=0.40)
pas3=tk.Label(text="password : ")
pas3.place(relx=0.50,rely=0.45)
#cursor.execute("insert into logindb values(1,'jugal','#python#')")
pas4_entry=tk.Entry()
pas4_entry.place(relx=0.55,rely=0.45)
def ok():
    na=name2_entry.get();
    p=pas4_entry.get();
    cursor.execute("select * from logindb order by sno desc limit 1")
    
    h=cursor.fetchone()
    if h==None:
           b=1      
    else:
    
           n=list(h)
           b=int(n[0])+1
    c="insert into logindb values(%s,%s,%s)"
    o=str(b),str(na),str(p)
    cursor.execute(c,o)
    my.commit()
y=tk.Button(text="Create new account",command=ok)
y.place(relx=0.55,rely=0.50)
                                 
                  
                   
     
                                                                                        
       

button=tk.Button(text="login",command=click)
button.place(relx=0.15,rely=0.50)

root.mainloop()
f.close()
