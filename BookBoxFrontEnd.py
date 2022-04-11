"""
A program that stores the book information
Title, Author, ISBN.
The user can view all records, serach entery, add entry, update entry, delete entry.
"""

from tkinter import *

window = Tk()

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

