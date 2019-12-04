# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:38:52 2019

@author: Moath
"""

# =============================================================================
# from tkinter import *
# 
# root = Tk(className = 'My first GUI')
# 
# root.mainloop()
# =============================================================================


print('--------------------')

# =============================================================================
# from tkinter import Tk
# root = Tk()
# 
# root.geometry("768x432+100+100")
# 
# root.mainloop()
# =============================================================================

print('--------------------')

from tkinter import Tk

# =============================================================================
# root = Tk()
# 
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# 
# print("Screen width: ", screen_width)
# print("Screen height: ", screen_height)
# =============================================================================

print('--------------------')

import tkinter as tk

# =============================================================================
# root = tk.Tk()
# 
# label = tk.Label(root, text = "Hello World", padx = 10, pady = 10)
# label.pack()
# 
# root.mainloop()
# =============================================================================

print('--------------------')

# =============================================================================
# root = tk.Tk()
# 
# label = tk.Label(root, text = 'hello world', font = ('times', 20, 'bold'), padx = 10, pady = 10)
# label.pack()
# root.mainloop()
# =============================================================================

print('--------------------')

from tkinter import *

# =============================================================================
# top = Tk()
# 
# top.geometry('200x100')
# 
# b1 = Button(top, text = "Simple", fg= 'red')
# b2 = Button(top, text = "New simple", fg = 'brown')
# 
# b1.pack(side = LEFT, padx = 10)
# b2.pack(side = LEFT, padx = 10)
# 
# top.mainloop()
# =============================================================================

print('--------------------')

# =============================================================================
# top = Tk()
# 
# top.geometry('400x250')
# 
# name = Label(top, text = 'name').place(x = 30, y = 50)
# email = Label(top, text = 'Email').place(x = 30, y = 90)
# password = Label(top, text = 'Password').place(x = 30, y = 130)
# 
# e1 = Entry(top).place(x = 80, y = 50)
# e1 = Entry(top).place(x = 80, y = 90)
# e1 = Entry(top).place(x = 95, y = 130)
# top.mainloop()
# =============================================================================

print('--------------------')

# =============================================================================
# def Pressed():
#     print('Hello, Press me again ')
#     
# root = Tk()
# button = Button(root, text = 'Press Me', command = Pressed)
# button.pack(pady = 40, padx = 40)
# root.mainloop()
# =============================================================================

print('--------------------')

from tkinter import messagebox

# =============================================================================
# def Pressed():
#     dialog_title = 'Please answer'
#     dialog_text = 'Do you like to travel ?'
#     answer = messagebox.askquestion(dialog_title, dialog_text)
#     
#     if answer =='yes':
#         print('I Like This ! ')
#     else:
#         print('You must have cliked the wrong button by accident. ')
#         
# root = Tk()
# button = Button(root, text = 'Press Me', command = Pressed)
# button.pack(pady = 40, padx = 40)
# root.mainloop()
# =============================================================================

print('--------------------')

# =============================================================================
# win = Tk()
# v = StringVar()
# e = Entry(win, textvariable = v)
# e.pack()
# v.set('Coding Academy')
# print(v.get())
# 
# win.mainloop()
# 
# =============================================================================

print('--------------------')

# =============================================================================
# root = Tk(className = 'My first GUI')
# svalue = StringVar()
# w = Entry(root, textvariable = svalue)
# 
# w.pack()
# 
# def act():
#     print('You entered')
#     print('%s' % svalue.get())
#     
# foo = Button(root, text = 'Press Me', command = act)
# 
# foo.pack()
# root.mainloop()
# =============================================================================

print('--------------------')

from tkinter import scrolledtext

# =============================================================================
# window = Tk()
# window.title('welcome to LikeGeeks app')
# window.geometry('350x200')
# txt = scrolledtext.ScrolledText(window, width =  40, height = 10)
# txt.grid(column = 0, row = 0)
# window.mainloop()
# =============================================================================

print('--------------------')

root = Tk()
root.title('menu_win')
def notdone():
    messagebox.showinfo('Note implemented', 'Not yet available')
top = Menu(root)
root.config(menu=top)
file = Menu(top, tearoff=0)
file.add_command(label="New...", command=notdone)
file.add_command(label='Open...', command=notdone)
file.add_separator()
file.add_command(label="Quit", command=root.destroy)
top.add_cascade(label="File", menu=file)
edit = Menu(top, tearoff=0)
edit.add_command(label='Cut', command=notdone)
edit.add_command(label="Paste", command=notdone)
top.add_cascade(label="Edit", menu=edit)
root.mainloop()

print('--------------------')

# =============================================================================
# def open_child1():
#     c = Toplevel(root)
#     c.title('Child window 1')
#     c.geometry('200x160+230+130')
#     Label(c, text = 'Child window 1').grid()
#     
# def open_child2():
#     c = Toplevel(root)
#     c.title('Child window 2')
#     c.geometry('200x160+230+130')
#     Label(c, text = 'Child window 2').grid()
#     
# root = Tk()
# root.title('Root window')
# 
# Button(root, text = 'open child window 1', command = open_child1).grid()
# Button(root, text = 'open child window 2', command = open_child2).grid()
# 
# root.mainloop()
# =============================================================================

print('--------------------')

import tkinter as tk
from tkinter import ttk

# =============================================================================
# root = tk.Tk()
# 
# combo = ttk.Combobox(root)
# combo['values'] = (1, 2, 3, 4, 5, 'Text')
# combo.current(3)
# combo.grid(column = 0, row = 0)
# 
# root.mainloop()
# =============================================================================

print('--------------------')

# =============================================================================
# colours = ['red','green','orange','white','yellow','blue']
# r = 0
# 
# for c in colours:
#     Label(text=c, relief=RIDGE, width =15).grid( row=r,column =0)
#     Entry(bg =c, relief=SUNKEN, width =10).grid( row=r,column =1)
#     r = r + 1
# 
# mainloop()
# =============================================================================

print('--------------------')

from tkinter.colorchooser import *

# =============================================================================
# def getColor():
#     color = askcolor()
#     print(color)
#     
# Button(text = 'Select Color', command = getColor).pack()
# 
# mainloop()
# =============================================================================

print('--------------------')











