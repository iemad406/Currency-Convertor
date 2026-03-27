#import required libraries

from modules.currency import CurrencyConvertor

import tkinter as tk

from tkinter import messagebox

import mysql.connector

from mysql.connector import Error

class Login:
    
    #Fetch from database to authonticate user to login

    def userLogIn(self,username,password,root,userNameEntry,passwordEntry):
        try:
            conn=mysql.connector.connect(

                host="localhost",

                user="root",

                password="",

                database="final_project"
            )

            cursor=conn.cursor(dictionary=True)

            query="""
               
                SELECT user_id,username,password, CONCAT(first_name,' ',last_name) as fullName FROM users WHERE username=%s AND password=%s
            """
            cursor.execute(query,(username,password))

            results = cursor.fetchall()

            if len(results)>0:
                
                
                root.destroy()

                userId=results[0]['user_id']
               
                user_full_name=results[0]['fullName']

                currency_window=CurrencyConvertor(userId,user_full_name)

                currency_window.mainWindow()
                
            else:
                
                messagebox.showinfo('Invalid Cridentials','The username or password is invalid')

                userNameEntry.delete(0, tk.END)

                passwordEntry.delete(0, tk.END)

        except Error as e:

            print(f"There is an issue:{e}") 

    #UI login window
    
    def logInWindow(self):

        root=tk.Tk()

        #Set Main Window settings

        root.title("Login")

        root.geometry("580x390+200+180")
        
        root.resizable(False,False)

        root.iconbitmap(r"./images/login.ico")

        root.configure(bg="#000")

        #Label
        
        login_label=tk.Label(root, text="Login Form",fg="blue",bg="silver",font=("Arial", 12))

        login_label.pack(padx=200,pady=50)
        
        #UserName Label

        userNameLabel=tk.Label(root, text="UserName",fg="blue",font=("Arial", 12))

        userNameLabel.place(x=100,y=150)

        userNameEntry=tk.Entry(root,bg="silver",fg="blue")

        userNameEntry.place(x=230,y=150,width=250,height=22)
        
        #password

        passwordLabel=tk.Label(root, text="Password",fg="blue",font=("Arial", 12))

        passwordLabel.place(x=100,y=210)

        passwordEntry=tk.Entry(root,bg="silver",fg="blue") 

        passwordEntry.place(x=230,y=210,width=250,height=22)
        
        #Button

        login=tk.Button(root,text="login",bg="silver",fg="blue",command=lambda:self.userLogIn(userNameEntry.get(),passwordEntry.get(),root,userNameEntry,passwordEntry))

        login.place(x=245,y=270,width=150,height=60)
        
        login.config(font=("Arial", 17))

        root.mainloop()

