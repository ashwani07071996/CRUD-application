from tkinter import*
from tkinter import messagebox


import mysql.connector as mysql

root=Tk()
root.title("CRUD check")
root.geometry("600x400")

root.config(bg="#fb44fb")

#--------------------------------------

my_label=Label(root,text="ID ",bg="#fb44fb",font="Arial,15,bold")
my_label.place(x=20,y=50)

my_label2=Label(root,text="Name ",font="Arial,15,bold",bg="#fb44fb")
my_label2.place(x=20,y=100)

my_label3=Label(root,text="Phone",bg="#fb44fb",font="Arial,15,bold")
my_label3.place(x=20,y=150)

my_entry=Entry(root)
my_entry.place(x=70,y=50)

my_entry2=Entry(root)
my_entry2.place(x=70,y=100)

my_entry3=Entry(root)
my_entry3.place(x=75,y=150)

#========function============================
def insert_fun():
    id=my_entry.get()
    name=my_entry2.get()
    phone=my_entry3.get()
    
    if id=="" or name=="" or phone=="":
        messagebox.showwarning("insertError","please fill all the data")
    else:
        con=mysql.connect(host="localhost",user="root",password="root",database="Ashwani_db")
        
        cursor=con.cursor()
        cursor.execute("insert into student values(%s,%s,%s)",(id,name,phone))
        
        cursor.execute("commit")
        
        my_entry.delete(0,"end")
        my_entry2.delete(0,"end")

        my_entry3.delete(0,"end")
        messagebox.showinfo("message","weldone ! ur data inserted")
        cursor.close()
        
def get_fun():
    id=my_entry.get()
    if id=="":
        messagebox.showwarning("GetdataError","please enter Id")
    else:
        con=mysql.connect(host="localhost",user="root",password="root",database="Ashwani_db")
        cursor=con.cursor()
        cursor.execute("select * from student where id=(%s)",(id,))
        result=cursor.fetchall()
        print(result)
        
        my_entry2.insert(0,result[0][1])
        my_entry3.insert(0,result[0][2])
        
        con.close()
        
    
def update_fun():
    id=my_entry.get()
    name=my_entry2.get()
    phone=my_entry3.get()
    if id=="" or name=="" or phone=="":
     messagebox.showwarning("update data","please enter data")
    

    else:
        con=mysql.connect(host="localhost",user="root",password="root",database="Ashwani_db")
        
        cursor=con.cursor()
        cursor.execute("update student set name=(%s),phone=(%s) where id=(%s)" ,(name,phone,id))
        
        cursor.execute("commit")
        my_entry.delete(0,"end")
        my_entry2.delete(0,"end")

        my_entry3.delete(0,"end")
        messagebox.showinfo("message","Update successful")
        con.close()







def delete_fun():
    id=my_entry.get()
   
    if id=="":
     messagebox.showwarning("delete data error","please enter ID")
    

    else:
        con=mysql.connect(host="localhost",user="root",password="root",database="Ashwani_db")
        
        cursor=con.cursor()
       # cursor.execute("delete from  student  where id=(%s)" ,(id))
        cursor.execute("delete from student where id=(%s)", (id,))

        
        cursor.execute("commit")

        my_entry.delete(0,"end")
        my_entry2.delete(0,"end")

        my_entry3.delete(0,"end")
        messagebox.showinfo("message","Delete successful ")
        con.close()

#=======================================================
        
def clear_fun():
    
        my_entry.delete(0,"end")
        my_entry2.delete(0,"end")

        my_entry3.delete(0,"end")
        

#============buttuns============================

btn=Button(root,text="insert",font="Arial,15,bold",borderwidth=5,
           relief="raised",padx=5,pady=5,bg="blue",command=insert_fun)
btn.place(x=100,y=200)

btn2=Button(root,text="update",font="Arial,15,bold",borderwidth=5,
           relief="raised",padx=5,pady=5,bg="blue",command=update_fun)
btn2.place(x=180,y=200)

btn3=Button(root,text="view",font="Arial,15,bold",borderwidth=5,
           relief="raised",padx=5,pady=5,bg="blue",command=get_fun)
btn3.place(x=280,y=200)

btn4=Button(root,text="delete",font="Arial,15,bold",borderwidth=5,
           relief="raised",padx=5,pady=5,bg="blue",command=delete_fun)
btn4.place(x=360,y=200)


btn5=Button(root,text="clear",font="Arial,15,bold",borderwidth=5,
           relief="raised",padx=5,pady=5,bg="red",command=clear_fun)
btn5.place(x=280,y=250)


#==============================================


#============================

root.mainloop()