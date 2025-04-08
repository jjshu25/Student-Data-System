from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import sqlite3
import openpyxl
from tkinter import filedialog
from tkcalendar import DateEntry
import sys


#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

hiddenimports=['babel.numbers']

# Reporter & Coder (Potal, Guia) 
Student_Data_fm=Tk()
Student_Data_fm.geometry('925x500+400+200')
Student_Data_fm.title('Student Data')
Student_Data_fm.state("zoomed")


#background color
bg_color='#323233'


#Image icon
login_icon=PhotoImage(file=resource_path('icon\\icon.png'))
eye_icon1=PhotoImage(file=resource_path('icon\\eyeicon1.png'))
eye_icon2=PhotoImage(file=resource_path('icon\\eyeicon2.png'))
back1_btn=PhotoImage(file=resource_path('icon\\back.png'))
forward1_btn=PhotoImage(file=resource_path('icon\\forward.png'))
logout1_btn=PhotoImage(file=resource_path('icon\\logout.png'))
submit1_btn=PhotoImage(file=resource_path('icon\\submit.png'))
exit1_btn=PhotoImage(file=resource_path('icon\\exit.png'))
ckc1=PhotoImage(file=resource_path('icon\\ckc.png'))
logo=PhotoImage(file=resource_path('icon\\logo.png'))
home=PhotoImage(file=resource_path('icon\\home.png'))
searchlogo=PhotoImage(file=resource_path('icon\\searchlogo.png'))





#Checking initial database
def init_database():

    if os.path.exists(resource_path('students_account_lists.db')):
        
        connection=sqlite3.connect(resource_path('students_account_lists.db'))

        cursor=connection.cursor()

        cursor.execute("""
        SELECT * FROM data
        """)
        connection.commit()  # Commit the changes
        print(cursor.fetchall())
        connection.close()  # Close the connection

    
    else:
        
        connection=sqlite3.connect(resource_path('students_account_lists.db'))

        cursor=connection.cursor()
        
        cursor.execute("""
        CREATE TABLE data(
        Username text, 
        Password text, 
        Name text, 
        Age text, 
        Date_of_Birth text, 
        Address text, 
        Contact_No text, 
        Guardians_Name text, 
        Guardians_Contact_No text, 
        Elementary text, 
        High_School text, 
        Senior_High_School text, 
        College text, 
        Semester text, 
        Subjects_Name text, 
        Subjects_Description text, 
        Credits_Units text,
        Year_Level
        )""")

    if os.path.exists(resource_path('admin_data_lists.db')):
        
        connection=sqlite3.connect(resource_path('admin_data_lists.db'))

        cursor=connection.cursor()

        cursor.execute("""
        SELECT * FROM data
        """)
        connection.commit()  # Commit the changes
        print(cursor.fetchall())
        connection.close()  # Close the connection

    
    else:
        
        connection=sqlite3.connect(resource_path('admin_data_lists.db'))

        cursor=connection.cursor()
        
        cursor.execute("""
        CREATE TABLE data(
        Username text, 
        Password text, 
        Name text, 
        Age text, 
        Date_of_Birth text, 
        Address text, 
        Contact_No text, 
        Guardians_Name text, 
        Guardians_Contact_No text, 
        Elementary text, 
        High_School text, 
        Senior_High_School text, 
        College text, 
        Semester text, 
        Subjects_Name text, 
        Subjects_Description text, 
        Credits_Units text,
        Year_Level
        )""")
    

    if os.path.exists(resource_path('first_year.db')):
        
        connection=sqlite3.connect(resource_path('first_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        SELECT * FROM First_Sem
        """)

        cursor1.execute("""
        SELECT * FROM Second_Sem
        """)
        connection.commit()  # Commit the changes
        print(cursor.fetchall())
        print(cursor1.fetchall())
        connection.close()  # Close the connection

    
    else:
        
        connection=sqlite3.connect(resource_path('first_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        CREATE TABLE First_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")
        
        cursor1.execute("""
        CREATE TABLE Second_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")

    if os.path.exists(resource_path('second_year.db')):
        
        connection=sqlite3.connect(resource_path('second_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        SELECT * FROM First_Sem
        """)

        cursor1.execute("""
        SELECT * FROM Second_Sem
        """)
        connection.commit()  # Commit the changes
        print(cursor.fetchall())
        print(cursor1.fetchall())
        connection.close()  # Close the connection

    
    else:
        
        connection=sqlite3.connect(resource_path('second_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        CREATE TABLE First_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")
        
        cursor1.execute("""
        CREATE TABLE Second_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")

    if os.path.exists(resource_path('third_year.db')):
        
        connection=sqlite3.connect(resource_path('third_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        SELECT * FROM First_Sem
        """)

        cursor1.execute("""
        SELECT * FROM Second_Sem
        """)
        connection.commit()  # Commit the changes
        print(cursor.fetchall())
        print(cursor1.fetchall())
        connection.close()  # Close the connection

    
    else:
        
        connection=sqlite3.connect(resource_path('third_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        CREATE TABLE First_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")
        
        cursor1.execute("""
        CREATE TABLE Second_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")

    if os.path.exists(resource_path('fourth_year.db')):
        
        connection=sqlite3.connect(resource_path('fourth_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        SELECT * FROM First_Sem
        """)

        cursor1.execute("""
        SELECT * FROM Second_Sem
        """)
        connection.commit()  # Commit the changes
        print(cursor.fetchall())
        print(cursor1.fetchall())
        connection.close()  # Close the connection

    
    else:
        
        connection=sqlite3.connect(resource_path('fourth_year.db'))

        cursor=connection.cursor()
        cursor1=connection.cursor()

        cursor.execute("""
        CREATE TABLE First_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")
        
        cursor1.execute("""
        CREATE TABLE Second_Sem(
        SubjectName text, 
        SubjectDescription text, 
        CreditsUnits text, 
        Grades text, 
        Remarks text, 
        Name text 
        )""")

#Adding/Inserting of data
def add_data(Username, Password, Name, Age, Date_of_Birth, Address, Contact_No, Guardians_Name, Guardians_Contact_No, Elementary, High_School, Senior_High_School, College, Semester, Subjects_Name, Subjects_Description, Credits_Units,Year_Level):
    connection = sqlite3.connect(resource_path('students_account_lists.db'))
    connection1 = sqlite3.connect(resource_path('admin_data_lists.db'))

    cursor = connection.cursor()  # Commit the changes
    cursor1 = connection1.cursor()  # Close the connection

    cursor.execute(f"""
    INSERT INTO data VALUES('{Username}', '{Password}', '{Name}', '{Age}', '{Date_of_Birth}', '{Address}', '{Contact_No}', '{Guardians_Name}', '{Guardians_Contact_No}', '{Elementary}', '{High_School}', '{Senior_High_School}', '{College}', '{Semester}', '{Subjects_Name}', '{Subjects_Description}', '{Credits_Units}','{Year_Level}')
    """)

    cursor1.execute(f"""
    INSERT INTO data VALUES('{Username}', '{Password}', '{Name}', '{Age}', '{Date_of_Birth}', '{Address}', '{Contact_No}', '{Guardians_Name}', '{Guardians_Contact_No}', '{Elementary}', '{High_School}', '{Senior_High_School}', '{College}', '{Semester}', '{Subjects_Name}', '{Subjects_Description}', '{Credits_Units}','{Year_Level}')
    """)

    connection.commit()  # Commit the changes
    connection.close()  # Close the connection
    connection1.commit()  # Commit the changes
    connection1.close()  # Close the connection


#Confirmation box for exiting or not
def confirmation_box(message):

    #Can store true or false in variable
    answer=BooleanVar()
    answer.set(False)

    #Getting the answer of the user(if Yes or No)
    def action(ans):
        answer.set(ans)
        confirmation_box_fm.destroy()

    #Frame of its content
    confirmation_box_fm=Frame(Student_Data_fm,highlightbackground=bg_color,highlightthickness=3)
    confirmation_box_fm.place(x=620,y=190,width=320,height=320)

    #Message on its box
    message_lb=Label(confirmation_box_fm,text=message,font=('Bold',15))
    message_lb.pack(padx=20)

    #No button on its box
    no_btn=Button(confirmation_box_fm,text='No',font=('Bold',15),bd=0,bg='#1e1ee4',fg='white',command=lambda: action(False))
    no_btn.place(x=50,y=160,width=80)

    #Yes button on its box
    yes_btn=Button(confirmation_box_fm,text='Yes',font=('Bold',15),bd=0,bg='#1e1ee4',fg='white',command=lambda: action(True))
    yes_btn.place(x=190,y=160,width=80)

    #Waiting until user press any button
    Student_Data_fm.wait_window(confirmation_box_fm)
    
    return answer.get()


def message_box(message):

    #Frame of its content
    message_box1_fm=Frame(Student_Data_fm,highlightbackground=bg_color,highlightthickness=3)
    message_box1_fm.place(x=620,y=190,width=350,height=300)

    #Close/Exit button
    close_btn=Button(message_box1_fm,text='X',bd=0,font=('Bold', 13), fg=bg_color,command=lambda: message_box1_fm.destroy())
    close_btn.place(x=315,y=5)

    #Message label
    message_lb=Label(message_box1_fm,text=message,font=('Bold',15))
    message_lb.pack(pady=50)


def Student_Data():
    
    #Forwarding to Login and Deleting Student Data1's content
    def forward_to_Login():
        Student_Data1_fm.destroy()
        Login()

    #Forwarding to Admin and Deleting Student Data1's content
    def forward_to_Admin():
        Student_Data1_fm.destroy()
        Admin()

    #Forwarding to Sign Up and Deleting Student Data1's content
    def forward_to_Sign_up():
        Student_Data1_fm.destroy()
        Sign_up()

    #Frame of its container
    Student_Data1_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Student Data
    heading_lb=Label(Student_Data1_fm,text='STUDENT DATA',bg=bg_color,fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=35,y=0,width=325)

    #Student button
    student_login_btn=Button(Student_Data1_fm,text='LOGIN',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_Login)
    student_login_btn.place(x=100,y=100,width=200)

    #Admin button
    admin_login_btn=Button(Student_Data1_fm,text='ADMIN',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_Admin)
    admin_login_btn.place(x=100,y=200,width=200)

    #Sign up button
    sign_up_login_btn=Button(Student_Data1_fm,text='SIGN UP',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_Sign_up)
    sign_up_login_btn.place(x=100,y=300,width=200)

    #Frame of its container
    Student_Data1_fm.pack(pady=30)
    Student_Data1_fm.pack_propagate(False)
    Student_Data1_fm.place(x=570,y=180)
    Student_Data1_fm.configure(width=400,height=420)

# Reporter & Coder(Roxas,Papa,Arocha)
def Login():

    #Forwarding to Student_Data and Deleting the content of Login
    def forward_to_Student_Data():
        Student_Data2_fm.destroy()
        Student_Data()

    #Frame of its container
    Student_Data2_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of LOGIN
    heading_lb=Label(Student_Data2_fm,text='LOGIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=403,y=100,width=325)

    #Image icon 
    login1_icon_lb=Label(Student_Data2_fm, image=login_icon,bd=0)
    login1_icon_lb.place(x=515,y=150,width=100,height=100)

    #Lock and unlock password function
    def unlock():
        if password_ent['show'] == '*':
            password_ent.config(show='')
            eye_icon_btn.config(image=eye_icon2)
        else:
            password_ent.config(show='*')
            eye_icon_btn.config(image=eye_icon1)  

    #Insert and delete of username
    def on_enter(e):
        username_ent.delete(0,'end')

    def on_leave(e):
        name=username_ent.get()
        if name=='':
            username_ent.insert(0,'Username')

    #Username
    username_ent=Entry(Student_Data2_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER)
    username_ent.place(x=425,y=280)

    #Placeholder of Username
    username_ent.insert(0,'Username')
    username_ent.bind('<FocusIn>', on_enter)
    username_ent.bind('<FocusOut>', on_leave)
    
    #Insert and delete of password
    def on_enter(e):
        password_ent.delete(0,'end')

    def on_leave(e):
            name=password_ent.get()
            if name=='':
                password_ent.insert(0,'Password')


    #Proceed to Admin Menu on enter key event if username and password is correct
    def proceed(e):
        check_login()

    #Password
    password_ent=Entry(Student_Data2_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER)
    password_ent.place(x=425,y=330)
    password_ent.bind('<Return>',proceed)

    #Placeholder of Password
    password_ent.insert(0,'Password')
    password_ent.bind('<FocusIn>', on_enter)
    password_ent.bind('<FocusOut>', on_leave)

    
    #Checking the username and password if it is in database
    def check_login():
        username = username_ent.get()
        password = password_ent.get()

        # Connect to the database
        connection = sqlite3.connect(resource_path('students_account_lists.db'))
        cursor = connection.cursor()

        # Check if the username and password are correct
        cursor.execute("SELECT * FROM data WHERE Username = ? AND Password = ?", (username, password))
        result = cursor.fetchone()

        if result:
            # Successful login, proceed to Login1 window
            global logged_in_user  # Declare logged_in_user as a global variable
            logged_in_user = username  # Store the logged-in user's username
            connection.close()
            Student_Data2_fm.destroy()
            Login1()
        else:
            # Display error message
            messagebox.showerror("Login Error", "Incorrect username or password.")
            connection.close()

    #Enter button
    enter_btn=Button(Student_Data2_fm,text="Enter",font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,width=5,bg='#6aa84f',fg='white',relief=RAISED,command=check_login)
    enter_btn.place(x=520,y=370)

    #Eye icon(lock)
    eye_icon_btn=Button(Student_Data2_fm,image=eye_icon1,bd=0,relief=RAISED,command=unlock)
    eye_icon_btn.place(x=700,y=330)

    #Back button icon
    back_btn=Button(Student_Data2_fm, image=back1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    back_btn.place(x=30,y=510)

    #Frame to its container
    Student_Data2_fm.pack(pady=100)
    Student_Data2_fm.pack_propagate(False)
    Student_Data2_fm.configure(width=1100,height=620)

# Reporter & Coder(Conarco,Montejo)
def Admin():

    #Calling Student_Data and destroying Login's content
    def forward_to_Student_Data():
        Student_Data3_fm.destroy()
        Student_Data()

    #Frame of its container
    Student_Data3_fm = Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of ADMIN
    heading_lb=Label(Student_Data3_fm,text='ADMIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=403,y=100,width=325)

    #Image icon 
    login_icon_lb=Label(Student_Data3_fm, image=login_icon,bd=0)
    login_icon_lb.place(x=515,y=150,width=100,height=100)
    
    #Insert and delete of username
    def on_enter(e):
        username1_ent.delete(0,'end')

    def on_leave(e):
        name=username1_ent.get()
        if name=='':
            username1_ent.insert(0,'Username')
    
    #Username
    username1_ent=Entry(Student_Data3_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER)
    username1_ent.place(x=425,y=280)

    #Placeholder of Username
    username1_ent.insert(0,'Username')
    username1_ent.bind('<FocusIn>', on_enter)
    username1_ent.bind('<FocusOut>', on_leave)
    
    #Insert and delete of password
    def on_enter(e):
        password1_ent.delete(0,'end')

    def on_leave(e):
            name=password1_ent.get()
            if name=='':
                password1_ent.insert(0,'Password')

    #Proceed to Admin Menu on enter key event if username and password is correct
    def proceed1(e):
        check_login1()

    #Password
    password1_ent=Entry(Student_Data3_fm,font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,)
    password1_ent.place(x=425,y=330)
    password1_ent.bind('<Return>', proceed1)

    #Placeholder of Password
    password1_ent.insert(0,'Password')
    password1_ent.bind('<FocusIn>', on_enter)
    password1_ent.bind('<FocusOut>', on_leave)

    #Checking the username and password if it is in database 
    def check_login1():
        username = username1_ent.get()
        password = password1_ent.get()

        # Connect to the database
        connection = sqlite3.connect(resource_path('admin_data_lists.db'))
        cursor = connection.cursor()

        # Check if the username and password are correct
        cursor.execute("SELECT * FROM data WHERE Username = ? AND Password = ?", ("admin", password))
        result = cursor.fetchone()

        if result:
            connection.close()  # Successful login, proceed to Admin1 window
            Student_Data3_fm.destroy()
            Admin1()
        else:
            # Display error message
            messagebox.showerror("Login Error", "Incorrect username or password.")
            connection.close()

    #Enter Button
    enter1_btn=Button(Student_Data3_fm,text="Enter",font=('Franklin Gothic Demi (Headings)',18),justify=CENTER,width=5,bg='#6aa84f',fg='white',relief=RAISED,command=check_login1)
    enter1_btn.place(x=520,y=370)

    #Back button icon
    back_btn=Button(Student_Data3_fm, image=back1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    back_btn.place(x=30,y=510)

    #Frame of its container
    Student_Data3_fm.pack(pady=100)
    Student_Data3_fm.pack_propagate(False)
    Student_Data3_fm.configure(width=1100,height=620)

# Reporter & Coder(Potal,Guia)
def Sign_up():

    #Forwarding to Student Data and deleting the content of Sign Up
    def forward_to_Student_Data():  
        ans = confirmation_box(message='Do you want to exit\nSign Up form?')

        if ans:
            Student_Data4_fm.destroy()
            Student_Data()


    #Set values in combobox
    yearlevel_list = ['1st Year','2nd Year','3rd Year','4th Year']


    #Targeting highlighted entry box
    def remove_highlight_warning(entry):

        if entry['highlightbackground'] != 'Gray':
            if entry.get() != '':
                entry.config(highlightcolor=bg_color,highlightbackground='Gray')


    #Checking the inputs if the user already input something
    def check_input_validation():
        if frame_box.get() == '':
            frame_box.config(highlightcolor='red',highlightbackground='red')

            frame_box.focus()
            message_box(message='Username is required')

        elif frame_box1.get() == '':
            frame_box1.config(highlightcolor='red',highlightbackground='red')

            frame_box1.focus()
            message_box(message='Password is required')

        elif frame_box2.get() == '':
            frame_box2.config(highlightcolor='red',highlightbackground='red')

            frame_box2.focus()
            message_box(message='Name is required')

        elif frame_box3.get() == '':
            frame_box3.config(highlightcolor='red',highlightbackground='red')

            frame_box3.focus()
            message_box(message='Age is required')

        elif frame_box4.get() == '':
            frame_box4.config(highlightcolor='red',highlightbackground='red')

            frame_box4.focus()
            message_box(message='Date of Birth is required')

        elif frame_box5.get() == '':
            frame_box5.config(highlightcolor='red',highlightbackground='red')

            frame_box5.focus()
            message_box(message='Address is required')

        elif frame_box6.get() == '':
            frame_box6.config(highlightcolor='red',highlightbackground='red')

            frame_box6.focus()
            message_box(message='Contact Number is required')

        elif frame_box7.get() == '':
            frame_box7.config(highlightcolor='red',highlightbackground='red')

            frame_box7.focus()
            message_box(message="Guardian's Name is required")

        elif frame_box8.get() == '':
            frame_box8.config(highlightcolor='red',highlightbackground='red')

            frame_box8.focus()
            message_box(message="Guardian's Contact Number is required")

        elif frame_box9.get() == '':
            frame_box9.config(highlightcolor='red',highlightbackground='red')

            frame_box9.focus()
            message_box(message='Elementary is required')

        elif frame_box10.get() == '':
            frame_box10.config(highlightcolor='red',highlightbackground='red')

            frame_box10.focus()
            message_box(message='High School is required')

        elif frame_box11.get() == '':
            frame_box11.config(highlightcolor='red',highlightbackground='red')

            frame_box11.focus()
            message_box(message='Senior High School is required')

        elif frame_box12.get() == '':
            frame_box12.config(highlightcolor='red',highlightbackground='red')

            frame_box12.focus()
            message_box(message='College is required')

        elif frame_box13.get() == '':
            frame_box13.config(highlightcolor='red',highlightbackground='red')

            frame_box13.focus()
            message_box(message='Semester is required')

        elif frame_box14.get() == '':
            frame_box14.config(highlightcolor='red',highlightbackground='red')

            frame_box14.focus()
            message_box(message='Subjects Name is required')

        elif frame_box15.get() == '':
            frame_box15.config(highlightcolor='red',highlightbackground='red')

            frame_box15.focus()
            message_box(message='Subjects Description is required')

        elif frame_box16.get() == '':
            frame_box16.config(highlightcolor='red',highlightbackground='red')

            frame_box16.focus()
            message_box(message='Credits Units is required')

        elif frame_box17.get() == '':
            frame_box17.config(highlightcolor='red',highlightbackground='red')

            frame_box17.focus()
            message_box(message='Year Level is required')

        else:
            add_data(
                     Username=frame_box.get(),
                     Password=frame_box1.get(),
                     Name=frame_box2.get(),
                     Age=frame_box3.get(),
                     Date_of_Birth=frame_box4.get(),
                     Address=frame_box5.get(),
                     Contact_No=frame_box6.get(),
                     Guardians_Name=frame_box7.get(),
                     Guardians_Contact_No=frame_box8.get(),
                     Elementary=frame_box9.get(),
                     High_School=frame_box10.get(),
                     Senior_High_School=frame_box11.get(),
                     College=frame_box12.get(),
                     Semester=frame_box13.get(),
                     Subjects_Name=frame_box14.get(),
                     Subjects_Description=frame_box15.get(),
                     Credits_Units=frame_box16.get(),
                     Year_Level=frame_box17.get(),)
            message_box('Account Successful Created')
            
            
    #Frame of its container
    Student_Data4_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Signup frame label
    student_login_lb=Label(Student_Data4_fm,text='SIGN UP',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED)
    student_login_lb.place(x=700,y=50,width=200)

    #Heading of Username 
    user_lb=Label(Student_Data4_fm,text='Username:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    user_lb.place(x=180,y=150,width=325)

    #Framebox of Username 
    frame_box=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box.place(x=400,y=150)

    #Binding
    frame_box.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box))

    #Heading of Password
    pass_lb=Label(Student_Data4_fm,text='Password:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    pass_lb.place(x=180,y=210,width=325)

    #Framebox of Password
    frame_box1=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box1.place(x=400,y=210)

    #Binding
    frame_box1.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box1))

    #Heading of Name
    name_lb=Label(Student_Data4_fm,text='Name:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    name_lb.place(x=200,y=270,width=325)

    #Framebox of Name
    frame_box2=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box2.place(x=400,y=270,width=185)

    #Binding
    frame_box2.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box2))

    #Heading of Age
    age_lb=Label(Student_Data4_fm,text='Age:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    age_lb.place(x=205,y=330,width=325)

    #Framebox of Age
    frame_box3=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box3.place(x=400,y=330)

    #Binding
    frame_box3.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box3))

    #Heading of Date of Birth
    birth_lb=Label(Student_Data4_fm,text='Date of Birth:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    birth_lb.place(x=170,y=390,width=325)

    #Framebox of Date of Birth
    frame_box4=DateEntry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12))
    frame_box4.place(x=400,y=390)

    #Heading of Address
    address_lb=Label(Student_Data4_fm,text='Address:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    address_lb.place(x=185,y=450,width=325)

    #Framebox of Address
    frame_box5=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box5.place(x=400,y=450)

    #Binding
    frame_box5.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box5))

    #Heading of Contact Number
    number_lb=Label(Student_Data4_fm,text='Contact Number:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    number_lb.place(x=155,y=510,width=325)

    #Framebox of Contact Number
    frame_box6=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box6.place(x=400,y=510)

    #Binding
    frame_box6.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box6))

    #Heading of Guardian's Name
    guardiansname_lb=Label(Student_Data4_fm,text="Guardian's Name:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    guardiansname_lb.place(x=150,y=565,width=325)

    #Framebox of Guardian's Name
    frame_box7=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box7.place(x=400,y=565)

    #Binding
    frame_box7.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box7))

    #Heading of Guardian's Contact Number
    guardianCN_lb=Label(Student_Data4_fm,text="Guardian's Contact Number:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    guardianCN_lb.place(x=110,y=620,width=325)

    #Framebox of Guardian's Contact Number
    frame_box8=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box8.place(x=400,y=620)

    #Binding
    frame_box8.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box8))

    #Heading of Elementary
    elementary_lb=Label(Student_Data4_fm,text='Elementary:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    elementary_lb.place(x=700,y=150,width=325)

    #Framebox of Elementary
    frame_box9=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box9.place(x=920,y=150)

    #Binding
    frame_box9.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box9))

    #Heading of High School
    highschool_lb=Label(Student_Data4_fm,text='High School:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    highschool_lb.place(x=695,y=210,width=325)

    #Framebox of High School
    frame_box10=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box10.place(x=920,y=210)

    #Binding
    frame_box10.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box10))

    #Heading of Senior High School
    seniorhigh_lb=Label(Student_Data4_fm,text='Senior High School:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    seniorhigh_lb.place(x=665,y=270,width=325)

    #Framebox of Senior High School
    frame_box11=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box11.place(x=920,y=270)

    #Binding
    frame_box11.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box11))

    #Heading of College
    college_lb=Label(Student_Data4_fm,text='College:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    college_lb.place(x=710,y=325,width=325)

    #Framebox of College
    frame_box12=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box12.place(x=920,y=325)

    #Binding
    frame_box12.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box12))

    #Heading of Semester
    semester_lb=Label(Student_Data4_fm,text='Semester:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    semester_lb.place(x=705,y=390,width=325)

    #Framebox of Semester
    frame_box13=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box13.place(x=920,y=390)

    #Binding
    frame_box13.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box13))

    #Heading of Subjects Name
    subjectname_lb=Label(Student_Data4_fm,text='Subjects Name:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    subjectname_lb.place(x=680,y=450,width=325)

    #Framebox of Subjects Name
    frame_box14=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box14.place(x=920,y=450)

    #Binding
    frame_box14.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box14))

    #Heading of Subjects Description
    subjectD_lb=Label(Student_Data4_fm,text='Subjects Description:',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    subjectD_lb.place(x=660,y=510,width=325)

    #Framebox of Subjects Description
    frame_box15=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box15.place(x=920,y=510)

    #Binding
    frame_box15.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box15))

    #Heading of Credit Units
    credits_lb=Label(Student_Data4_fm,text="Credit Units:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    credits_lb.place(x=695,y=565,width=325)

    #Framebox of Credit Units
    frame_box16=Entry(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),highlightcolor='#1e1ee4',highlightbackground='gray',highlightthickness=2)
    frame_box16.place(x=920,y=565)

    #Binding
    frame_box16.bind('<KeyRelease>', lambda e: remove_highlight_warning(entry=frame_box16))

    #Heading of Year Level
    yearlvl_lb=Label(Student_Data4_fm,text="Year Level:",bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',12,'bold'))
    yearlvl_lb.place(x=700,y=620,width=325)

    #Combobox of Year Level
    frame_box17=ttk.Combobox(Student_Data4_fm,font=('Franklin Gothic Demi (Headings)',12),state='readonly',values=yearlevel_list)
    frame_box17.place(x=920,y=620)

    # Set the initial selection to the placeholder value
    frame_box17.current(0)
    
    #Exit button
    exit_btn=Button(Student_Data4_fm, image=exit1_btn,bd=0,bg='#323233',command=forward_to_Student_Data)
    exit_btn.place(x=880,y=660,width=110)

    #Submit button
    submit_btn=Button(Student_Data4_fm, image=submit1_btn,bd=0,bg='#323233',command=check_input_validation)
    submit_btn.place(x=1020,y=660,width=110)

    #Frame to its container
    Student_Data4_fm.pack(pady=100)
    Student_Data4_fm.pack_propagate(False)
    Student_Data4_fm.place(x=0,y=0)
    Student_Data4_fm.configure(width=1600,height=1000)


def Login1():

    #Forwarding to Student Data and destroying the content of Login1
    def forward_to_Student_Data():
        Student_Data5_fm.destroy()
        Student_Data()

    #Forwarding to first_year_user and destroying the content of Login1
    def forward_to_first_year_user():
        Student_Data5_fm.destroy()
        first_year_user()

    #Forwarding to second_year_user and destroying the content of Login1
    def forward_to_second_year_user():
        Student_Data5_fm.destroy()
        second_year_user()

    #Forwarding to third_year_user and destroying the content of Login1
    def forward_to_third_year_user():
        Student_Data5_fm.destroy()
        third_year_user()

    #Forwarding to fourth_year_user and destroying the content of Login1
    def forward_to_fourth_year_user():
        Student_Data5_fm.destroy()
        fourth_year_user()

    #Frame of its container
    Student_Data5_fm=Frame(Student_Data_fm, bg=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Student
    heading_lb=Label(Student_Data5_fm,text='STUDENT',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=455,y=50,width=200)

    #Image icon 
    login_icon_lb=Label(Student_Data5_fm, image=login_icon,bd=0)
    login_icon_lb.place(x=500,y=100,width=100,height=100)

    #1st year button
    firstyear_btn=Button(Student_Data5_fm,text='FIRST YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_first_year_user)
    firstyear_btn.place(x=450,y=220,width=200)

    #2nd year button
    secondyear_btn=Button(Student_Data5_fm,text='SECOND YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_second_year_user)
    secondyear_btn.place(x=450,y=300,width=200)

    #3rd year button
    thirdyear_btn=Button(Student_Data5_fm,text='THIRD YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_third_year_user)
    thirdyear_btn.place(x=450,y=380,width=200)

    #4th year button
    fourthyear_btn=Button(Student_Data5_fm,text='FOURTH YEAR',bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_fourth_year_user)
    fourthyear_btn.place(x=450,y=460,width=200)

    #logout button
    logout_btn=Button(Student_Data5_fm,image=logout1_btn,bd=0,bg='#323233',relief=RAISED,command=forward_to_Student_Data)
    logout_btn.place(x=940,y=520,width=120)

    #Frame of its container
    Student_Data5_fm.pack(pady=100)
    Student_Data5_fm.pack_propagate(False)
    Student_Data5_fm.configure(width=1100,height=620)


def Admin1():

    #Forwarding to Admin1 and destroying the content of Admin1
    def forward_to_Admin():
        Student_Data6_fm.destroy()
        Admin()

    #Forwarding to view_student_info and destroying the content of Admin1
    def forward_to_view_student_info():
        Student_Data6_fm.destroy()
        view_student_info()

    #Forwarding to edit_student_info and destroying the content of Admin1
    def forward_to_edit_student_info():
        Student_Data6_fm.destroy()
        edit_student_info()

    #Forwarding to print_student_info and destroying the content of Admin1
    def forward_to_print_student_info():
        Student_Data6_fm.destroy()
        print_student_info()

    #Frame of its container
    Student_Data6_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of Student
    heading_lb=Label(Student_Data6_fm,text='ADMIN',bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.place(x=453,y=50,width=200)

    #Image icon 
    login_icon_lb=Label(Student_Data6_fm, image=login_icon,bd=0)
    login_icon_lb.place(x=500,y=100,width=100,height=100)

    #View students info button
    firstyear_btn=Button(Student_Data6_fm,text="VIEW STUDENT'S INFO",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_view_student_info)
    firstyear_btn.place(x=400,y=220,width=300)

    #Edit students info button
    secondyear_btn=Button(Student_Data6_fm,text="EDIT STUDENT'S INFO",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_edit_student_info)
    secondyear_btn.place(x=400,y=300,width=300)

    #Print students info button
    thirdyear_btn=Button(Student_Data6_fm,text="PRINT STUDENT'S INFO",bg='#1e5fe4',fg='white',font=('Franklin Gothic Demi (Headings)',18,'bold'),bd=0,relief=RAISED,command=forward_to_print_student_info)
    thirdyear_btn.place(x=400,y=380,width=300)

    #logout button
    logout_btn=Button(Student_Data6_fm,image=logout1_btn,bd=0,bg='#323233',relief=RAISED,command=forward_to_Admin)
    logout_btn.place(x=940,y=520,width=120)

    #Frame of its container
    Student_Data6_fm.pack(pady=100)
    Student_Data6_fm.pack_propagate(False)
    Student_Data6_fm.configure(width=1100,height=620)

# Reporter & Coder(Conarco,Montejo)
def first_year_user():

    #Forwarding to Login1 and deleting the content of first_year_user
    def forward_to_Login1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data7_fm.destroy()
            Login1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']

    #Frame of its container
    Student_Data7_fm=Frame(Student_Data_fm, bg=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data7_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data Logo
    studentlogo_lb=Label(Student_Data7_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data7_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Login1)
    profilelogo_btn.place(x=1270,y=5)

    def display_student_data():

        global name_check

        # Connect to the database
        connection = sqlite3.connect(resource_path('students_account_lists.db'))
        connection1 = sqlite3.connect(resource_path('first_year.db'))

        cursor = connection.cursor()
        cursor1 = connection1.cursor()
        
        # Fetch the data for the logged-in user from the database
        cursor.execute("SELECT * FROM data WHERE Username = ?", (logged_in_user,))
        user_data = cursor.fetchone()

        name_check = user_data[2]

        if user_data:
            # Check if the Year Level matches the desired value
            desired_year_level = "1st Year"
            if user_data[17] == desired_year_level:    

                # Fetch the subject data for the logged-in user from the First_Sem table
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (user_data[2],))
                subject_data = cursor1.fetchall()

                # Create labels to display the user data
                data_label = Label(Student_Data7_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label.place(x=350, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[7], user_data[8], user_data[9]
                )
                data_label.config(text=row_text, fg='white')

                # Other label that was displayed at the right
                data_label1 = Label(Student_Data7_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label1.place(x=890, y=100)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    user_data[10], user_data[11], user_data[12], user_data[13], user_data[14], user_data[15], user_data[16], user_data[17]
                )
                data_label1.config(text=row_text, fg='white')

                # Display the subject data in the table
                for i, row_data in enumerate(subject_data, start=1):
                    for j, field_data in enumerate(row_data):
                        input_fields[i-1][j].insert(0, field_data)

            else:
                #If Year Level does not match, it will display "No data found for the logged-in user."
                data_label = Label(Student_Data7_fm, text="No data found for the logged-in user.", font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233')
                data_label.place(x=350, y=100)        

        # Close the database connection
        connection.close()

    # Create the table
    table_frame = Frame(Student_Data7_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']  
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)

    # Create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data7_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    # Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    #Selecting between 1st Sem and 2nd Sem
    def view_entries(event):
        selected_option = select_sem_btn.get()

        if selected_option == '1st Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('first_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the First_Sem table
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?",(name_check,))
            first_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(first_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)

            # Close the database connection
            conn.close()

        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('first_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the Second_Sem tables
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?",(name_check,))
            second_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(second_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)


            # Close the database connections
            conn.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data7_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the view_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', view_entries)


    # Frame of its container
    Student_Data7_fm.pack(fill='both', expand=1)
    Student_Data7_fm.pack_propagate(False)
    display_student_data()

# Reporter & Coder(Roxas,Papa,Chanchan)
def second_year_user():

    #Forwarding to Login1 and deleting the content of second_year_user
    def forward_to_Login1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data8_fm.destroy()
            Login1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']

    #Frame of its container
    Student_Data8_fm=Frame(Student_Data_fm, bg=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data8_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data Logo
    studentlogo_lb=Label(Student_Data8_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data8_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Login1)
    profilelogo_btn.place(x=1270,y=5)

    def display_student_data():

        global name_check
        
        # Connect to the database
        connection = sqlite3.connect(resource_path('students_account_lists.db'))
        connection1 = sqlite3.connect(resource_path('second_year.db'))

        cursor = connection.cursor()
        cursor1=connection1.cursor()
        
        # Fetch the data for the logged-in user from the database
        cursor.execute("SELECT * FROM data WHERE Username = ?", (logged_in_user,))
        user_data = cursor.fetchone()

        name_check = user_data[2]

        if user_data:
            # Check if the Year Level matches the desired value
            desired_year_level = "2nd Year"
            if user_data[17] == desired_year_level:

                # Fetch the subject data for the logged-in user from the First_Sem table
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (user_data[2],))
                subject_data = cursor1.fetchall()

                # Create labels to display the user data
                data_label = Label(Student_Data8_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label.place(x=350, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[7], user_data[8], user_data[9]
                )
                data_label.config(text=row_text, fg='white')

                # Other label that was displayed at the right
                data_label1 = Label(Student_Data8_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label1.place(x=890, y=100)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    user_data[10], user_data[11], user_data[12], user_data[13], user_data[14], user_data[15], user_data[16], user_data[17]
                )
                data_label1.config(text=row_text, fg='white')

                # Display the subject data in the table
                for i, row_data in enumerate(subject_data, start=1):
                    for j, field_data in enumerate(row_data):
                        input_fields[i-1][j].insert(0, field_data)

            else:
                #If Year Level does not match, it will display "No data found for the logged-in user."
                data_label = Label(Student_Data8_fm, text="No data found for the logged-in user.", font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233')
                data_label.place(x=350, y=100)

        # Close the database connection
        connection.close()

    # Create the table
    table_frame = Frame(Student_Data8_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']  
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)

    # Create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data8_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    # Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    #Selecting between 1st Sem and 2nd Sem
    def view_entries(event):
        selected_option = select_sem_btn.get()

        if selected_option == '1st Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('second_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the First_Sem table
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?",(name_check,))
            first_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(first_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)

            # Close the database connection
            conn.close()

        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('second_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the Second_Sem tables
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?",(name_check,))
            second_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(second_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)


            # Close the database connections
            conn.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data8_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the view_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', view_entries)


    # Frame of its container
    Student_Data8_fm.pack(fill='both', expand=1)
    Student_Data8_fm.pack_propagate(False)
    display_student_data()

# Reporter & Coder(Conarco,Montejo)
def third_year_user():

    #Forwarding to Login1 and deleting the content of third_year_user
    def forward_to_Login1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data9_fm.destroy()
            Login1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']

    #Frame of its container
    Student_Data9_fm=Frame(Student_Data_fm, bg=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data9_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data Logo
    studentlogo_lb=Label(Student_Data9_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data9_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Login1)
    profilelogo_btn.place(x=1270,y=5)

    def display_student_data():

        global name_check
        
        # Connect to the database
        connection = sqlite3.connect(resource_path('students_account_lists.db'))
        connection1 = sqlite3.connect(resource_path('third_year.db'))

        cursor = connection.cursor()
        cursor1 = connection1.cursor()
        
        # Fetch the data for the logged-in user from the database
        cursor.execute("SELECT * FROM data WHERE Username = ?", (logged_in_user,))
        user_data = cursor.fetchone()

        name_check = user_data[2]

        if user_data:
            # Check if the Year Level matches the desired value
            desired_year_level = "3rd Year"
            if user_data[17] == desired_year_level:

                # Fetch the subject data for the logged-in user from the First_Sem table
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (user_data[2],))
                subject_data = cursor1.fetchall()

                # Create labels to display the user data
                data_label = Label(Student_Data9_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label.place(x=350, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[7], user_data[8], user_data[9]
                )
                data_label.config(text=row_text, fg='white')

                # Other label that was displayed at the right
                data_label1 = Label(Student_Data9_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label1.place(x=890, y=100)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    user_data[10], user_data[11], user_data[12], user_data[13], user_data[14], user_data[15], user_data[16], user_data[17]
                )
                data_label1.config(text=row_text, fg='white')

                # Display the subject data in the table
                for i, row_data in enumerate(subject_data, start=1):
                    for j, field_data in enumerate(row_data):
                        input_fields[i-1][j].insert(0, field_data)

            else:
                #If Year Level does not match, it will display "No data found for the logged-in user."
                data_label = Label(Student_Data9_fm, text="No data found for the logged-in user.", font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233')
                data_label.place(x=350, y=100)

        # Close the database connection
        connection.close()

    # Create the table
    table_frame = Frame(Student_Data9_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']  
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)

    # Create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data9_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    # Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    #Selecting between 1st Sem and 2nd Sem
    def view_entries(event):
        selected_option = select_sem_btn.get()

        if selected_option == '1st Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('third_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the First_Sem table
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?",(name_check,))
            first_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(first_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)

            # Close the database connection
            conn.close()

        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('third_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the Second_Sem tables
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?",(name_check,))
            second_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(second_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)


            # Close the database connections
            conn.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data9_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the view_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', view_entries)


    # Frame of its container
    Student_Data9_fm.pack(fill='both', expand=1)
    Student_Data9_fm.pack_propagate(False)
    display_student_data()

# Reporter & Coder(Roxas,Papa,Chanchan)
def fourth_year_user():

    #Forwarding to Login1 and deleting the content of fourth_year_user
    def forward_to_Login1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data10_fm.destroy()
            Login1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']

    #Frame of its container
    Student_Data10_fm=Frame(Student_Data_fm, bg=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data10_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data Logo
    studentlogo_lb=Label(Student_Data10_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data10_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Login1)
    profilelogo_btn.place(x=1270,y=5)

    def display_student_data():

        global name_check

        # Connect to the database
        connection = sqlite3.connect(resource_path('students_account_lists.db'))
        connection1 = sqlite3.connect(resource_path('fourth_year.db'))

        cursor = connection.cursor()
        cursor1 = connection1.cursor()
        
        # Fetch the data for the logged-in user from the database
        cursor.execute("SELECT * FROM data WHERE Username = ?", (logged_in_user,))
        user_data = cursor.fetchone()

        name_check = user_data[2]

        if user_data:
            # Check if the Year Level matches the desired value
            desired_year_level = "4th Year"
            if user_data[17] == desired_year_level:

                # Fetch the subject data for the logged-in user from the First_Sem table
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (user_data[2],))
                subject_data = cursor1.fetchall()

                # Create labels to display the user data
                data_label = Label(Student_Data10_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label.place(x=350, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[7], user_data[8], user_data[9]
                )
                data_label.config(text=row_text, fg='white')

                # Other label that was displayed at the right
                data_label1 = Label(Student_Data10_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233')
                data_label1.place(x=890, y=100)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    user_data[10], user_data[11], user_data[12], user_data[13], user_data[14], user_data[15], user_data[16], user_data[17]
                )
                data_label1.config(text=row_text, fg='white')

                # Display the subject data in the table
                for i, row_data in enumerate(subject_data, start=1):
                    for j, field_data in enumerate(row_data):
                        input_fields[i-1][j].insert(0, field_data)
            else:
                #If Year Level does not match, it will display "No data found for the logged-in user."
                data_label = Label(Student_Data10_fm, text="No data found for the logged-in user.", font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233')
                data_label.place(x=350, y=100)

        # Close the database connection
        connection.close()

    # Create the table
    table_frame = Frame(Student_Data10_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']  
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)

    # Create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data10_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    # Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    #Selecting between 1st Sem and 2nd Sem
    def view_entries(event):
        selected_option = select_sem_btn.get()

        if selected_option == '1st Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('fourth_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the First_Sem table
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?",(name_check,))
            first_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(first_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)

            # Close the database connection
            conn.close()

        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn = sqlite3.connect(resource_path('fourth_year.db'))
            cursor = conn.cursor()

            # Fetch the data from the Second_Sem tables
            cursor.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?",(name_check,))
            second_sem_data = cursor.fetchall()

            # Populate the table with the fetched data
            for i, row_data in enumerate(second_sem_data, start=1):
                for j, field_data in enumerate(row_data):
                    input_fields[i-1][j].insert(0, field_data)


            # Close the database connections
            conn.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data10_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the view_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', view_entries)


    # Frame of its container
    Student_Data10_fm.pack(fill='both', expand=1)
    Student_Data10_fm.pack_propagate(False)
    display_student_data()

# Reporter & Coder(Roxas,Papa,Chanchan)
def view_student_info():

    #Forwarding to Admin1 and deleting the content of view_student_info
    def forward_to_Admin1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data11_fm.destroy()
            Admin1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']

    #Frame of its container
    Student_Data11_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data11_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data
    studentlogo_lb=Label(Student_Data11_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data11_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Admin1)
    profilelogo_btn.place(x=1270,y=5)

    #Heading of Name Entry(User's Name)
    name_entry_ent = Entry(Student_Data11_fm,highlightbackground=bg_color,highlightthickness=3,bd=1,font=('Franklin Gothic Demi (Headings)',15,'bold'))
    name_entry_ent.place(x=100,y=105,width=190,height=35)

    def display_student_data(name='ADMIN'):
        # Clear any existing data labels
        for widget in Student_Data11_fm.winfo_children():
            if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                widget.destroy()

        # Clear any existing table data
        for row_fields in input_fields:
            for field in row_fields:
                field.delete(0, 'end')

        # Connect to the database
        conn = sqlite3.connect(resource_path('admin_data_lists.db'))
        conn1 = sqlite3.connect(resource_path('first_year.db'))
        conn2 = sqlite3.connect(resource_path('second_year.db'))
        conn3 = sqlite3.connect(resource_path('third_year.db'))
        conn4 = sqlite3.connect(resource_path('fourth_year.db'))

        cursor = conn.cursor()
        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()
        cursor3 = conn3.cursor()
        cursor4 = conn4.cursor()

        #Fetching the names in the 1st,2nd,3rd,4th year names
        cursor1.execute("SELECT DISTINCT Name FROM First_Sem")
        first_year_names = [row[0] for row in cursor1.fetchall()]

        cursor2.execute("SELECT DISTINCT Name FROM First_Sem")
        second_year_names = [row[0] for row in cursor2.fetchall()]

        cursor3.execute("SELECT DISTINCT Name FROM First_Sem")
        third_year_names = [row[0] for row in cursor3.fetchall()]

        cursor4.execute("SELECT DISTINCT Name FROM First_Sem")
        fourth_year_names = [row[0] for row in cursor4.fetchall()]

        # Fetch the data from the database based on the name
        if name:
            cursor.execute("SELECT * FROM data WHERE Name = ?", (name,))
        else:
            cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        
        if data:
            # Create labels to display the data
            for row in data:

                data_label = Label(Student_Data11_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233',width=40,height=8)
                data_label.place(x=320, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
                )
                data_label.config(text=row_text, fg='white')

                #Other label that was displayed at the right
                data_label1 = Label(Student_Data11_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233',width=50,height=9)
                data_label1.place(x=840, y=80)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17]
                )
                data_label1.config(text=row_text, fg='white')

            if name in first_year_names:
                # Fetch the table data from the database
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor1.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in second_year_names:
                # Fetch the table data from the database
                cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor2.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in third_year_names:
                # Fetch the table data from the database
                cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor3.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in fourth_year_names:
                # Fetch the table data from the database
                cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor4.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

        else:
            # No data found
            text=Text(Student_Data11_fm,wrap=WORD,font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233',width=91,height=8)
            text.insert(INSERT,"No data found.")
            text.place(x=350,y=100)

        # Close the database connection
        conn.close()
        conn1.close()
        conn2.close()
        conn3.close()
        conn4.close()


    # Create the table
    table_frame = Frame(Student_Data11_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)


    # create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data11_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    # Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    def search_user():
        name = name_entry_ent.get()
        display_student_data(name)
        #Reset the semester values when we click the search_btn1
        select_sem_btn.set("1st Sem")

    #Selecting between 1st Sem and 2nd Sem
    def view_entries(event):
        selected_option = select_sem_btn.get()
        name = name_entry_ent.get()  # Get the entered name

        if selected_option == '1st Sem':
            display_student_data(name)  # Display data from First_Sem
        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn1 = sqlite3.connect(resource_path('first_year.db'))
            conn2 = sqlite3.connect(resource_path('second_year.db'))
            conn3 = sqlite3.connect(resource_path('third_year.db'))
            conn4 = sqlite3.connect(resource_path('fourth_year.db'))

            cursor1 = conn1.cursor()
            cursor2 = conn2.cursor()
            cursor3 = conn3.cursor()
            cursor4 = conn4.cursor()

            # Fetch the data from the Second_Sem tables
            cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data1 = cursor1.fetchall()

            cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data2 = cursor2.fetchall()

            cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data3 = cursor3.fetchall()

            cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data4 = cursor4.fetchall()

            # Populate the table with the fetched data
            for i, row_fields in enumerate(input_fields):
                for j, field in enumerate(row_fields):
                    if i < len(second_sem_data1):
                        field.insert(0, second_sem_data1[i][j])
                    elif i < len(second_sem_data2):
                        field.insert(0, second_sem_data2[i - len(second_sem_data1)][j])
                    elif i < len(second_sem_data3) + len(second_sem_data2):
                        field.insert(0, second_sem_data3[i - len(second_sem_data1) - len(second_sem_data2)][j])
                    elif i < len(second_sem_data4) + len(second_sem_data3) + len(second_sem_data2):
                        field.insert(0, second_sem_data4[i - len(second_sem_data1) - len(second_sem_data2) - len(second_sem_data3)][j])

            # Close the database connections
            conn1.close()
            conn2.close()
            conn3.close()
            conn4.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data11_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the clear_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', view_entries)

    #Search button logo
    search_btn = Button(Student_Data11_fm, image=searchlogo, highlightthickness=3, relief=RAISED, command=search_user)
    search_btn.place(x=290,y=108,height=30)


    # Frame of its container
    Student_Data11_fm.pack(fill='both', expand=1)
    Student_Data11_fm.pack_propagate(False)
    display_student_data()

# Reporter & Coder(Potal,Guia)
def edit_student_info():

    #Forwarding to Admin1 and deleting the content of edit_student_info
    def forward_to_Admin1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data12_fm.destroy()
            Admin1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']
    new_values = ['1st Sem', '2nd Sem']

    #Frame of its container
    Student_Data12_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data12_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data Logo
    studentlogo_lb=Label(Student_Data12_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data12_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Admin1)
    profilelogo_btn.place(x=1270,y=5)

    #Heading of Name Entry(User's Name)
    name_entry1_ent = Entry(Student_Data12_fm, highlightbackground=bg_color, highlightthickness=3,bd=1,font=('Franklin Gothic Demi (Headings)',15,'bold'))
    name_entry1_ent.place(x=100,y=105,width=190,height=35)

    def display_student_data(name='ADMIN'):
        # Clear any existing data labels
        for widget in Student_Data12_fm.winfo_children():
            if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                widget.destroy()

        # Clear any existing table data
        for row_fields in input_fields:
            for field in row_fields:
                field.delete(0, 'end')

        # Connect to the database
        conn = sqlite3.connect(resource_path('admin_data_lists.db'))
        conn1 = sqlite3.connect(resource_path('first_year.db'))
        conn2 = sqlite3.connect(resource_path('second_year.db'))
        conn3 = sqlite3.connect(resource_path('third_year.db'))
        conn4 = sqlite3.connect(resource_path('fourth_year.db'))

        cursor = conn.cursor()
        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()
        cursor3 = conn3.cursor()
        cursor4 = conn4.cursor()

        #Fetching the names in the 1st,2nd,3rd,4th year names
        cursor1.execute("SELECT DISTINCT Name FROM First_Sem")
        first_year_names = [row[0] for row in cursor1.fetchall()]

        cursor2.execute("SELECT DISTINCT Name FROM First_Sem")
        second_year_names = [row[0] for row in cursor2.fetchall()]

        cursor3.execute("SELECT DISTINCT Name FROM First_Sem")
        third_year_names = [row[0] for row in cursor3.fetchall()]

        cursor4.execute("SELECT DISTINCT Name FROM First_Sem")
        fourth_year_names = [row[0] for row in cursor4.fetchall()]

        # Fetch the data from the database based on the name
        if name:
            cursor.execute("SELECT * FROM data WHERE Name = ?", (name,))
        else:
            cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        
        if data:
            # Create labels to display the data
            for row in data:

                data_label = Label(Student_Data12_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233',width=40,height=8)
                data_label.place(x=320, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
                )
                data_label.config(text=row_text, fg='white')

                #Other label that was displayed at the right
                data_label1 = Label(Student_Data12_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233',width=50,height=9)
                data_label1.place(x=840, y=80)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17]
                )
                data_label1.config(text=row_text, fg='white')

            if name in first_year_names:
                # Fetch the table data from the database
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor1.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in second_year_names:
                # Fetch the table data from the database
                cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor2.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in third_year_names:
                # Fetch the table data from the database
                cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor3.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in fourth_year_names:
                # Fetch the table data from the database
                cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor4.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

        else:
            # No data found
            text=Text(Student_Data12_fm,wrap=WORD,font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233',width=91,height=8)
            text.insert(INSERT,"No data found.")
            text.place(x=350,y=100)

        # Close the database connection
        conn.close()
        conn1.close()
        conn2.close()
        conn3.close()
        conn4.close()

       
    # Create the table
    table_frame = Frame(Student_Data12_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)

    # Create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data12_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    #Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    def search_user():
        name = name_entry1_ent.get()
        display_student_data(name)
        #Reset the semester values when we click the search_btn1
        select_sem_btn.set("1st Sem")

    #Selecting between 1st Sem and 2nd Sem
    def clear_entries(event):
        selected_option = select_sem_btn.get()
        name = name_entry1_ent.get()  # Get the entered name

        if selected_option == '1st Sem':
            display_student_data(name)  # Display data from First_Sem
        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn1 = sqlite3.connect(resource_path('first_year.db'))
            conn2 = sqlite3.connect(resource_path('second_year.db'))
            conn3 = sqlite3.connect(resource_path('third_year.db'))
            conn4 = sqlite3.connect(resource_path('fourth_year.db'))

            cursor1 = conn1.cursor()
            cursor2 = conn2.cursor()
            cursor3 = conn3.cursor()
            cursor4 = conn4.cursor()

            # Fetch the data from the Second_Sem tables
            cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data1 = cursor1.fetchall()

            cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data2 = cursor2.fetchall()

            cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data3 = cursor3.fetchall()

            cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data4 = cursor4.fetchall()

            # Populate the table with the fetched data
            for i, row_fields in enumerate(input_fields):
                for j, field in enumerate(row_fields):
                    if i < len(second_sem_data1):
                        field.insert(0, second_sem_data1[i][j])
                    elif i < len(second_sem_data2):
                        field.insert(0, second_sem_data2[i - len(second_sem_data1)][j])
                    elif i < len(second_sem_data3) + len(second_sem_data2):
                        field.insert(0, second_sem_data3[i - len(second_sem_data1) - len(second_sem_data2)][j])
                    elif i < len(second_sem_data4) + len(second_sem_data3) + len(second_sem_data2):
                        field.insert(0, second_sem_data4[i - len(second_sem_data1) - len(second_sem_data2) - len(second_sem_data3)][j])

            # Close the database connections
            conn1.close()
            conn2.close()
            conn3.close()
            conn4.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data12_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the clear_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', clear_entries)

    #Search button logo
    search1_btn = Button(Student_Data12_fm, image=searchlogo, highlightthickness=3, relief=RAISED, command=search_user)
    search1_btn.place(x=290,y=108,height=30)

    def save_table_data():
        # Connect to the database
        conn = sqlite3.connect(resource_path('admin_data_lists.db'))
        conn1 = sqlite3.connect(resource_path('first_year.db'))
        conn2 = sqlite3.connect(resource_path('second_year.db'))
        conn3 = sqlite3.connect(resource_path('third_year.db'))
        conn4 = sqlite3.connect(resource_path('fourth_year.db'))

        # Connect to the database
        cursor = conn.cursor()
        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()
        cursor3 = conn3.cursor()
        cursor4 = conn4.cursor()
        cursor5 = conn.cursor()

        # Get the name entered in the entry box
        Name = name_entry1_ent.get()

        # Get the selected semester from the combobox
        selected_semester = select_sem_btn.get()

        # Fetch all distinct values from the Year_Level column
        cursor.execute("SELECT DISTINCT Year_Level FROM data WHERE Name = ?", (Name,))
        yearlevel = [row[0] for row in cursor.fetchall()]

        if yearlevel:
            # Iterate over the input fields
            for row_fields in input_fields:
                SubjectName = row_fields[0].get()
                SubjectDescription = row_fields[1].get()
                CreditsUnits = row_fields[2].get()
                Grades = row_fields[3].get()
                Remarks = row_fields[4].get()

                # Check if all fields are filled
                if SubjectName or SubjectDescription or CreditsUnits or Grades or Remarks:

                    if selected_semester == '1st Sem':

                        if '1st Year' in yearlevel:
                            # Check if the record exists in the first_year.db database
                            cursor1.execute("""
                            SELECT * FROM First_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor1.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor1.execute("""
                                UPDATE First_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor1.execute("""
                                INSERT INTO First_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                        elif '2nd Year' in yearlevel:
                        
                            # Check if the record exists in the first_year.db database
                            cursor2.execute("""
                            SELECT * FROM First_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor2.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor2.execute("""
                                UPDATE First_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor2.execute("""
                                INSERT INTO First_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                        elif '3rd Year' in yearlevel:
                        
                            # Check if the record exists in the third_year.db database
                            cursor3.execute("""
                            SELECT * FROM First_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor3.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor3.execute("""
                                UPDATE First_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor3.execute("""
                                INSERT INTO First_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                        elif '4th Year' in yearlevel:
                        
                            # Check if the record exists in the first_year.db database
                            cursor4.execute("""
                            SELECT * FROM First_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor4.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor4.execute("""
                                UPDATE First_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor4.execute("""
                                INSERT INTO First_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                    elif selected_semester == '2nd Sem':
                        
                        if '1st Year' in yearlevel:
                            # Insert or update data in the Second_Sem table of the first_year.db database
                            cursor1.execute("""
                            SELECT * FROM Second_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor1.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor1.execute("""
                                UPDATE Second_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor1.execute("""
                                INSERT INTO Second_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                        elif '2nd Year' in yearlevel:
                            # Insert or update data in the Second_Sem table of the second_year.db database
                            cursor2.execute("""
                            SELECT * FROM Second_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor2.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor2.execute("""
                                UPDATE Second_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor2.execute("""
                                INSERT INTO Second_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                        elif '3rd Year' in yearlevel:
                            # Insert or update data in the Second_Sem table of the third_year.db database
                            cursor3.execute("""
                            SELECT * FROM Second_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor3.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor3.execute("""
                                UPDATE Second_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor3.execute("""
                                INSERT INTO Second_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))

                        elif '4th Year' in yearlevel:
                            # Insert or update data in the Second_Sem table of the fourth_year.db database
                            cursor4.execute("""
                            SELECT * FROM Second_Sem
                            WHERE SubjectName = ? AND Name = ?
                            """, (SubjectName, Name))
                            record_exists = cursor4.fetchone()

                            if record_exists:
                                # Update the existing record
                                cursor4.execute("""
                                UPDATE Second_Sem
                                SET SubjectDescription = ?, CreditsUnits = ?, Grades = ?, Remarks = ?
                                WHERE SubjectName = ? AND Name = ?
                                """, (SubjectDescription, CreditsUnits, Grades, Remarks, SubjectName, Name))
                            else:
                                # Insert a new record
                                cursor4.execute("""
                                INSERT INTO Second_Sem (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name))


        # Commit the changes and close the connections
        conn.commit()
        conn1.commit()
        conn2.commit()
        conn3.commit()
        conn4.commit()
        conn.close()
        conn1.close()
        conn2.close()
        conn3.close()
        conn4.close()

    # Do something with the data (e.g., save it to the database)
    display_student_data()  # Update the display after saving the data

    # Save button
    save_btn = Button(Student_Data12_fm, text="Save", font=('Franklin Gothic Demi (Headings)', 16, 'bold'), bg='#6aa84f', fg='white', relief=RAISED, command=save_table_data)
    save_btn.place(x=1420, y=690)

    # Frame of its container
    Student_Data12_fm.pack(fill='both', expand=1)
    Student_Data12_fm.pack_propagate(False)
    display_student_data()

# Reporter & Coder(Potal,Guia)
def print_student_info():

    #Forwarding to Admin1 and deleting the content of print_student_info
    def forward_to_Admin1():  
        ans = confirmation_box(message='Do you want to exit?')

        if ans:
            Student_Data13_fm.destroy()
            Admin1()

    #Set values in combobox
    semester_list = ['1st Sem','2nd Sem']

    #Frame of its container
    Student_Data13_fm=Frame(Student_Data_fm, background=bg_color, highlightbackground=bg_color, highlightthickness=3)

    #Heading of CKC
    heading_lb=Label(Student_Data13_fm,text='Christ the King College',image=ckc1,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',25,'bold'))
    heading_lb.pack(side=TOP)

    #Heading of Student Data Logo
    studentlogo_lb=Label(Student_Data13_fm,image=logo,compound=LEFT,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'))
    studentlogo_lb.place(x=0,y=0,height=98)

    #Heading of Home
    profilelogo_btn=Button(Student_Data13_fm,image=home,bg='#323233',fg='white',font=('Franklin Gothic Demi (Headings)',13,'bold'),bd=0,relief=RAISED,command=forward_to_Admin1)
    profilelogo_btn.place(x=1270,y=5)

    #Heading of Name Entry(User's Name)
    name_entry1_ent = Entry(Student_Data13_fm,highlightbackground=bg_color,highlightthickness=3,bd=1,font=('Franklin Gothic Demi (Headings)',15,'bold'))
    name_entry1_ent.place(x=100,y=105,width=190,height=35)

    def display_student_data(name='ADMIN'):
        # Clear any existing data labels
        for widget in Student_Data13_fm.winfo_children():
            if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                widget.destroy()

        # Clear any existing table data
        for row_fields in input_fields:
            for field in row_fields:
                field.delete(0, 'end')

        # Connect to the database
        conn = sqlite3.connect(resource_path('admin_data_lists.db'))
        conn1 = sqlite3.connect(resource_path('first_year.db'))
        conn2 = sqlite3.connect(resource_path('second_year.db'))
        conn3 = sqlite3.connect(resource_path('third_year.db'))
        conn4 = sqlite3.connect(resource_path('fourth_year.db'))

        cursor = conn.cursor()
        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()
        cursor3 = conn3.cursor()
        cursor4 = conn4.cursor()

        #Fetching the names in the 1st,2nd,3rd,4th year names
        cursor1.execute("SELECT Name FROM First_Sem")
        first_year_names = [row[0] for row in cursor1.fetchall()]

        cursor2.execute("SELECT Name FROM First_Sem")
        second_year_names = [row[0] for row in cursor2.fetchall()]

        cursor3.execute("SELECT Name FROM First_Sem")
        third_year_names = [row[0] for row in cursor3.fetchall()]

        cursor4.execute("SELECT Name FROM First_Sem")
        fourth_year_names = [row[0] for row in cursor4.fetchall()]
        
        # Fetch the data from the database based on the name
        if name:
            cursor.execute("SELECT * FROM data WHERE Name = ?", (name,))
        else:
            cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        
        if data:
            # Create labels to display the data
            for row in data:

                data_label = Label(Student_Data13_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233',width=40,height=8)
                data_label.place(x=320, y=100)

                row_text = "Name: {}\nAge: {}\nDate of Birth: {}\nAddress: {}\nContact Number: {}\nGuardian's Name: {}\nGuardian's Contact Number: {}\nElementary: {}".format(
                    row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]
                )
                data_label.config(text=row_text, fg='white')

                #Other label that was displayed at the right
                data_label1 = Label(Student_Data13_fm, font=('Franklin Gothic Demi (Headings)', 18), wraplength=800, justify='left', bg='#323233',width=50,height=9)
                data_label1.place(x=840, y=80)

                row_text = "High School: {}\nSenior High School: {}\nCollege: {}\nSemester: {}\nSubjects Name: {}\nSubjects Description: {}\nCredits Units: {}\nYear Level: {}".format(
                    row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17]
                )
                data_label1.config(text=row_text, fg='white')

            if name in first_year_names:
                # Fetch the table data from the database
                cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor1.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in second_year_names:
                # Fetch the table data from the database
                cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor2.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in third_year_names:
                # Fetch the table data from the database
                cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor3.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

            elif name in fourth_year_names:
                # Fetch the table data from the database
                cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM First_Sem WHERE Name = ?", (name,))
                table_data = cursor4.fetchall()

                # Populate the table with the fetched data
                for i, row_fields in enumerate(input_fields):
                    for j, field in enumerate(row_fields):
                        if i < len(table_data):
                            field.insert(0, table_data[i][j])

        else:
            # No data found
            text=Text(Student_Data13_fm,wrap=WORD,font=('Franklin Gothic Demi (Headings)', 18), fg='white', bg='#323233',width=91,height=8)
            text.insert(INSERT,"No data found.")
            text.place(x=350,y=100)

        # Close the database connection
        conn.close()
        conn1.close()
        conn2.close()
        conn3.close()
        conn4.close()

  
    # Create the table
    table_frame = Frame(Student_Data13_fm, bg='#323233')
    table_frame.place(x=100, y=360)

    # Create the table headers
    headers = ['Subject Name', 'Subject Description', 'Credits/Units', 'Grades', 'Remarks']
    for i, header in enumerate(headers):
        header_label = Label(table_frame, text=header, font=('Franklin Gothic Demi (Headings)', 16, 'bold'), fg='white', bg='#323233')
        header_label.grid(row=0, column=i, padx=20, pady=10)

    # Create input fields for the table
    input_fields = []
    for i in range(1, 8):
        row_fields = []
        for j in range(5):
            if j == 2 or j == 3:  # Credits/Units and Grades fields
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14), justify=CENTER)
            else:
                entry = Entry(table_frame, font=('Franklin Gothic Demi (Headings)', 14))
            entry.grid(row=i, column=j, padx=20, pady=10)
            row_fields.append(entry)
        input_fields.append(row_fields)

    # Create combobox widget for semester list
    select_sem_btn = ttk.Combobox(Student_Data13_fm,font=('Franklin Gothic Demi (Headings)', 12, 'bold'),state='readonly',values=semester_list)
    select_sem_btn.place(x=8,y=420,width=100)

    #Set the initial selection to the placeholder value
    select_sem_btn.current(0)

    def search_user():
        name = name_entry1_ent.get()
        display_student_data(name)
        #Reset the semester values when we click the search_btn1
        select_sem_btn.set("1st Sem")

    #Selecting between 1st Sem and 2nd Sem
    def clear_entries(event):
        selected_option = select_sem_btn.get()
        name = name_entry1_ent.get()  # Get the entered name

        if selected_option == '1st Sem':
            display_student_data(name)  # Display data from First_Sem
        elif selected_option == '2nd Sem':
            # Clear the input fields
            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

            # Connect to the databases
            conn1 = sqlite3.connect(resource_path('first_year.db'))
            conn2 = sqlite3.connect(resource_path('second_year.db'))
            conn3 = sqlite3.connect(resource_path('third_year.db'))
            conn4 = sqlite3.connect(resource_path('fourth_year.db'))

            cursor1 = conn1.cursor()
            cursor2 = conn2.cursor()
            cursor3 = conn3.cursor()
            cursor4 = conn4.cursor()

            # Fetch the data from the Second_Sem tables
            cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data1 = cursor1.fetchall()

            cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data2 = cursor2.fetchall()

            cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data3 = cursor3.fetchall()

            cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks FROM Second_Sem WHERE Name = ?", (name,))
            second_sem_data4 = cursor4.fetchall()

            # Populate the table with the fetched data
            for i, row_fields in enumerate(input_fields):
                for j, field in enumerate(row_fields):
                    if i < len(second_sem_data1):
                        field.insert(0, second_sem_data1[i][j])
                    elif i < len(second_sem_data2):
                        field.insert(0, second_sem_data2[i - len(second_sem_data1)][j])
                    elif i < len(second_sem_data3) + len(second_sem_data2):
                        field.insert(0, second_sem_data3[i - len(second_sem_data1) - len(second_sem_data2)][j])
                    elif i < len(second_sem_data4) + len(second_sem_data3) + len(second_sem_data2):
                        field.insert(0, second_sem_data4[i - len(second_sem_data1) - len(second_sem_data2) - len(second_sem_data3)][j])

            # Close the database connections
            conn1.close()
            conn2.close()
            conn3.close()
            conn4.close()

        else:
            # If any other option is selected, clear the displayed data and input fields
            for widget in Student_Data13_fm.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() in (350, 890):
                    widget.destroy()

            for row_fields in input_fields:
                for field in row_fields:
                    field.delete(0, 'end')

    # Bind the clear_entries function to the <<ComboboxSelected>> event
    select_sem_btn.bind('<<ComboboxSelected>>', clear_entries)

    #Search button logo
    search1_btn = Button(Student_Data13_fm, image=searchlogo, highlightthickness=3, relief=RAISED, command=search_user)
    search1_btn.place(x=290,y=108,height=30)

    def print_data(name):
        # Connect to the database
        conn = sqlite3.connect(resource_path('admin_data_lists.db'))
        conn1 = sqlite3.connect(resource_path('first_year.db'))
        conn2 = sqlite3.connect(resource_path('second_year.db'))
        conn3 = sqlite3.connect(resource_path('third_year.db'))
        conn4 = sqlite3.connect(resource_path('fourth_year.db'))

        cursor = conn.cursor()
        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()
        cursor3 = conn3.cursor()
        cursor4 = conn4.cursor()

        # Check the selected value from the combobox
        selected_option = select_sem_btn.get()

        if selected_option == "2nd Sem":
            # Fetching the data of Second_Sem from the databases
            cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM Second_Sem WHERE Name = ?", (name,))
            first_year_data_second_sem = cursor1.fetchall()
    
            cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM Second_Sem WHERE Name = ?", (name,))
            second_year_data_second_sem = cursor2.fetchall()
    
            cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM Second_Sem WHERE Name = ?", (name,))
            third_year_data_second_sem = cursor3.fetchall()
    
            cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM Second_Sem WHERE Name = ?", (name,))
            fourth_year_data_second_sem = cursor4.fetchall()

        else:
            # Fetching the data of First_Sem from the databases
            cursor1.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM First_Sem WHERE Name = ?", (name,))
            first_year_data = cursor1.fetchall()

            cursor2.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM First_Sem WHERE Name = ?", (name,))
            second_year_data = cursor2.fetchall()

            cursor3.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM First_Sem WHERE Name = ?", (name,))
            third_year_data = cursor3.fetchall()

            cursor4.execute("SELECT SubjectName, SubjectDescription, CreditsUnits, Grades, Remarks, Name FROM First_Sem WHERE Name = ?", (name,))
            fourth_year_data = cursor4.fetchall()

        # Open a file dialog to get the filename
        file_name = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '.xlsx'), ('All Files', '.*')])

        if file_name:
            # Create a new workbook and select the active worksheet
            workbook = openpyxl.Workbook()
            worksheet = workbook.active

            # Write the data to the worksheet
            if selected_option == "2nd Sem":
                if first_year_data_second_sem:
                    worksheet.title = 'First Year (Second Semester)'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in first_year_data_second_sem:
                        worksheet.append(row)

                elif second_year_data_second_sem:
                    worksheet.title = 'Second Year (Second Semester)'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in second_year_data_second_sem:
                        worksheet.append(row)

                elif third_year_data_second_sem:
                    worksheet.title = 'Third Year (Second Semester)'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in third_year_data_second_sem:
                        worksheet.append(row)

                elif fourth_year_data_second_sem:
                    worksheet.title = 'Fourth Year (Second Semester)'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in fourth_year_data_second_sem:
                        worksheet.append(row)

            else:
                if first_year_data:
                    worksheet.title = 'First Year'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in first_year_data:
                        worksheet.append(row)

                elif second_year_data:
                    worksheet.title = 'Second Year'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in second_year_data:
                        worksheet.append(row)

                elif third_year_data:
                    worksheet.title = 'Third Year'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in third_year_data:
                        worksheet.append(row)

                elif fourth_year_data:
                    worksheet.title = 'Fourth Year'
                    worksheet.append(['SubjectName', 'SubjectDescription', 'CreditsUnits', 'Grades', 'Remarks', 'Name'])
                    for row in fourth_year_data:
                        worksheet.append(row)

            # Save the workbook to the specified file
            workbook.save(file_name)

            # Open the saved file with the default Excel application
            os.startfile(file_name, 'open')

        # Close the database connections
        conn.close()
        conn1.close()
        conn2.close()
        conn3.close()
        conn4.close()

    # Button of Print
    print_btn = Button(Student_Data13_fm, text="Print", font=('Franklin Gothic Demi (Headings)', 16, 'bold'), bg='#6aa84f', fg='white', relief=RAISED, command=lambda: print_data(name_entry1_ent.get()))
    print_btn.place(x=1420, y=690, width=70)

    # Calling display_student_data and display its context
    display_student_data()  

    # Frame of its container
    Student_Data13_fm.pack(fill='both', expand=1)
    Student_Data13_fm.pack_propagate(False)




    



#Login()
#Admin()
#first_year_user()
Student_Data()
#Sign_up()
init_database()
Student_Data_fm.mainloop()