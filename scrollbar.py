# import tkinter as tk
# from tkinter import ttk
#
# root = tk.Tk()
# root.resizable(True, True)
# root.title("Scrollbar Widget Example")
#
# # apply the grid layout
# root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)
#
# # create the text widget
# text = tk.Text(root, height=10)
# text.grid(row=0, column=0, sticky=tk.EW)
#
# # create a scrollbar widget and set its command to the text widget
# scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
# scrollbar.grid(row=0, column=1, sticky=tk.NS)
#
# #  communicate back to the scrollbar
# text['yscrollcommand'] = scrollbar.set
#
# # add sample text to the text widget to show the screen
# for i in range(1,50):
#     position = f'{i}.0'
#     text.insert(position,f'Line {i}\n');
#
# root.mainloop()

from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
