import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application=tk.Tk()
main_application.geometry('1200x800')
main_application.title("Text Editor")


#---------------------------------------------------------------------------------------------------------------------------

#                                              MAIN MENU
main_menu=tk.Menu()

# ----------------- FILE -----------------
new_icon=tk.PhotoImage(file='D:\icons2\\new.png')
save_icon=tk.PhotoImage(file="D:\icons2\\save.png")
saveas_icon=tk.PhotoImage(file="D:\icons2\\save_as.png")
open_icon=tk.PhotoImage(file="D:\icons2\\open.png")
exit_icon=tk.PhotoImage(file="D:\icons2\\exit.png")

file=tk.Menu(main_menu,tearoff=False)

#----------------- EDIT --------------------
copy_icon=tk.PhotoImage(file='D:\icons2\\copy.png')
cut_icon=tk.PhotoImage(file="D:\icons2\\cut.png")
paste_icon=tk.PhotoImage(file="D:\icons2\\paste.png")
clear_all_icon=tk.PhotoImage(file="D:\icons2\\clear_all.png")
find_icon=tk.PhotoImage(file="D:\icons2\\find.png")


edit=tk.Menu(main_menu,tearoff=False)

#--------------- VIEW -------------------
view=tk.Menu(main_menu,tearoff=False)

#------------------- COLOR THEME --------------

light_default_icon=tk.PhotoImage(file="D:\icons2\\light_default.png")
light_plus_icon=tk.PhotoImage(file="D:\icons2\\light_plus.png")
dark_icon=tk.PhotoImage(file="D:\icons2\\dark.png")
red_icon=tk.PhotoImage(file="D:\icons2\\red.png")
monokai_icon=tk.PhotoImage(file="D:\icons2\\monokai.png")
night_blue_icon=tk.PhotoImage(file="D:\icons2\\night_blue.png")

color_theme=tk.Menu(main_menu,tearoff=False)

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)

color_dict={
    'Light Default':('#000000','#ffffff'),
    'light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')          
}

# CASCADE
main_menu.add_cascade(label="File",menu=file)
main_menu.add_cascade(label="Edit",menu=edit)
main_menu.add_cascade(label="View",menu=view)
main_menu.add_cascade(label="Color Theme",menu=color_theme)


#                                               END MAIN MENU
#--------------------------------------------------------------------------------------------------------------------------

#                                                   TOOL BAR

#  FONT BOX

tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)


font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0,column=0,padx=5)
  
#    SIZE BOX

size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state="readonly")
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

#  BOLD BUTTON              
bold_iconn=tk.PhotoImage(file='D:\icons2\\bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_iconn)
bold_btn.grid(row=0,column=2,padx=5)

# ITALLIC BUTTON
itallic_icon=tk.PhotoImage(file='D:\icons2\\italic.png')
itallic_btn=ttk.Button(tool_bar,image=itallic_icon)
itallic_btn.grid(row=0,column=3,padx=5)

# UNDERLINE BUTTON
underline_icon=tk.PhotoImage(file='D:\icons2\\underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

#  FONT COLOR BUTTON
font_color_icon=tk.PhotoImage(file="D:\icons2\\font_color.png")
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#  ALLIGNMENT BUTTON
left_allignment_icon=tk.PhotoImage(file="D:\icons2\\align_left.png")
left_allignment_btn=ttk.Button(tool_bar,image=left_allignment_icon)
left_allignment_btn.grid(row=0,column=6,padx=5)

center_allignment_icon=tk.PhotoImage(file="D:\icons2\\align_center.png")
center_allignment_btn=ttk.Button(tool_bar,image=center_allignment_icon)
center_allignment_btn.grid(row=0,column=7,padx=5)

right_allignment_icon=tk.PhotoImage(file="D:\icons2\\align_right.png")
right_allignment_btn=ttk.Button(tool_bar,image=right_allignment_icon)
right_allignment_btn.grid(row=0,column=8,padx=5)

#                                                  END TOOL BAR

#--------------------------------------------------------------------------------------------------------------------------

#                                               TEXT EDITOR

text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scrool_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scrool_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scrool_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrool_bar.set)




#  FONT FAMILY AND FONT SIZE FUNCTIONALLITY

current_font_family="Arial"
current_font_size=12
def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))


font_box.bind("<<ComboboxSelected>>",change_font)

def change_size(main_application):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_size.bind("<<ComboboxSelected>>",change_size)  



#  BUTTONS FUNCTIONALITY


# BOLD
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
        
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
bold_btn.configure(command=change_bold)


# ITALIC
def change_itallic():
    text_prop=tk.font.Font(font=text_editor['font'])
    if text_prop.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_prop.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
itallic_btn.configure(command=change_itallic)


# UNDERLINE
def change_under_line():
        text_prop=tk.font.Font(font=text_editor['font'])
        if text_prop.actual()['underline']==0:
            text_editor.configure(font=(current_font_family,current_font_size,'underline'))
        if text_prop.actual()['underline']==1:
            text_editor.configure(font=(current_font_family,current_font_size,'normal'))
underline_btn.configure(command=change_under_line)


# COLOR CHOOSER
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)


#  ALLIGNMENT
def align_left():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content,'left')

left_allignment_btn.configure(command=align_left)



def align_center():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('center', tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

center_allignment_btn.config(command=align_center)


def align_right():
    text_content=text_editor.get(1.0, 'end')
    text_editor.tag_config('right', tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

center_allignment_btn.config(command=align_right)




text_editor.configure(font=('Arial',12))




#                                              END TEXT EDITOR

#---------------------------------------------------------------------------------------------------------------------------

#                                                  MAIN STATUS BAR

status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)


text_changed=False
#  FUNCTIONALITY FOR STATUS BAR
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0, 'end-1c').split())
        characters=len(text_editor.get(1.0, 'end-1c').replace(" ",""))
        status_bar.config(text=f"Characters : {characters} wordss : {words}")
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)


#                                             END MAIN STATUS BAR


#--------------------------------------------------------------------------------------------------------------------------
#                                            MAIN MENU FUNCTIONALITY

#  VARIABLE NEW FUNCTIONALITY 
url=''

def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0, tk.END)


# OPEN FUNCTIONALITY
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File', filetypes=(('text file','*.txt'),('All Files',"*.*")))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except:
        return
    main_application.title(os.path.basename(url))




#  SAVE FILE FUNCTIONALITY
def save_file(event= None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w' , encoding='utf-8') as fw:
               fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode= 'w', defaultextension='.txt' ,filetypes=(('text file','*.txt'),('All Files',"*.*")))
            content2= text_editor.get(1.0 , tk.END)
            url.write(content)
    except:
        return


#  SAVE AS FUNCTIONALITY

def save_as(event=None):
    global url
    try:
        content=text_editor.get(1.0, tk.END)
        url=filedialog.asksaveasfile(mode= 'w', defaultextension='.txt' ,filetypes=(('text file','*.txt'),('All Files',"*.*")))
        url.write(content)
        url.close()
    except:
        return


# EXIT FUNCTIONALITY
# def exit
# -------------- FILE COMMANDS ----------------

file.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator='ctrl+N',command=new_file)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='ctrl+S' , command=save_file)
file.add_command(label='Save As',image=saveas_icon,compound=tk.LEFT,accelerator='ctrl+Shift+S',command=save_as)
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='ctrl+O', command=open_file)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='alt+F4')


# --------------- EDIT COMMANDS ------------------

edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='ctrl+C')
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='ctrl+X')
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='ctrl+V')
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='ctrl+alt+X')
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='ctrl+F')


# -----------------VIEW CHECK BUTTON -------------------

view.add_checkbutton(label="Tool Bar")
view.add_checkbutton(label='Status Bar')



# --------------------COLOR THEME ----------------------

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT)
    count+=1

    
    
    
#                                          END MAIN MENU FUNCTIONALLITY

#---------------------------------------------------------------------------------------------------------------------------

main_application.config(menu=main_menu)
main_application.mainloop()


