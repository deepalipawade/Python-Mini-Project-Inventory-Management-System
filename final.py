from tkinter import  *
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
from tkinter import messagebox
def Insert_Vendor():
    #t=Toplevel()
    global vid,vname,vadd,vcon
    vid=e1.get()
    vname=e2.get() 
    vadd=e3.get()
    vcon=e4.get()
    if(len(vcon)!=10):
        messagebox.showinfo("Invalid Contact", "Enter Apprpriate contact no , It should be of length 10.")
        closeT()
        top1()
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    c.execute('''create table IF NOT EXISTS vendor_info(vid int primary key,vname string,vadd string,vcon string)''')
    try:
        c.execute('''insert into vendor_info(vid,vname,vadd,vcon) VALUES (?,?,?,?)''',(vid,vname,vadd,vcon))
    except sqlite3.IntegrityError:
        messagebox.showinfo("Duplication Error", "Enter Apprpriate id , Vendor with this id already Exists")
        closeT()
        top1()

    c.execute('''select * from vendor_INFO''')
    conn.commit() 						# if not written rollback till last commit and table will be empty
    messagebox.showinfo("Successfully Added", "Vendor Information added")

    
def top1():
    global t   
    t=Toplevel()
    t.title("VENDOR INFORMATION")
    t.configure(background='LIGHTGOLDENROD')
    l1=Label(t,text="Enter Vendor Details",bg='LIGHTGOLDENROD',fg="black",font=("Arial Bold", 12)).place(relx=0.35, rely=0.05, anchor=CENTER)
    t.geometry("400x400")
    MyInfo()

def MyInfo():
    global e1,e2,e3,e4,e5,e6
    Label(t, text="ID",bg='LIGHTGOLDENROD',fg="black").place(relx=0.15, rely=0.1)
    Label(t, text="NAME",bg='LIGHTGOLDENROD',fg="black").place(relx=0.15, rely=0.2)
    Label(t, text="ADDRESS",bg='LIGHTGOLDENROD',fg="black").place(relx=0.15, rely=0.3)
    Label(t, text="CONTACT NO",bg='LIGHTGOLDENROD',fg="black").place(relx=0.15, rely=0.4)

    e1 = Entry(t)
    e2 = Entry(t)
    e3 = Entry(t)
    e4 = Entry(t)
    

    e1.place(relx=0.45, rely=0.1)
    e2.place(relx=0.45, rely=0.2)
    e3.place(relx=0.45, rely=0.3)
    e4.place(relx=0.45, rely=0.4)
    
    b1=Button(t,text="INSERT",bg="ORANGE",fg="black",height=1,width=15,command=Insert_Vendor).place(relx=0.35, rely=0.6)
    b2=Button(t,text="ADD PRODUCTS",bg="ORANGE",fg="black",height=1,width=15,command=add_product).place(relx=0.35, rely=0.7)
    b3=Button(t,text="Back",bg="TOMATO",fg="black",height=1,width=15,command=closeT).place(relx=0.35, rely=0.85)

def add_product():
    global e1,e2,e3,e4,e5,e6,t1
    t1=Toplevel()
    t1.geometry("400x400")
    t1.title("PRODUCT DETAILS")
    t1.configure(background='LIGHTGOLDENROD')
    s=vname+" :- Product Details"
    t1.title(s)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=0)
    l1=Label(t1,text=s,bg='LIGHTGOLDENROD')
    l1.place(relx=0.25, rely=0.03, anchor=CENTER)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=1)
    t.geometry("400x400")
    Label(t1, text="ID",bg='LIGHTGOLDENROD',fg="black").grid(row=2)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=3)
    Label(t1, text="NAME",bg='LIGHTGOLDENROD',fg="black").grid(row=4)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=5)
    Label(t1, text="PURCHASE PRICE",bg='LIGHTGOLDENROD',fg="black").grid(row=6)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=7)
    Label(t1, text="QUANTITY",bg='LIGHTGOLDENROD',fg="black").grid(row=8)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=9)
    Label(t1, text="SELLING PRICE",bg='LIGHTGOLDENROD',fg="black").grid(row=10)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=11)

    e1 = Entry(t1)
    e2 = Entry(t1)
    e3 = Entry(t1)
    e4 = Entry(t1)
    e5 = Entry(t1)

    e1.grid(row=2, column=1)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=3)
    e2.grid(row=4, column=1)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=5)
    e3.grid(row=6, column=1)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=7)
    e4.grid(row=8, column=1)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=9)
    e5.grid(row=10, column=1)
    Label(t1,bg='LIGHTGOLDENROD').grid(row=11)

    b2=Button(t1,text="DONE",bg="TOMATO",fg="black",height=2,width=15,command=Insert_pro).grid(row=14,column=1)
    b3=Button(t1,text="Back",bg="TOMATO",fg="black",height=2,width=15,command=closeT1).grid(row=14,column=2)

def Insert_pro():
    global pid,pname,pcp,psp,pq
    pid=e1.get()
    pname=e2.get() 
    pcp=e3.get()
    pq=e4.get()
    psp=e5.get()
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    c.execute('''create table IF NOT EXISTS product_info(pid int primary key,vid int references vendor_info(vid),pname string,pcp real,pq int,psp real)''') 
    print(vid)
    c.execute('''insert into product_info(pid,vid,pname,pcp,pq,psp) VALUES (?,?,?,?,?,?)''',(pid,vid,pname,pcp,pq,psp))
    c.execute('''select * from product_info''')
    conn.commit() 						# if not written rollback till last commit and table will be empty
    conn.close()

def closeT1():
    t1.destroy()

def top2():
    global t
    t=Toplevel()
    t.geometry("550x400")
    t.configure(background='Rosybrown1')
    t.title("PRODUCT DETAILS") 
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    #c.execute('''alter table vendor_info drop vadd''')
    #c.execute('''delete from product_info''')
    #c.execute('''delete from vendor_info''')
    c.execute('''SELECT P.PID,V.VNAME,P.PNAME,P.PCP,P.PQ,P.PSP FROM PRODUCT_INFO P INNER JOIN vendor_info V ON P.VID=V.VID ''') 
    data=c.fetchall() 
    #print(data)
    r=1
    c=0 
    Label(t, text="ID",bg="Rosybrown3",fg="black",width=5,font=("Arial Bold", 10)).grid(row=0, column=0)
    Label(t, text="VENDOR NAME",bg="Rosybrown3",fg="black",font=("Arial Bold", 10)).grid(row=0, column=1)
    Label(t, text="PRODUCT NAME",bg="Rosybrown3",fg="black",font=("Arial Bold", 10)).grid(row=0, column=2)
    Label(t, text="PURCHASE PRICE",bg="Rosybrown3",fg="black",font=("Arial Bold", 10)).grid(row=0, column=3)
    Label(t, text="QUANTITY",bg="Rosybrown3",fg="black",font=("Arial Bold", 10)).grid(row=0, column=4)
    Label(t, text="SELLING PRICE",bg="Rosybrown3",fg="black",font=("Arial Bold", 10)).grid(row=0, column=5)
  
    for index in data:
        c=0
        for i in index:
            Label(t, text=i,bg='Rosybrown1',fg="black").grid(row=r, column=c)
            c=c+1
        r=r+1
    if(r<=10):
        r=(r/10)
        r=r-0.3
    else:
        r=0.9   
    z=Button(t,text="back",bg="Rosybrown3",fg="black",width=5,font=("Arial Bold", 10),command=closeT).place(relx=0.45,rely=r)
    conn.commit()
    conn.close()

def top3():
    global e1,e2,t,value
    display=["VENDOR NAMES"]
    global variable,t
    t=Toplevel()
    t.title('SELL PRODUCT')
    t.configure(background='LIGHTGOLDENROD')
    t.geometry("500x500")
    l=['laptop','charger','keyboard','camera']
    Label(t, text="Sell Products to Customers",bg='LIGHTGOLDENROD',font=("Arial Bold", 15)).place(relx=0.2,rely=0.01)
    Label(t,text="Select Product Name",bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.2,rely=0.1)    
    variable = StringVar(t)
    variable.set("Product Name")
    w = OptionMenu(t,variable,*l,command=okay).place(relx=0.5,rely=0.1)
    
def okay(value):
    global c,conn,p,d,l
    p=value
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    c.execute('''select vid from product_info where pname=?''',(p,))
    vid=c.fetchall()
    l=[]
    idList=[]
    for i in vid:
        i=i[0]
        c.execute('''select vname from vendor_info where vid=?''',(i,))
        data=c.fetchall()
        data=data[0]
        data=data[0]
        l.append(data)
    Label(t, text="Select Vendor Name",bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.2,rely=0.2)    
    variable = StringVar(t)
    variable.set("VENDOR NAME")
    value=" "
    w = OptionMenu(t,variable,*l,command=vn).place(relx=0.5,rely=0.2)
   
    
def vn(value):
    flag=0
    c.execute('''select vname from vendor_info  where vid IN(select vid from product_info where pname=?)''',(p,))
    exists=c.fetchall()
    for i in exists:
            if(i[0]==value):
                print('value',value)
                flag=1
    if(flag==0):
         print(error)
         messagebox.showerror('Missing','Vendor Names Not Selected')
         okay(p)                
    global m,q,e,id,sp
    m=(value)
    print(m)
    c.execute('''select * from vendor_info''')
    data=c.fetchall()
    print(data)
    c.execute('''select vid from vendor_info where vname=?''',(m,))
    data=c.fetchall()
    id=data[0]
    id=id[0]	
    c.execute('''select vid,vname from vendor_info''') 
    q1=c.fetchall()   
    c.execute('''select pq from product_info where vid=?''',(id,)) 
    q=c.fetchall()
    Label(t,text="Available Quantity : ",bg='LIGHTGOLDENROD',fg="black",font=("Arial Bold", 10)).place(relx=0.25,rely=0.3)
    Label(t,text=q[0],bg='LIGHTGOLDENROD',font=("Arial", 10)).place(relx=0.55,rely=0.3)
    c.execute('''select psp from product_info where vid=?''',(id,)) 
    data=c.fetchall()
    sp=data[0]
    sp=sp[0]
    Label(t,text="Selling Price : ",bg='LIGHTGOLDENROD',fg="black",font=("Arial Bold", 10)).place(relx=0.25,rely=0.4)
    Label(t,text=sp,bg='LIGHTGOLDENROD',font=("Arial", 10)).place(relx=0.55,rely=0.4)
    Label(t,text="Quantity to sell:",bg='LIGHTGOLDENROD',fg="black",font=("Arial Bold", 10)).place(relx=0.25,rely=0.5)
    e=Entry(t)
    e.place(relx=0.55,rely=0.5)
    z=Button(t,text="ok",bg="Rosybrown3",fg="black",width=5,font=("Arial Bold", 10),command=sellclose).place(relx=0.45,rely=0.6)
    
def sellclose():
    print(m)
    z=e.get()
    b=0
    try:
        b=int(z)
    except ValueError:
           msg=messagebox.showerror('Value Error',"Inappropriate Value for Quantity,Only Integers are allowed.")
           vn(m)
    c=q[0]
    a=c[0]
    if(a<b):
        msg=messagebox.showerror('No Sufficient Stock',"Enter Appropriate Quantity .")
        vn(m) 
    left=a-b
    total=sp*b
    print(total)
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()	
    c.execute('''create table if not exists record (pname string,psp number,Qsold int)''')
    c.execute('''insert into record values(?,?,?)''',(p,sp,b))
    c.execute('''select * from record''')
    data= c.fetchall()
    c.execute('''update product_info set pq=? where vid=?''',(left,id,))
    conn.commit()
    Label(t,text="TOTAL PRICE : ",bg='LIGHTGOLDENROD',font=("Arial Bold", 10),fg="black").place(relx=0.25,rely=0.7)
    Label(t,text=total,bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.55,rely=0.7)
    z=Button(t,text="Done",bg="Rosybrown3",fg="black",width=5,font=("Arial Bold", 10),command=closeT).place(relx=0.45,rely=0.8)
    conn.close()

def top4():
    global e1,e2,t
    display=["VENDOR NAMES"]
    global variable,t
    t=Toplevel()
    t.title('PURCHASE PRODUCT')
    t.configure(background='LIGHTGOLDENROD')
    t.geometry("500x500")
    l=['laptop','camera','keyboard','charger']
    Label(t, text="Buy Produts From Vendors",bg='LIGHTGOLDENROD',font=("Arial Bold", 15)).place(relx=0.2,rely=0.01)
    Label(t, text="Select Product Name",bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.25,rely=0.1)    
    variable = StringVar(t)
    variable.set("Product")
    w = OptionMenu(t,variable,*l,command=ok_t4).place(relx=0.55,rely=0.1)

def ok_t4(value):
    global c,conn,p,d
    p=value
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    print("VENDOR :")
    c.execute('''select * from vendor_info''')
    c.execute('''select * from product_info''')
    c.execute('''select vid from product_info where pname=?''',(p,))
    vid=c.fetchall()
    l=[]
    for i in vid:
        i=i[0]
        c.execute('''select vname from vendor_info where vid=?''',(i,))
        data=c.fetchall()
        data=data[0]
        data=data[0]
        l.append(data)
    z=Button(t,text="Back",bg="GOLDENROD",font=("Arial Bold", 12),command=closeT).place(relx=0.35,rely=0.9)
    Label(t, text="Select Vendor Name",bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.25,rely=0.2)
    variable = StringVar(t)
    variable.set("VENDOR")
    w = OptionMenu(t,variable,*l,command=ok1_t4).place(relx=0.55,rely=0.2)
   
def ok1_t4(value):
    global m,q,e1,e2,e3,id
    m=(value)
    c.execute('''select vid from vendor_info where vname=?''',(m,))
    data=c.fetchall()
    id=data[0]
    id=id[0]	
    c.execute('''select pq from product_info where vid=?''',(id,)) 
    q=c.fetchall()
    q=q[0]
    Label(t,text="AVAILABLE QUANTITY : ",bg='LIGHTGOLDENROD',font=("Arial Bold", 10),fg="black").place(relx=0.25,rely=0.3)
    Label(t,text=q,bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.55,rely=0.3) 
    Label(t,text="Quantity to buy ",bg='LIGHTGOLDENROD',font=("Arial Bold", 10),fg="black").place(relx=0.22,rely=0.4)
    e1=Entry(t)
    e1.place(relx=0.55,rely=0.4)
    Label(t,text="Enter Purchase Price : ",bg='LIGHTGOLDENROD',font=("Arial Bold", 10),fg="black").place(relx=0.22,rely=0.5)
    e2=Entry(t)
    e2.place(relx=0.55,rely=0.5)
    Label(t,text="Enter Selling Price: ",bg='LIGHTGOLDENROD',font=("Arial Bold", 10),fg="black").place(relx=0.22,rely=0.6)
    e3=Entry(t)
    e3.place(relx=0.55,rely=0.6)    
    z=Button(t,text="OK",bg="GOLDENROD",font=("Arial Bold", 8),command=buyclose).place(relx=0.35,rely=0.7)
    

def buyclose():
    global sp,cp
    try:
        q1=int(e1.get())
    except ValueError:
           msg=messagebox.showerror('Value Error',"Inappropriate Value for Quantity,Only Integers are allowed.")
           vn(m)
    try:
        cp=float(e2.get())
    except ValueError:
           msg=messagebox.showerror('Value Error',"Inappropriate Value for Price , Only Integers are allowed.")
           vn(m)
    try:
        sp=float(e3.get())
    except ValueError:
           msg=messagebox.showerror('Value Error',"Inappropriate Value for Price , only Integers are allowed.")
           vn(m)
    a=q[0]
    print(a)
    left=a+q1
    total=sp*q1
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()	
    c.execute('''update product_info set pq=?,psp=?,pcp=? where vid=?''',(left,sp,cp,id,))
    conn.commit()
    Label(t,text="TOTAL PRICE : ",bg='LIGHTGOLDENROD',font=("Arial Bold", 10),fg="black").place(relx=0.25,rely=0.8)
    Label(t,text=total,bg='LIGHTGOLDENROD',font=("Arial Bold", 10)).place(relx=0.55,rely=0.8)
    z=Button(t,text="Done",bg="GOLDENROD",font=("Arial Bold", 12),command=closeT).place(relx=0.35,rely=0.9)
    conn.close()

def top5():
    global t
    t=Toplevel()
    t.title('DATA ANALYSIS')
    t.geometry("600x600")
    t.configure(background='Rosybrown1')
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
#    print(c.fetchall())
 
    conn.row_factory=sqlite3.Row
    crsr=conn.execute("SELECT * From PRODUCT_INFO")
    row=crsr.fetchone()
    titles=row.keys()
	
    data = c.execute("SELECT * FROM PRODUCT_INFO")
    if sys.version_info < (3,):
     f = open('output.csv', 'wb')
    else:
     f = open('output.csv', 'w', newline="")

    writer = csv.writer(f,delimiter=';')
    writer.writerow(titles)
    writer.writerows(data)
    f.close()
    Label(t, text="Data Analysis",bg='Rosybrown1',font=("Arial Bold", 15)).place(relx=0.35,rely=0.07)
    b1=Button(t,text="Pie Chart",bg="goldenrod",fg="black",height=2,width=10,command=pie).place(relx=0.25 ,rely=0.18)
    Label(t, text=" ( Most Selling Product ) ",bg='Rosybrown1',font=("Arial Bold", 10)).place(relx=0.45,rely=0.20)

    b2=Button(t,text="Graph",bg="orange",fg="black",height=2,width=10,command=show_graph).place(relx=0.25 ,rely=0.38)
    Label(t, text=" ( Profit % Vs Vendors ) ",bg='Rosybrown1',font=("Arial Bold", 10)).place(relx=0.45,rely=0.40)

    b4=Button(t,text="Back",bg="tomato",fg="black",height=3,width=10,command=closeT).place(relx=0.45 ,rely=0.58)
    conn.commit()
def pie():
    csvfile = open('output.csv','r')
    plots = csv.reader(csvfile,delimiter=',')
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    c.execute('''select distinct pname from product_info order by pname''')
    data=c.fetchall()
    labels = tuple()
    for i in data:
        labels=labels+(i[0],)
    c.execute('''select count(*) from PRODUCT_INFO group by pname ORDER BY pname''')
    data=c.fetchall()
    sizes=list()
    print(data)
    for i in data:
        i=i[0]
        i=int(i)
        sizes.append(i)
    print(sizes)
    print(labels)
    colors = ['salmon', 'gold','lightblue','lightgreen']
    plt.pie(sizes, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()
    conn.commit()
    conn.close()
    csvfile.close()

def show_graph():
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    x=[]
    y=[]
    p=[]
    c.execute('''select vname from vendor_info''')
    data=c.fetchall()
    for d in data[0:9]:
        d=d[0]
        d=str(d)
        c.execute('''select vid from vendor_info where vname=?''',(d,))
        vid=c.fetchall()
        vid=vid[0]
        vid=vid[0]
        c.execute('''select psp from product_info where vid=?''',(vid,))
        sp=c.fetchall()
        sp=sp[0]
        sp=float(sp[0])
        c.execute('''select pcp from product_info where vid=?''',(vid,))
        cp=c.fetchall()
        cp=cp[0]
        cp=float(cp[0])
        profit=(sp-cp)/cp
        per=profit*100
        print(per)
        p.append(per)
        x.append(d)
    print(x)
    print(p)
    plt.xlabel('Vendor Name')
    plt.ylabel('Profit %')
    plt.plot(x,p)
    plt.show()
    conn.commit()
    conn.close()

def top6():    
    global t
    t=Toplevel()
    t.geometry("300x500")
    t.configure(background='Rosybrown1')
    t.title("SOLD PRODUCT DETAILS") 
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    c.execute('''SELECT * FROM RECORD ''') 
    data=c.fetchall() 
    r=1
    c=0 
    Label(t, text="Product Name",bg="Rosybrown3",fg="black",width=10,font=("Arial Bold", 10)).grid(row=0, column=0)
    Label(t, text="Selling Price",bg="Rosybrown3",fg="black",width=10,font=("Arial Bold", 10)).grid(row=0, column=1)
    Label(t, text="Quantity Sold",bg="Rosybrown3",fg="black",width=10,font=("Arial Bold", 10)).grid(row=0, column=2)
    
    for index in data:
        c=0
        for i in index:
            Label(t, text=i,bg='Rosybrown1',fg="black").grid(row=r, column=c)
            c=c+1
        r=r+1
    print(r)	
    if(r<=10):
        r=(r/10)
        r=r-0.3
    else:
        r=0.9   
    z=Button(t,text="back",bg="Rosybrown3",fg="black",width=5,font=("Arial Bold", 10),command=closeT).place(relx=0.3,rely=0.85)
    conn.commit()
    conn.close()

    
def top7():
    global t
    t=Toplevel()
    t.geometry("400x550")
    t.title("VENDOR DETAILS") 
    t.configure(background='Rosybrown1')
    conn=sqlite3.connect("Inventory.db")
    c=conn.cursor()
    v=1056
    c.execute('''delete from vendor_info where vid=?''',(v,))
    c.execute('''select * from vendor_info''')
    data=c.fetchall() 
    Label(t, text="ID",bg="Rosybrown3",fg="black").grid(row=0, column=0)
    Label(t, text="VENDOR NAME",bg="Rosybrown3",fg="black").grid(row=0, column=1)
    Label(t, text="VENDOR ADDRESS",bg="Rosybrown3",fg="black").grid(row=0, column=2)
    Label(t, text="VENDOR CONTACT",bg="Rosybrown3",fg="black").grid(row=0, column=3)
    row=1
    col=0
    for index in data:
        col=0
        for i in index:
            Label(t, text=i,bg='Rosybrown1').grid(row=row, column=col)
            col=col+1
        row=row+1
    z=Button(t,text="back",bg="Rosybrown3",fg="black",width=5,font=("Arial Bold", 10),command=closeT).place(relx=0.3,rely=0.85)
    conn.commit()
    conn.close()

def closeT():
    t.destroy()
   
def close():
    root.destroy()

#anchor=CENTER
global root
root = Tk()
root.geometry("600x600")
root.configure(background='LIGHTGOLDENROD')
root.title("INVENTORY MANAGEMENT SYSTEM")
l1=Label(root,text="WELCOME  TO  ELECTRONICS   INVENTORY  MANAGEMENT  SYSTEM",font=("Arial Bold", 20),bg='LIGHTGOLDENROD',fg="black")
l1.place(relx=0.48, rely=0.05, anchor=CENTER)

b1=Button(root,text="AVAILABLE STOCK",bg="ORANGE",fg="black",height=2,width=25,command=top2).place(relx=0.35,rely=0.15)#grid(row=3,column=3)

#Label(root).grid(row=4,column=2)

b2=Button(root,text="SELL PRODUCTS",bg="GOLDENROD",fg="black",height=2,width=25,justify="center",command=top3).place(relx=0.35 ,rely=0.25)


b3=Button(root,text="PURCHASE PRODUCTS",bg="ORANGE",fg="black",height=2,width=25,justify="center",command=top4).place(relx=0.35 ,rely=0.35)


b4=Button(root,text="DATA ANALYASIS ",bg="GOLDENROD",fg="black",height=2,width=25,justify="center",command=top5).place(relx=0.35 ,rely=0.45)
		
b5=Button(root,text="ADD VENDOR INFORMATION",bg="ORANGE",fg="black",height=2,width=25,justify="center",command=top1).place(relx=0.35 ,rely=0.55)
		
b6=Button(root,text="VENDOR DETAILS",bg="GOLDENROD",fg="black",height=2,width=25,justify="center",command=top7).place(relx=0.35 ,rely=0.65)

b8=Button(root,text="HISTORY REPORT",bg="ORANGE",fg="BLACK",height=2,width=25,command=top6).place(relx=0.35,rely=0.75)

b7=Button(root,text="DONE",bg="TOMATO",fg="BLACK",height=3,width=15,command=close)#.grid(row=9,column=3)
b7.place(relx=0.38, rely=0.85)


root.mainloop()
