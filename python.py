from logging import disable, log
from os import stat
from random import random
import mysql.connector
from tkinter import *
import random

window = Tk()
window.title("LOGIN")
window.geometry("550x290")
window.configure(bg="white")
mydb = mysql.connector.connect(
    host="localhost", user="root", password="vidit@OD7", database="library")
mycursor = mydb.cursor()


# contains widgets from main page
def main():
    global options
    options = Frame(content)
    options.grid(row=0, column=0, padx=100, pady=50)

    # add Books
    add_books_button = Button(
        options, text="ADD BOOKS IN STOCK", width=50, border=2, height=2, command=add_book)
    add_books_button.grid(row=0, column=0)

    # buy Membership
    Buy_membership_button = Button(
        options, text="BUY MEMBERSHIP", width=50, border=2, height=2, command=buy_membership)
    Buy_membership_button.grid(row=1, column=0)

    # revert Membership
    revert_Membership_button = Button(
        options, text="REVERT MEMBERSHIP", width=50, border=2, height=2, command=revert_membership)
    revert_Membership_button.grid(row=2, column=0)

    # member issues book from library
    issue_books_button = Button(
        options, text="ISSUE BOOKS TO MEMBER", width=50, border=2, height=2, command=issue_book)
    issue_books_button.grid(row=3, column=0)

    # Member Returns book to Library
    return_books_button = Button(
        options, text="RETURN BOOKS TO LIBRARY", width=50, border=2, height=2, command=return_book)
    return_books_button.grid(row=4, column=0)


# contains widget for add books page
def add_book():
    # clearing content of main menu
    options.grid_forget()

    # creating frame for add books page
    global add_book_frame
    add_book_frame = Frame(content, bg="white")
    add_book_frame.grid(row=0, column=0, padx=100, pady=50)

    # title text
    title_disable = Entry(add_book_frame, border=0)
    title_disable.insert(INSERT, "TITLE")
    title_disable.configure(state="disable")
    title_disable.grid(row=0, column=0)

    # title entry
    title = Entry(add_book_frame, width=40, border=2)
    title.grid(row=0, column=1)

    # author text
    author_disable = Entry(add_book_frame, border=0)
    author_disable.insert(INSERT, "AUTHOR")
    author_disable.configure(state="disable")
    author_disable.grid(row=1, column=0)

    # author entry
    author = Entry(add_book_frame, width=40, border=2)
    author.grid(row=1, column=1)

    # quantity text
    quantity_disable = Entry(add_book_frame, border=0)
    quantity_disable.insert(INSERT, "QUANTITY")
    quantity_disable.configure(state="disable")
    quantity_disable.grid(row=2, column=0)

    # quantity entry
    quantity = Entry(add_book_frame, width=40, border=2)
    quantity.grid(row=2, column=1)

    # submit all the data to db
    submit = Button(add_book_frame, text="SUBMIT", command=lambda: add_book_submit(
        str(title.get()), str(author.get()), quantity.get()))
    submit.grid(row=3, column=1, pady=20)

    # go back to mainmenu
    back = Button(add_book_frame, text="BACK", command=lambda: back2menu(2))
    back.grid(row=3, column=0)


# contains widget for commiting changes to db from add books section
def add_book_submit(title, author, quantity):
    # condition to check if any of the entrys are blank ; this gives error in db
    if title == "" or author == "" or quantity == "":
        empty = Entry(add_book_frame, width=50)
        empty.insert(INSERT, "EMPTY NOT ALLOWED")
        empty.configure(state="disable")
        empty.grid(row=4, column=0, columnspan=2)
    else:
        # generate random bookid , ececute the sql insert query and commit
        BOOK_ID = random.randint(0, 100000)
        mycursor.execute(
            f"INSERT INTO `library`.`books` (`BOOK_ID`, `BOOK_NAME`, `AUTHOR`, `QUANTITY`) VALUES('{BOOK_ID}', '{title}', '{author}', '{quantity}')")
        mydb.commit()


# contains widgets for buying membership
def buy_membership():
    options.grid_forget()

    # buy membership frame ; will contain all widgets
    global buy_membership_frame
    buy_membership_frame = Frame(content, bg="white")
    buy_membership_frame.grid(row=0, column=0, padx=100, pady=50)

    # full name handel
    full_name_disable = Entry(buy_membership_frame, border=0)
    full_name_disable.insert(INSERT, "FULL NAME")
    full_name_disable.configure(state="disable")
    full_name_disable.grid(row=0, column=0)

    # full name entry
    full_name = Entry(buy_membership_frame, width=40, border=2)
    full_name.grid(row=0, column=1)

    # phone number handel
    phone_disable = Entry(buy_membership_frame, border=0)
    phone_disable.insert(INSERT, "PHONE NO")
    phone_disable.configure(state="disable")
    phone_disable.grid(row=1, column=0)

    # phone number entry
    phone = Entry(buy_membership_frame, width=40, border=2)
    phone.grid(row=1, column=1)

    # email handel
    email_disable = Entry(buy_membership_frame, border=0)
    email_disable.insert(INSERT, "EMAIL")
    email_disable.configure(state="disable")
    email_disable.grid(row=2, column=0)

    # email entry
    email = Entry(buy_membership_frame, width=40, border=2)
    email.grid(row=2, column=1)

    # address handel
    address_disable = Entry(buy_membership_frame, border=0)
    address_disable.insert(INSERT, "ADDRESS")
    address_disable.configure(state="disable")
    address_disable.grid(row=3, column=0)

    # address text box
    address = Text(buy_membership_frame, width=30, height=5, border=2)
    address.grid(row=3, column=1, rowspan=5)

    # submit button
    submit = Button(buy_membership_frame, text="submit",
                    command=lambda: buy_membership_submit(full_name.get(), phone.get(), email.get(), address.get(1.0, "end-1c")))
    submit.grid(row=8, column=1, pady=20)

    # back to menu button
    backed = Button(buy_membership_frame, text="back",
                    command=lambda: back2menu(3))
    backed.grid(row=8, column=0)


# contains widgets for commiting changes to db from buy membership section
def buy_membership_submit(name, phone, email, address):
    # checking if any of the fields were left blank or not
    if name == "" or phone == "" or email == "" or address == "":
        empty = Entry(buy_membership_frame, width=50)
        empty.insert(INSERT, "EMPTY NOT ALLOWED")
        empty.configure(state="disable")
        empty.grid(row=9, column=0, columnspan=2)
    else:
        # if no entry blank; generate random id ; and save all data in db ; then commit
        member_id = random.randint(0, 1000000)
        print(member_id, str(name), phone, str(email), str(address))
        mycursor.execute(
            f"INSERT INTO `library`.`members` (`MEMBER_ID`, `MEMBER_NAME`, `RESIDENTIAL_ADDRESS`, `PHONE_NO`, `EMAIL_ADDRESS`) VALUES ('{member_id}', '{name}', '{address}', '{phone}', '{email}');")
        mydb.commit()


# contains widget for reverting membership
def revert_membership():
    options.grid_forget()
    # Revert membership frame , all widgets will be inside this frame
    global revert_membership_frame
    revert_membership_frame = Frame(content, bg="white")
    revert_membership_frame.grid(row=0, column=0, padx=100, pady=50)

    # member id handel
    member_id_disable = Entry(revert_membership_frame, border=0)
    member_id_disable.insert(INSERT, "MEMBER ID")
    member_id_disable.configure(state="disable")
    member_id_disable.grid(row=0, column=0)

    # member id entry
    member_id = Entry(revert_membership_frame, width=40, border=2)
    member_id.grid(row=0, column=1)

    # confirm member id handel
    member_id_disable = Entry(revert_membership_frame, border=0)
    member_id_disable.insert(INSERT, "CONFIRM MEMBER ID")
    member_id_disable.configure(state="disable")
    member_id_disable.grid(row=1, column=0)

    # confirm member entry
    confirm_member_id = Entry(revert_membership_frame, width=40, border=2)
    confirm_member_id.grid(row=1, column=1)

    # submit button
    submit = Button(revert_membership_frame, text="Submit",
                    command=lambda: revert_membership_submit(member_id.get(), confirm_member_id.get()))
    submit.grid(row=2, column=1)

    # back to menu button
    back = Button(revert_membership_frame, text="BACK",
                  command=lambda: back2menu(4))
    back.grid(row=2, column=0)


# contains widgets for commiting changes to db from buy revert membership section
def revert_membership_submit(ID, confirm_id):
    # checking for blank entries
    if ID == "" or confirm_id == "":
        empty = Entry(revert_membership_frame, width=50)
        empty.insert(INSERT, "EMPTY NOT ALLOWED")
        empty.configure(state="disable")
        empty.grid(row=4, column=0, columnspan=2)
    else:
        # checking if member id and conformation id are matching or not
        if ID != confirm_id:
            empty = Entry(revert_membership_frame, width=50)
            empty.insert(INSERT, "MEMBER ID AND CONFORMATION ID NOT MATCHING ")
            empty.configure(state="disable")
            empty.grid(row=4, column=0, columnspan=2)
        else:
            mycursor.execute(
                f"DELETE FROM `library`.`members` WHERE (`MEMBER_ID` = '{ID}');")
            mydb.commit()


# contains widgets fro issue book section
def issue_book():
    options.grid_forget()
    # creating global issue book frame
    global issue_book_frame
    issue_book_frame = Frame(content, bg="white")
    issue_book_frame.grid(row=0, column=0, padx=100, pady=50)

    # book id handel
    book_id_disable = Entry(issue_book_frame, border=0)
    book_id_disable.insert(INSERT, "BOOK ID")
    book_id_disable.configure(state="disable")
    book_id_disable.grid(row=0, column=0)
    # book id entry
    book_id = Entry(issue_book_frame, border=2, width=40)
    book_id.grid(row=0, column=1)
    # member id handel
    member_id_disable = Entry(issue_book_frame, border=0)
    member_id_disable.insert(INSERT, "MEMBER ID")
    member_id_disable.configure(state="disable")
    member_id_disable.grid(row=1, column=0)
    # member id entry
    member_id = Entry(issue_book_frame, width=40, border=2)
    member_id.grid(row=1, column=1)
    # date handel
    date_disable = Entry(issue_book_frame, border=0)
    date_disable.insert(INSERT, "ISSUE DATE")
    date_disable.configure(state="disable")
    date_disable.grid(row=2, column=0)
    # date label
    date = Entry(issue_book_frame, border=2, width=40)
    date.grid(row=2, column=1)

    # submit button
    submit = Button(issue_book_frame, text="Submit",
                    command=lambda: issue_book_submit(book_id.get(), member_id.get(), logged_user, date.get()))
    submit.grid(row=3, column=1)

    # back to menu button
    back = Button(issue_book_frame, text="BACK", command=lambda: back2menu(5))
    back.grid(row=3, column=0)


# contains widgets for commiting changes to db from issue book section
def issue_book_submit(book_id, member_id, employee_id, date):
    # if and of the entry widget is blank ;
    if book_id == "" or member_id == "" or employee_id == "" or date == "":
        empty = Entry(issue_book_frame, width=50)
        empty.insert(INSERT, "EMPTY NOT ALLOWED")
        empty.configure(state="disable")
        empty.grid(row=4, column=0, columnspan=2)
    # all of the entrys has some content in it
    else:
        # checks if the book id entered in the entry exists in db
        try:
            mycursor.execute(
                f"""select QUANTITY
                    from books
                    where BOOK_ID={book_id}""")
            for i in mycursor:
                quantitys = i
            quantity = quantitys[0]
            # now the book does exist ; but this check if it is in stock
            if quantity > 0:
                # book exist
                # there is atleast one left in stock as well
                # now this checks if correct member id is mentioned
                try:
                    mycursor.execute(
                        f"""select MEMBER_ID
                            from members
                            where MEMBER_ID={member_id}""")
                    for i in mycursor:
                        members = i
                    # decreasing total number of books in stock by 1; coz the book is issued
                    quantity = quantity-1
                    mycursor.execute(f"""UPDATE `library`.`books` SET `QUANTITY` = '{quantity}'
                                        WHERE (`BOOK_ID` = '{book_id}');""")
                    mydb.commit()
                    # checks for correct date format;
                    try:
                        issue_no = random.randint(0, 1000000)
                        mycursor.execute(
                            f"INSERT INTO `library`.`issued_book` (`ISSUE_NO`, `ISSUED_DATE`, `BOOK_ID`, `MEMBER_ID`, `EMPLOYEE_ID`) VALUES('{issue_no}', '{date}', '{book_id}', '{member_id}', '{employee_id}')")
                        mydb.commit()

                        empty = Entry(issue_book_frame, width=60)
                        empty.insert(
                            INSERT, f"BOOK ISSUED SUCCESSFULLY, ISSUE NO:{issue_no}")
                        empty.configure(state="disable")
                        empty.grid(row=4, column=0, columnspan=2, pady=100)
                    # incorrect date formate
                    except:
                        empty = Entry(issue_book_frame, width=60)
                        empty.insert(
                            INSERT, "INCORRECT DATE FORMAT ; USE YYYY-MM-DD FORMAT")
                        empty.configure(state="disable")
                        empty.grid(row=4, column=0, columnspan=2, pady=100)
                # incorrect member id is written
                except:
                    empty = Entry(issue_book_frame, width=60)
                    empty.insert(INSERT, "NO MEMBER WITH THIS ID FOUND")
                    empty.configure(state="disable")
                    empty.grid(row=4, column=0, columnspan=2, pady=100)
            # it means all of this book are already issued by someone else
            else:
                empty = Entry(issue_book_frame, width=60)
                empty.insert(INSERT, "THE BOOK IS OUT OF STOCK")
                empty.configure(state="disable")
                empty.grid(row=4, column=0, columnspan=2, pady=100)
        # alerts if book id does not exist in our system ; i.e incorrect
        except:
            empty = Entry(issue_book_frame, width=60)
            empty.insert(INSERT, "NO BOOK WITH THIS ID FOUND")
            empty.configure(state="disable")
            empty.grid(row=4, column=0, columnspan=2, pady=100)


# contains widgets for return book section
def return_book():
    pass


# function to return to main page
def back2menu(num):
    # enter main menu from login page
    if num == 1:
        login_frame.grid_forget()
    # enter menu page from add books pageS
    elif num == 2:
        add_book_frame.grid_forget()
    # enter menue page from buy membership page
    elif num == 3:
        buy_membership_frame.grid_forget()
    elif num == 4:
        revert_membership_frame.grid_forget()
    elif num == 5:
        issue_book_frame.grid_forget()
    main()


# password and id check function
def login_check():
    # initial both value no, get value from widgets , if value matche in db ,both converted to yes and redirection to menu
    both = "no"
    # getting values
    login_check = login_display.get()
    password_check = password_display.get()
    # checking with db
    if login_check == "" or password_check == "":
        return print("empty not allowed")
    mycursor.execute(f"""SELECT *
                    from administration
                    where EMPLOYEE_ID={login_check} and PASSWORD={password_check}""")
    for i in mycursor:
        if (str(i[1]) == login_check and str(i[0]) == password_check):
            both = "yes"
    # actions if both are correct /wrong
    if both == "yes":
        global logged_user
        logged_user = login_check
        back2menu(1)
    else:
        empty = Entry(login_frame, width=60)
        empty.insert(INSERT, "INCORRECT LOGIN ID/PASSWORD PLEASE CHECK AGAIN")
        empty.configure(state="disable")
        empty.grid(row=3, column=0, columnspan=3, pady=100)


# placing login widgets
def login():
    login_frame.grid(row=1, column=0)
    login_text.grid(row=0, column=0)
    login_display.grid(row=0, column=1, columnspan=2)
    PASSWORD_text.grid(row=1, column=0)
    password_display.grid(row=1, column=1, columnspan=2)
    done.grid(row=2, column=0, columnspan=3)


content = Frame(window, bg="white")
content.pack()
# frame where we will add login id and password
global login_frame
login_frame = Frame(content, bg="white", padx=100, pady=100)


# text input for login input
login_text = Entry(login_frame, border=0)
login_text.insert(INSERT, "LOGIN ID   ")
login_text.configure(state="disable")
login_display = Entry(login_frame, width=40, border=2)


# text input for password
PASSWORD_text = Entry(login_frame, border=0)
PASSWORD_text.insert(INSERT, "PASSWORD")
PASSWORD_text.configure(state="disable")
password_display = Entry(login_frame, width=40, border=2)


# submit button
done = Button(login_frame, text="submit", command=login_check, width=10)
login()

window.mainloop()
