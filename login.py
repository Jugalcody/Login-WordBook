import tkinter as tk
root=tk.Tk()
from PIL import Image,ImageTk
from tkinter import messagebox
name=tk.Label(text="user id : ")
name.place(relx=0.13,rely=0.4)

name_entry=tk.Entry()
name_entry.place(relx=0.36,rely=0.4)


pas=tk.Label(text="password : ")
pas.place(relx=0.12,rely=0.45)

pas_entry=tk.Entry()
pas_entry.place(relx=0.36,rely=0.45)

f=open("word.txt","a+")
image=Image.open("12.jpg")
image.resize((100,100), Image.ANTIALIAS)
image.thumbnail((1500,700),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.place(relx=0.22,rely=0.16)
                                              
                                            

#store={"jugal":"#python#"}
def click():
       name=name_entry.get()
       pas=pas_entry.get()
    
       if name=="jugal" :
                   if pas=="#python#":
                                 rr=messagebox.askquestion("user exist!!","Do you want to continue?")
                                 if rr=="yes":
                                             
                                            a=f"Welcome {name}"
                                            
                                            tk.Label(text=a,font="Bold").place(relx=0.1,rely=0.45)
                                            tk.Label(text="Word Notebook").place(relx=0.09,rely=0.55)
                                            tk.Label(text="Enter a word : ").place(relx=0.09,rely=0.65)
                                            c=tk.Entry()
                                            c.place(relx=0.4,rely=0.65)
                                            b=tk.Label(text="Meaning : ")
                                            b.place(relx=0.09,rely=0.7)
                                            t=tk.Entry()
                                            t.place(relx=0.40,rely=0.7)
                                            
                                            def submit():
                                                   
                                                    v=c.get()
                                                    oo=t.get()
                                                    
                                            
                                            
                                            
                                            
                                                    f.write(v+"      "+oo+"\n")
                                                        
                                            tk.Button(text="Submit",command=submit,bg="skyblue").place(relx=0.09,rely=0.75)
                                            
                                            
                                              
                                            

                   else:
                                 h=tk.Label(text="Wrong password").place(relx=0.14,rely=0.34)
                  
                   
     
                                                                                        
       

button=tk.Button(text="login",command=click)
button.place(relx=0.15,rely=0.5)

root.mainloop()
f.close()
