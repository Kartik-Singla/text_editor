import tkinter as tk
from tkinter import ttk,colorchooser,filedialog,messagebox
from tkinter import font
import os
main_app=tk.Tk()
main_app.geometry('1200x800')
main_app.title('TEXT EDITOR')

main_menu=tk.Menu()#---->creates a bar where menu will recide it will be invisible if menu is empty
file=tk.Menu(main_app,tearoff=False)
edit=tk.Menu(main_app,tearoff=False)
view=tk.Menu(main_app,tearoff=False)
color_theme=tk.Menu(main_app,tearoff=False)  

#   file icons 
new_icon=tk.PhotoImage(file='icons2/new.png')#--->saved the icon in variable
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

#   edit icons
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

#   view icons
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')

# color theme
light_default_icon =tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon =tk.PhotoImage(file='icons2/light_plus.png')

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon)

color_dict={
     'Light Default':('#000000','#ffffff'),
     'Light Plus':('#474747','#e0e0e0')
}

#add_cascade only adds label to menu bar doesnot perform any  command it has it keys which perfoem command
main_menu.add_cascade(label='FILE',menu=file)#--->adds 'FILE' to main_menu
main_menu.add_cascade(label='EDIT',menu=edit)
main_menu.add_cascade(label='VIEW',menu=view)
main_menu.add_cascade(label='COLOR THEME',menu=color_theme)

tool_bar=ttk.Label(main_app)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuple=tk.font.families()#---> import all the fonts from font module and assign it to font_tuple
font_family=tk.StringVar()# stores our input font
font_box=ttk.Combobox(tool_bar,width=25,textvariable=font_family,state='readonly')# specified that our storing variable is font_family
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,80))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)


#bold button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
#italic button
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
#underline button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
#font color button
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)
# align buttons
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

text_editor=tk.Text(main_app)
text_editor.config(wrap='char',relief=tk.FLAT)#--->wrap takes the word to next line if it doesnot fit to current line
text_editor.focus_set()# when we start app cursor automatically appears

scroll_bar=tk.Scrollbar(main_app)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)#EXPANDS WRITING AREA IN BOTH X NA DY DIRECTIONS
scroll_bar.config(command=text_editor.yview)#to configure scroll bar with our text editor
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functions

curr_font_family='Arial'
curr_font_size=12
curr_font_weight='normal'
curr_font_slant='roman'
curr_font_underline='normal'

def change_font(main_app):
    global curr_font_family
    curr_font_family=font_family.get()
    text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_underline,curr_font_weight,curr_font_slant))

def change_fontsize(main_app):
    global curr_font_size
    curr_font_size=size_var.get()
    text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_underline,curr_font_weight,curr_font_slant))    

font_box.bind('<<ComboboxSelected>>',change_font) 
font_size.bind('<<ComboboxSelected>>',change_fontsize)

def change_bold():
    global curr_font_weight
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        curr_font_weight='bold'
        text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_underline,curr_font_weight,curr_font_slant))
        # since curr_font_underline and curr_font_weight both are initilaised to normal write curr_font_underline before curr_font_weight so that value of weight changes
    if text_property.actual()['weight']=='bold':
        curr_font_weight='normal'
        text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_underline,curr_font_slant,curr_font_weight))    

bold_btn.configure(command=change_bold)

def change_italic():
    global curr_font_slant
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        curr_font_slant='italic'
        text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_underline,curr_font_slant,curr_font_weight))
    if text_property.actual()['slant']=='italic':
        curr_font_slant='roman'
        text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_underline,curr_font_slant,curr_font_weight))    

italic_btn.configure(command=change_italic)

def change_underline():
    global curr_font_underline
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        curr_font_underline='underline'
        text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_weight,curr_font_slant,curr_font_underline))
    if text_property.actual()['underline']==1:
        curr_font_underline='normal'
        text_editor.configure(font=(curr_font_family,curr_font_size,curr_font_weight,curr_font_slant,curr_font_underline))    

underline_btn.configure(command=change_underline)

#there are two ways to configure the button one is above other is writing the command arguement at the time of declaration of button Caution:Declare function above it

# font color functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])#foreground color....hexacode is there on index=1

font_color_btn.configure(command=change_font_color)

#align functionality 
def align_center():
    text_content=text_editor.get(1.0,'end')#to get everything written on text editor in text_content variable
    text_editor.tag_configure('center',justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)

#if the data is on left we have to centralize it then first we store data in variable then delete it from its current position then align it to center with help of variable

def align_left():
    text_content=text_editor.get(1.0,'end')#to get everything written on text editor in text_content variable
    text_editor.tag_configure('left',justify=tk.LEFT)
    text_editor.delete(1.0,'end')#TO D
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

def align_right():
    text_content=text_editor.get(1.0,'end')#to get everything written on text editor in text_content variable
    text_editor.tag_configure('right',justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial',12))

#status bar
status_bar=ttk.Label(main_app,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def changed(main_app):
    global text_changed
    if text_editor.edit_modified():#edit_modified returns true if something is modified in text editor
        text_changed = True 
        words=len(text_editor.get(1.0,'end-1c').split())#since newline is also considered as character we deleted one character from end by -1c
        characters=len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text=f'Characters:{characters}  Words:{words}')
    text_editor.edit_modified(False) #when we hit first character 220th line becomes true then it remains true so it doesn't count more so we have to make it false   
text_editor.bind('<<Modified>>',changed)        
#new file functionality
url=''
def new_file(main_app):
    global url
    url=''
    text_editor.delete(1.0,'end')#delete all the content written on editor

#open functionality   
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    # opened current working directory when 'open window' opens
    # when 'open window' opens the title of window is 'Select File'
    #file types determine the types of file user can open
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,'end')
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:            
        return
    main_app.title(os.path.basename(url))
    #change title of text editor(only base name is printed)  

# save functionality  

def save_file(event=None):
    global url
    try:
        if url:
            content=(text_editor.get(1.0,'end'))# takes all the info written on editor in this variable
            #if the file is alrady saved it means url shoul have value url=True
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)# writes the content on file
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2=text_editor.get(1.0,'end')#save all data in this variable
            url.write(content2)#writes on file
            url.close()
    except:
        return  

#save as functionality  
def save_as(event=None):
    global url
    try:
        content=(text_editor.get(1.0,'end'))# first saved the content of file
        os.remove(url)#deleted the current file named file
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        #asked to name a file
        url.write(content)# wrote in file
        url.close()
    except:
        return    

# exit functionaity

def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save your file')
            if mbox: # invoked when user selects yes
                save_file()
                main_app.destroy()

            elif mbox is False: # invoked when user selects no
                #if we had written mbox instead of mbox is False then on pressing cancel window would have been destroyed
                main_app.destroy()
        else:
            main_app.destroy()             
    except:
        return


#   keys of FILE menu
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',comman=new_file)#--->adds "New" to FILE...without tk.LEFT only icon appears
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+S',command=save_as)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=exit_func) 

# find functionality

def find_func(event=None):

    def find():
        word=text_fentry.get()
        text_editor.tag_remove('match','1.0','end')
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word=text_fentry.get()
        replace_text=text_rentry.get()
        content=text_editor.get(1.0,'end')
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,'end')
        text_editor.insert(1.0,new_content)

    find_dialogue=tk.Tk()
    find_dialogue.geometry('450x250')
    find_dialogue.title('Find')

    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)

    text_flabel=ttk.Label(find_frame,text='Find')
    text_rlabel=ttk.Label(find_frame,text='Replace')

    text_fentry=ttk.Entry(find_frame,width=30)
    text_rentry=ttk.Entry(find_frame,width=30)

    text_fbtn=ttk.Button(find_frame,text='Find',command=find)
    text_rbtn=ttk.Button(find_frame,text='Replace',command=replace)

    text_flabel.grid(row=0,column=0,padx=3,pady=3)
    text_rlabel.grid(row=0,column=1,padx=3,pady=3)

    text_fentry.grid(row=1,column=0,padx=3,pady=3)
    text_rentry.grid(row=1,column=1,padx=3,pady=3)

    text_fbtn.grid(row=2,column=0,padx=8,pady=4)
    text_rbtn.grid(row=2,column=1,padx=8,pady=4)

    find_frame.mainloop()




#   keys of EDIT menu
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+P',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Shift+X',command=lambda:text_editor.delete(1.0,'end'))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)  

#view check buttons

show_status_bar=tk.BooleanVar()
show_tool_bar=tk.BooleanVar()
show_status_bar.set(True)
show_tool_bar.set(True)

def hide_toolbar():
    global show_tool_bar
    if show_tool_bar:#if tool bar is already present
        tool_bar.pack_forget()
        show_tool_bar=False

    else:
        #if there is no tool bar and we have to show it then first we have to clear text editor then status bar then pack tool bar to top
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X) #tk.X means to fill it on left side
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar=True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False

    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True             

#   keys of VIEW menu

view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_tool_bar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=0,variable=show_status_bar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

#change background
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)


count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

main_app.config(menu=main_menu)
main_app.bind('<Control-n>',new_file)
main_app.bind('<Control-o>',open_file)
main_app.bind('<Control-s>',save_file)
main_app.bind('<Control-Shift-s>',save_as)
main_app.bind('<Control-x>',exit_func)
main_app.bind('<Control-f>',find_func)
main_app.mainloop()
 