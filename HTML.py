def startup():
    print('''
          |-----------------------------------------------|\n
            Starting Lunar-Code Loading...\n
            V0.1.0 \n
            Starting System Checks\n
            Done
          ''')
startup()
import tkinter.font as tkfont
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename, test
from tkinter.messagebox import showerror, showinfo, showwarning
from tkinter.scrolledtext import ScrolledText
from tkhtmlview import *
from tkHyperLinkManager import HyperlinkManager
from functools import partial
import webbrowser
app=Tk()
app.title("Lunar Code")
app.geometry("1000x600")
app.iconbitmap("images/icon.ico")
#generate splashscreen
splash_label = Label(app,text="Lunar Code V0.1.0",font=16,foreground="black")
splash_label.pack()
def main(): 
    # destroy splash window
    splash_label.destroy()
app.after(2200,main)
#----------------------
editor = ScrolledText(app, font=("Tahoma 14"), wrap=None)
editor.pack(fill=BOTH, expand=1)
editor.focus()
editor.config(fg="#F8F8F2",bg="#272822")
hyperlink= HyperlinkManager(editor)
editor.insert(END,
"#Github Lunar-Code -V0.1.0",hyperlink.add(partial(webbrowser.open,"https://github.com/superpythonguy/Lunar-Code")))

menu = Menu(app)
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
cl_menu.add_command(label="Python")
cl_menu.add_command(label="HTML")
#######

# function to open files
def open_file(event=None):
    global code, file_path
    #code = editor.get(1.0, END)
    open_path = askopenfilename(filetypes=[("HTML File", "*.html")])
    file_path = open_path
    with open(open_path, "r") as file:
        code = file.read()
        editor.delete(1.0, END)
        editor.insert(1.0, code)
app.bind("<Control-o>", open_file)
######################################
# function to save files
def save_file(event=None):
    global code, file_path
    if file_path == '':
        save_path = asksaveasfilename(defaultextension = ".html", filetypes=[("HTML File", "*.html")])
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
    save_path = asksaveasfilename(defaultextension = ".html", filetypes=[("HTML File", "*.html")])
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
#########
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save as",command=save_as)
file_menu.add_command(label="Quit",command=close)
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
status_bars = ttk.Label(app,text = f"https://github.com/superpythonguy/Lunar-code \tV0.1.0\t characters: 0 words: 0")
status_bars.pack(side = BOTTOM)
# function to display count and word characters
text_change = False
def change_word(event = None):
    global text_change
    if editor.edit_modified():
        text_change = True
        word = len(editor.get(1.0, "end-1c").split())
        chararcter = len(editor.get(1.0, "end-1c").replace(" ",""))
        status_bars.config(text = f"https://github.com/superpythonguy/Lunar-code \tV0.1.0\t characters: {chararcter} words: {word}")
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
########
def erase_text():
    editor.delete("1.0",END)
app.bind("<Control-N>",erase_text)
file_menu.add_command(label="New",command=erase_text)
########
app.mainloop()
