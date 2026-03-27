#Required Library

import tkinter as tk

from tkinter import messagebox

import string 

import random

import requests

import mysql.connector

from mysql.connector import Error

from datetime import datetime

class CurrencyConvertorApp:
    
    
    def __init__(self,fullName,userID):

        self.userName=fullName

        self.userIDEN=userID

    def getUserName(self):

        return self.userName

    def getUserId(self):

        return self.userIDEN  
    #Generate random number
    
    def generateRandomNumber(self,length=11):

        randomNumber=''.join(random.choice(string.digits) for _ in range(length))

        return randomNumber
    
    #Store the info of the transaction in the database

    def storeInfo(self,amount):
        try:

            id=self.generateRandomNumber()
            
            user_iden=self.getUserId()

            transactionAmount=amount

            currDate=datetime.now().date()

            currTime=datetime.now().time()
            
            user_full_name=self.getUserName()
            
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="final_project"
            )

            cursor=conn.cursor()
            
            
            
            query='''
                     INSERT INTO final_project.users_transaction
                     VALUES (%s,%s,%s,%s,%s,%s)
            '''
            
            data=(id,user_iden,transactionAmount,currDate,currTime,user_full_name)

            cursor.execute(query,data)

            conn.commit()

                        

        except Error as e:

            print(f"Error:{e}") 

        finally:

            cursor.close()

            conn.close()    

    #Method for currency convertor

    def convert(self,currency_from,currency_to,amount):
          
        api_key="f4ec9f68e9abc4d98a189062" 

        baseUrl=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

        url = baseUrl + currency_from

        try:

            response=requests.get(url)

            fetchedData=response.json()
            
            if response.status_code==200:

                conversionRate=fetchedData['conversion_rates'][currency_to]

                conversionAmount=amount*conversionRate
                
                self.storeInfo(float(conversionAmount))

            else: 

                messagebox.showinfo("Issues","There is an issue with complete proccess")

        except Exception as e:

            messagebox.showinfo("Issue with connection with the server",f"{e}")            

    def mainWindow(self):

        root=tk.Tk()

        root.title("Currency Convertor App")

        root.resizable(False,False)

        root.iconbitmap(r"./images/icon1.ico")  

        root.config(bg="#000")

        root.geometry("900x750+300+100")
        
        #Message Welcome Label

        meessageWelcome=tk.Label(root,text=f"Welcome {self.userName}",bg="silver",fg="blue",font=('Arial',23))

        meessageWelcome.pack(fill="x",padx=0,pady=0)
        
        #Currency Convertor Compnents
        
        #1 Labels

        amount=tk.Label(root,text="Amount",bg="silver",fg="blue",font=('Arial',23),width=15)

        amount.place(x=340,y=170)

        #Entry Fro Ammount

        amountEntry=tk.Entry(root,bg="silver",fg="blue",font=('Arial',23))
        
        amountEntry.place(x=349,y=240,width=260,height=25)
        
        #From Currency
        
        fromCurrency=tk.Label(root,text="From Currency",bg="silver",fg="blue",font=('Arial',23),width=15)
        
        fromCurrency.place(x=340,y=300)
        
        #From Currency Entry

        fromCurrencyEntry=tk.Entry(root,bg="silver",fg="blue",font=('Arial',23))

        fromCurrencyEntry.place(x=340,y=380,width=260,height=25)
        
        #To Currency

        toCurrency=tk.Label(root,text="To Currency",bg="silver",fg="blue",font=('Arial',23),width=15)

        toCurrency.place(x=340,y=430)
        
        #To Currency Entry

        toCurrencyEntry=tk.Entry(root,bg="silver",fg="blue",font=('Arial',23))

        toCurrencyEntry.place(x=340,y=499,width=260,height=25)
        
        #Button

        currencyButton=button=tk.Button(root,text="Done",bg="silver",fg="blue",font=("Helvetica", 12),width=26,command=lambda:self.convert(fromCurrencyEntry.get(),toCurrencyEntry.get(),float(amountEntry.get())))

        currencyButton.place(x=345,y=559,width=300,height=55)

        root.mainloop()  
        
