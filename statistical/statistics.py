#import required libraries

import tkinter as tk

from tkinter import ttk

import mysql.connector

from tkinter import messagebox

from mysql.connector import Error

class StatisticsAnalysis:
    
    def __init__(self,option,userID):

        self.userOption=option

        self.user_id=userID
    
    #Main Method to show Statistical

    def fetch(self):

        if self.userOption=="Last Three months currency convertor Transactions":

            res=self.fetchDataBasedOIntegerval(3)
            
            if len(res)!=0:

                self.showData(res)

            else:

                messagebox.showinfo("Empty Statistics","No statitics founded")    

        elif self.userOption=="Last Onth month Currency Convertor Transactions":

            res=self.fetchDataBasedOIntegerval(1)

            if len(res)!=0:

                self.showData(res)

            else:

                messagebox.showinfo("Empty Statistics","No statitics founded")    

        else:

            res=self.fetchDataBasedOIntegerval(12)

            if len(res)!=0:

                self.showData(res)

            else:

                messagebox.showinfo("Empty Statistics","No statitics founded")    

    #Fetch Data From DataBase
     
    def fetchDataBasedOIntegerval(self,interval):

        try:

            conn=mysql.connector.connect(

                host="localhost",
                user="root",
                password="",
                database="final_project"
            ) 

            cursor=conn.cursor(dictionary=True)

            query="""
            
                 SELECT transaction_id,transaction_amount_money,transaction_date,transaction_time FROM users_transaction WHERE transaction_date>=DATE_SUB(CURDATE(), INTERVAL %s MONTH) AND user_id1=%s

            """   

            cursor.execute(query,(interval,self.user_id))   

            results= cursor.fetchall()

            cursor.close()

            conn.close()

            return results
        
        except Error as e:

            print(f"There is an issue:{e}")
    
    #Show the data

    def showData(self,data):
        
        #Set Main Window configuration

        root=tk.Tk()

        root.title("Statistical")

        root.iconbitmap(r"./images/statistical_icon.ico")

        root.config(bg="#000") 
        
        root.geometry("700x650+270+190")

        root.resizable(False,False)

        #TreeWidjet

        tree=ttk.Treeview(root)

        tree['columns'] = ("Transaction ID","Transaction Amount of Money","Transaction Date","Transaction Time")
            
        tree.column("Transaction ID",width=50,minwidth=50,anchor=tk.CENTER) 

        tree.column("Transaction Amount of Money",width=100,minwidth=100,anchor=tk.CENTER)  

        tree.column("Transaction Date",width=50,minwidth=50,anchor=tk.CENTER)  

        tree.column("Transaction Time",width=150,minwidth=150,anchor=tk.CENTER)  
        
        tree.heading("Transaction ID",text="Transaction ID",anchor=tk.CENTER)

        tree.heading("Transaction Amount of Money",text="Transaction Amount of Money",anchor=tk.CENTER)

        tree.heading("Transaction Date",text="Transaction Date",anchor=tk.CENTER)

        tree.heading("Transaction Time",text="Transaction Time",anchor=tk.CENTER)
        
        for curr in data:

            tree.insert('',tk.END,values=[curr[key] for key in curr.keys()])

        #Add Horizintal scrolling

        vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)

        vsb.pack(side='right', fill='y')

        tree.configure(yscrollcommand=vsb.set)  

        tree.pack(expand=True, fill='both')

        root.mainloop()      

