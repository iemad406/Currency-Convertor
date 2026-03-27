import tkinter as tk

class MainWindow:

    #switch to login window

    def switchToLogInForm(self,root):

        root.destroy()

        from modules.login import Login

        myLogInWindow=Login()

        myLogInWindow.logInWindow()
    
    #Switch into sign up form

    def switchToSignUpForm(self,root):

        root.destroy()

        from modules.signup import SignUp

        mySignUp=SignUp()

        mySignUp.signUpWindow()

    def mainWindow(self):
         # Main Window

        root = tk.Tk()

        root.geometry("700x400+500+200")

        root.title("Currency Converter")

        # Disable Re sizable

        root.resizable(False, False)

        # Set the icon

        root.iconbitmap(r"./images/icon1.ico")

        #Set the background color 
        
        root.configure(bg="#000")
        
        #Label

        label=tk.Label(root, text="Choose login/signup",fg="blue",bg="silver",font=("Arial", 12))

        label.pack(padx=200,pady=35)
        
        #Login Button

        login=tk.Button(root,text="Login", width=30,height=1,font=("Arial", 12),command=lambda:self.switchToLogInForm(root))

        login.pack(side=tk.LEFT, padx=(50, 20))

        login.configure(bg="silver", fg="white")
        
        #sign up

        Signup=tk.Button(root,text="Signup", width=30,height=1,font=("Arial", 12),command=lambda:self.switchToSignUpForm(root))

        Signup.pack(side=tk.LEFT, padx=(20, 10))

        Signup.configure(bg="silver", fg="white")

        root.mainloop()

window=MainWindow()

window.mainWindow()
