#Import Required Libries

from statistical.statistics import StatisticsAnalysis

from modules.currency_convertor import CurrencyConvertorApp

import tkinter as tk

from tkinter import ttk


class CurrencyConvertor:
    
    #Constructor

    def __init__(self,userID,fullName):

        self.user_id=userID

        self.userFullName=fullName

    def select_option(self,val,root):
        
        root.destroy()
        
        
        statistics=StatisticsAnalysis(val,self.user_id)
        
        statistics.fetch()
    
    def switchToCurrency(self,root):

        root.destroy()

        currency=CurrencyConvertorApp(self.userFullName,self.user_id)

        currency.mainWindow()

    def mainWindow(self):
        
        #Main Window Configuration

        root=tk.Tk()

        root.title("Currency Convertor Window")
        
        root.geometry("800x700+100+100")

        root.resizable(False,False)

        root.iconbitmap(r"./images/icon1.ico")
        
        root.config(bg="#000")

        #Label
         
        label=tk.Label(root,text="Currency Convertor Program Welcome",bg="silver",fg="blue",font=("Arial", 12),bd=5, relief="solid",padx=10,pady=10)

        label.pack(fill='x',padx=0,pady=0)

        #Comobobox
        
        options=[
            "Last Three months currency convertor Transactions",
            "Last Onth month Currency Convertor Transactions",
            "Last One Year Onth Currency Convertor Transactions"
        ]

        comobobox=ttk.Combobox(root,values=options,font=("Helvetica", 12), width=20)
        
        comobobox.set("Choose One Event")

        comobobox.pack(pady=50)

        #Button
        
        button=tk.Button(root,text="Done",bg="silver",fg="blue",font=("Helvetica", 12),width=26,command=lambda:self.select_option(comobobox.get(),root))
        
        button.pack(pady=67)

        convertor_currency_button=tk.Button(root,text="Currency Convertor",bg="silver",fg="blue",font=("Helvetica", 12),width=26,command=lambda:self.switchToCurrency(root))

        convertor_currency_button.pack(side=tk.LEFT, padx=(40,20),pady=70)
        
        payment_button=tk.Button(root,text="Payment",bg="silver",fg="blue",font=("Helvetica", 12),width=26)

        payment_button.pack(side=tk.LEFT, padx=(30,20),pady=70)

        root.mainloop()


