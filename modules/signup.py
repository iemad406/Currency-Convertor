#import required libraries

from modules.login import Login

import random

import tkinter as tk

import mysql.connector

from mysql.connector import Error

from tkinter import messagebox

import string

from datetime import datetime

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

class SignUp:
    
    #Create random numbers

    def randomNumbers(self,length):

        randomNumber=''.join(random.choice(string.digits) for _ in range(length))

        return randomNumber
    
    #Send password ans user name into user's email

    def sendEmail(self,email,username,password):

        try:
            subject="User Credentials Information"

            source="ibrahimshakhatreh06@gmail.com"
        
            targetEmail=email

            body=f"The UserName:{username}\nThe Password:{password}"

            msg=MIMEMultipart()

            msg['From']=source

            msg['To']=targetEmail

            msg['Subject']=subject
            
            msg.attach(MIMEText(body, 'plain'))

            #Set the SMTP server authentication and configuration

            server=smtplib.SMTP("smtp.gmail.com",587)

            server.starttls()

            server.login('ibrahimshakhatreh06@gmail.com','knnsbtvtshdywzpc')
            
            text=msg.as_string()
            
            server.sendmail(source,targetEmail,text)

            server.quit()

        except Exception as e:

            print(f"There is an issue:{e}")

    #Insert info into database

    def insertIntoDataBase(self,firstNameEntry,lastNameEntry,emailEntry,root):

        first_name=firstNameEntry.get()

        last_name=lastNameEntry.get()

        email=emailEntry.get()
        
        currDate=datetime.now().date()

        currTime=datetime.now().time()

        randomUserName=self.randomNumbers(6)

        randomPassword=self.randomNumbers(6)

        randowmIden=self.randomNumbers(11)
        
        try:
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="final_project"
            )

            cursor = conn.cursor()

            query="""
            
                INSERT INTO users VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
            """
            self.sendEmail(email,randomUserName,randomPassword)

            data=(randowmIden,first_name,last_name,email,randomUserName,randomPassword,currDate,currTime)

            cursor.execute(query,data)

            conn.commit()
            
            messagebox.showinfo("success_inserted","The userinfo is inserted successfully")

            root.destroy()
            
            
            myLogin=Login()

            myLogin.logInWindow()

        except Error as e:

            print(f"There is an issue:{e}")

        finally:

            cursor.close()

            conn.close()

    #UI of signup 

    def signUpWindow(self):

        root=tk.Tk()

        #Set main window settings
        
        root.title("SignUp Form")

        root.geometry("690x500+200+200")

        root.resizable(False,False)

        root.iconbitmap(r"./images/signUpIcon.ico")
        
        root.config(bg="#000")

        #First Name Label

        signUpLabel=tk.Label(root,text="SignUp Form",bg="silver",fg="blue",font=("Arial", 19))

        signUpLabel.place(x=230,y=20)

        #First Name Label
        
        fn=tk.Label(root,text="First Name",bg="silver",fg="blue",font=("Arial", 19))

        fn.place(x=100,y=190)

        #First Name Entry

        fn_entry= tk.Entry(root,bg="silver",fg="blue",font=("Arial", 19))

        fn_entry.place(x=270,y=190,width=189,height=25)
        
        #Last Name Label

        ln=tk.Label(root,text="Last Name",bg="silver",fg="blue",font=("Arial", 19))
        
        ln.place(x=100,y=250)
        
        #Last Name Entry

        ln_entry=tk.Entry(root,bg="silver",fg="blue",font=("Arial", 19))

        ln_entry.place(x=270,y=260,width=189,height=25)
        
        #password label

        email_label=tk.Label(root,text="Email",bg="silver",fg="blue",font=("Arial", 19))
        
        email_label.place(x=100,y=300)

        #Password Entry

        email_entry=tk.Entry(root,bg="silver",fg="blue",font=("Arial", 19))

        email_entry.place(x=276,y=315,width=189,height=25)
        
        #Button

        signUpButton=tk.Button(root,text="Create Account",bg="silver",fg="blue",font=("Arial", 23),command=lambda:self.insertIntoDataBase(fn_entry,ln_entry,email_entry,root))

        signUpButton.place(x=265,y=400)

        root.mainloop()

