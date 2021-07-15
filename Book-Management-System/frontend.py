from tkinter import *
from backend import Database

database = Database("Books.db")
selected_tuple = ()
def clear_and_display():
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def get_selected_row(event):
    global selected_tuple
    if(list1.curselection() == ()):
        s2_label_text.set("Not any books availble yet...")
    else:
        index = list1.curselection()[0] #return a tuple so we are taking only firt index
        selected_tuple = list1.get(index)
        # To diplay the entry on entrywidget as soon as user select any entry from list box
        clear_and_display()

def view_command():
    list1.delete(0,END)
    rows = database.view();
    if(rows == []):
        s2_label_text.set("Not any books availble yet...")
    else:
        s2_label_text.set("List of availble books...")
        for row in rows:
            list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row);
        
def insert_command():
    if(title_text.get()=="" or author_text.get()=="" or year_text.get()=="" or isbn_text.get() ==""):
        s2_label_text.set("Fill All The Entries First")
    else:
        database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        list1.delete(0,END)
        s2_label_text.set("Row inserted sucessfully...")
        # view_command()

def delete_command():
    # Sending id to function
    database.delete(selected_tuple[0])
    s2_label_text.set("Selected row deleted sucessfully.")
    # view_command()

def update_command():
    # Sending id to function
    database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    s2_label_text.set("Selected row updated sucessfully")
    # view_command()


window=Tk()

window.title("Book Management System")
window.resizable(0,0)
l1 = Label(window,text = "Title")
l1.grid(row=0,column = 0)

l1 = Label(window,text = "Author")
l1.grid(row=0,column = 2)

l1 = Label(window,text = "Year")
l1.grid(row=1,column = 0)

l1 = Label(window,text = "ISBN")
l1.grid(row=1,column = 2)

title_text = StringVar()
e1 = Entry(window,textvariable = title_text)
e1.grid(row = 0,column = 1)

author_text = StringVar()
e2 = Entry(window,textvariable = author_text)
e2.grid(row = 0,column = 3)

year_text = StringVar()
e3 = Entry(window,textvariable = year_text)
e3.grid(row = 1,column = 1)

isbn_text = StringVar()
e4 = Entry(window,textvariable = isbn_text)
e4.grid(row = 1,column = 3)

s1_label =Label(window,text = "Status : ")
s1_label.grid(row = 2,column = 0)

s2_label_text = StringVar()
s2_label = Label(window,textvariable = s2_label_text)
s2_label.grid(row=2,column = 1,columnspan = 2)

list1 = Listbox(window,height = 8,width = 38)
list1.grid(row=3,column=0,rowspan = 7,columnspan = 3)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=4,rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text = "View All",width = 12,command = view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text = "Search Entry",width = 12,command = search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text = "Add Entry",width = 12,command = insert_command)
b3.grid(row=4,column=3)

b4 = Button(window,text = "Update Selected",width = 12,command = update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text = "Delete Selected",width = 12,command = delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text = "Exit",width = 12,command = window.quit)
b6.grid(row=7,column=3)

window.mainloop()