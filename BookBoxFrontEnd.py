"""
A program that stores the book information
Title, Author, ISBN.
The user can view all records, serach entery, add entry, update entry, delete entry.
"""

import BookBoxBackEnd

window = Tk()
window.wm_title("BookBox")

def view_command():
    # This for preventing the view-all button from keeping displaying the rows when its clicked in after the first click
    list1.delete(0, END)
    for row in BookBoxBackEnd.view():
        list1.insert(END,  row)

def search_command():
    list1.delete(0, END)
    for row in BookBoxBackEnd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

# Wrraper function fir getthing the data from the back end
def add_command():
    BookBoxBackEnd.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END) # making sure the listbox is empty

    #Displaying on tthe listbox what the user enters (to verifythat data got entered
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    # we use the global variable selected_tuple that get assigned in the get_selected_row function.
    # We take only the id from that tuple
    # We pass that id to the delete function from the back end to perform the row removal
    BookBoxBackEnd.delete(selected_tuple[0])

def update_command():
    # We keep the id (selected_tuple[0]) since csn not be updated
    BookBoxBackEnd.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())




label1 = Label(window, text="title")
label1.grid(row=0, column=0)
label2 = Label(window, text="Author")
label2.grid(row=0, column=2)
label3 = Label(window, text="Year")
label3.grid(row=1, column=0)
label4 = Label(window, text="ISBN")
label4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text= StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar1 = Scrollbar(window)
scroll_bar1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=scroll_bar1.set)

# this mean when scrolling bar, only the vertical view will change
scroll_bar1.configure(command=list1.yview())


button1 = Button(window, text="View all", width=12)
button1.grid(row=2, column=3)
button2 = Button(window, text="Search book", width=12)
button2.grid(row=3, column=3)
button3 = Button(window, text="add book", width=12)
button3.grid(row=4, column=3)
button4 = Button(window, text="Update book", width=12)
button4.grid(row=5, column=3)
button5 = Button(window, text="Delete book", width=12)
button5.grid(row=6, column=3)
button6 = Button(window, text="Close", width=12)
button6.grid(row=7, column=3)


window.mainloop()

