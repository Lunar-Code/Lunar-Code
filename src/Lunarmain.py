def startup():
    print('''
          |-----------------------------------------------|\n
            Starting Lunar-Code Loading...\n
            V1.1.0 \n
            Starting System Checks\n
            Done
          ''')
startup()
import platform
import re
import tkinter.font as tkfont
import webbrowser
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename, test
from tkinter.font import Font
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.scrolledtext import ScrolledText

import idlelib.colorizer as ic
import idlelib.percolator as ip
from suggestion import Suggestion
from tkhtmlview import *

from linenum import TextPeer
from tkHyperLinkManager import HyperlinkManager

DATASET = "pyauto.txt"
app=Tk()
app.title("Lunar Code")
app.geometry("1100x650")
app.iconbitmap("icon.ico")
#generate splashscreen
splash_label = Label(app,text="Lunar Code V1.1.0",font=16,foreground="black")
splash_label.pack()
def main(): 
    # destroy splash window
    splash_label.destroy()
app.after(2200,main)
#----------------------
editor = Text(app,wrap = None,undo = True)
editor.focus()
editor.config(fg="#F8F8F2",bg="#272822",insertbackground='grey')
editor.config(font=("Tahoma 14"))
hyperlink= HyperlinkManager(editor)
editor.insert(END,
"#Github Lunar-Code -V1.1.0",hyperlink.add(partial(webbrowser.open,"https://github.com/Lunar-Code/Lunar-Code")))
def pyversion():
    python = (platform.python_version())
    showinfo(r"Python Version",python)


def htmlm():
    import HTML
    
menu = Menu(app,background="red", fg="white")
app.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
edit_menu = Menu(menu, tearoff=0)
view_menu = Menu(menu, tearoff=0)
theme_menu = Menu(menu, tearoff=0)
other_menu = Menu(menu, tearoff=0)
test_menu = Menu(menu, tearoff=0)
cl_menu = Menu(menu,tearoff=0)

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit", menu=edit_menu)
menu.add_cascade(label ="View", menu=view_menu)
menu.add_cascade(label ="Theme", menu=theme_menu)
menu.add_cascade(label="Other",menu=other_menu)
menu.add_cascade(label="Languages",menu=test_menu)
test_menu.add_cascade(label="Languages",menu=cl_menu)
test_menu.add_command(label="undo",command=editor.edit_undo)
cl_menu.add_command(label="Javascript")
cl_menu.add_command(label="HTML",command=htmlm)
#######
# function to open files
def open_file(event=None):
    global code, file_path,open_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("", "*")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
        app.title("Editing " + open_path)
app.bind("<Control-o>", open_file)
######################################
# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
        file_path =save_path
    else:
        save_path = file_path
    with open(save_path, "w") as file:
        code = editor.get(2.0, END)
        file.write(code) 
app.bind("<Control-s>", save_file)
#####################################
# function to save files as specific name 
def save_as(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    save_path = asksaveasfilename(defaultextension = ".py", filetypes=[("Python File", "*.py")])
    file_path = save_path
    with open(save_path, "w") as file:
        code = editor.get(1.0, END)
        file.write(code) 
app.bind("<Control-S>", save_as)
########
font = tkfont.Font(font=editor['font'])  # get font associated with Text widget
tab_width = font.measure(' ' * 4)  # compute desired width of tabs
editor.config(tabs=(tab_width,))
########

def monkai():
    editor.config(fg="#F8F8F2",bg="#272822")
    
def light():
    editor.config(fg="black",bg="white")
    
def dark():
    editor.config(fg="white",bg="black")
    
def light_blue():
    editor.config(fg="white",bg="#3F425D")
    
def off_white():
    editor.config(fg="black",bg="#D6E5E4")
   
theme_menu.add_command(label="Monkai(default)",command=monkai)
theme_menu.add_command(label="Light",command=light)
theme_menu.add_command(label="Dark",command=dark)
theme_menu.add_command(label="Light Blue",command=light_blue)
theme_menu.add_command(label="Off white",command=off_white)
########
# function to close IDE window
def close(event=None):
    showwarning("Exit","Make sure you saved your work!")
    app.destroy()
app.bind("<Control-q>", close)
# define function to cut 
# the selected text
########

def running(event=None):
    global code    
    code = editor.get(1.0, END)
    showinfo("check terminal","Python file Ran in the terminal")
    exec(code)
app.bind("<Control-r>", running)
menu.add_command(label="Run",command=running)
#########
def erase_text():
    editor.delete("1.0",END)
app.bind("<Control-N>",erase_text)
#########
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="New",command=erase_text)
file_menu.add_command(label="Quit",command=close)
#########
def about():
    import About
def help():
    import Help
# function to display and hide status bar
show_status_bar = BooleanVar()
show_status_bar.set(True)
def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar = False 
    else :
        status_bars.pack(side=BOTTOM)
        show_status_bar = True
        
view_menu.add_checkbutton(label = "Status Bar" , onvalue = True, offvalue = 0,variable = show_status_bar , command = hide_statusbar)
# create a label for status bar
status_bars = ttk.Label(app,text = f"https://github.com/Lunar-Code/Lunar-Code \tV1.1.0\t characters: 0 words: 0")
status_bars.pack(side = BOTTOM)
# function to display count and word characters
text_change = False
def change_word(event = None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text = f"https://github.com/Lunar-Code/Lunar-Code \tV1.1.0\t characters: {chararcter} words: {word}")
    editor.edit_modified(False)
# define function to cut 
# the selected text
def cut_text(event=None):
        editor.event_generate(("<<Cut>>"))
# define function to copy 
# the selected text
def copy_text(event=None):
        editor.event_generate(("<<Copy>>"))
# define function to paste 
# the previously copied text
def paste_text(event=None):
        editor.event_generate(("<<Paste>>"))
editor.bind("<<Modified>>",change_word)
edit_menu.add_command(label="Cut", command=cut_text) 
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

other_menu.add_command(label="About",command=about)
other_menu.add_command(label="Help",command=help)
other_menu.add_command(label="Python version",command=pyversion)
#########
def autoindent(event):
    # the text widget that received the event
    widget = event.widget

    # get current line
    line = widget.get("insert linestart", "insert lineend")

    # compute the indentation of the current line
    match = re.match(r'^(\s+)', line)
    current_indent = len(match.group(0)) if match else 0

    # compute the new indentation
    new_indent = current_indent + 4

    # insert the character that triggered the event,
    # a newline, and then new indentation
    widget.insert("insert", event.char + "\n" + " "*new_indent)

    # return 'break' to prevent the default behavior
    return "break"

editor.bind(":", autoindent)
########
def example():
    print("Hello World!\ni am a example program from Lunar-code")
other_menu.add_command(label="Example code",command=example)
########
def ppi():
    showinfo("Check terminal","check terminal")
    import PPI
other_menu.add_command(label="PPI",command=ppi)
     
cdg = ic.ColorDelegator()
cdg.prog = re.compile(r'\b(?P<MYGROUP>tkinter)\b|' + ic.make_pat().pattern, re.S)
cdg.idprog = re.compile(r'\s+(\w+)', re.S)

cdg.tagdefs['MYGROUP'] = {'foreground': 'blue', 'background': 'transparent'}

cdg.tagdefs['COMMENT'] = {'foreground': 'green', 'background': 'transparent'}
cdg.tagdefs['KEYWORD'] = {'foreground': '#EF1DD3', 'background': 'transparent'}
cdg.tagdefs['BUILTIN'] = {'foreground': '#0B1FF0', 'background': 'transparent'}
cdg.tagdefs['STRING'] = {'foreground': '#F40307', 'background': 'transparent'}
cdg.tagdefs['DEFINITION'] = {'foreground': '#E0D81B', 'background': 'transparent'}
ip.Percolator(editor).insertfilter(cdg)
suggestion = Suggestion(editor, dataset=DATASET)

map_font = Font(family="Courier", size=3)
minimap = TextPeer(editor, font=map_font, state="disabled",
                   background="#272822", foreground="white")
minimap.pack(side="right", fill="y")
editor.pack(side="left", fill="both", expand=True)

if __name__ == "__main__":
    import time

    from pypresence import Presence

    client_id = "975823272182677554"  # Enter your Application ID here.
    RPC = Presence(client_id=client_id)
    RPC.connect()

    # Make sure you are using the same name that you used when uploading the image
    RPC.update(large_image="moon", large_text="Lunar Code is a code editor made in python!",
            small_image="python2", small_text="Python editor",
            state="Editing...",
            details="Download Lunar-Code Now")
    app.mainloop()
    while 1:
        time.sleep(15) #Can only update presence every 15 seconds
