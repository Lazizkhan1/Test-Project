from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import colorchooser
import tkinter.messagebox
import subprocess

compiler = Tk()
compiler.title("Lazizkhan's IDE")
file_path = ''


def bg_color():
    color = colorchooser.askcolor()
    colorHex = color[1]
    editor.config(bg=colorHex)
    code_output.config(bg=colorHex)


def text_color():
    color = colorchooser.askcolor()
    colorHex = color[1]
    editor.config(fg=colorHex)
    code_output.config(fg=colorHex)


def set_file_path(path):
    global file_path
    file_path = path


def open_file(*args):
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        code_output.delete('1.0', END)
        set_file_path(path)


def save_as(*args):
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        file.write(code)
        set_file_path(path)


def run(*args):
    if file_path == '':
        save_prompt = Toplevel()
        text = tkinter.messagebox.showinfo("Lazizkhan's IDE", "Do you want to save the file?")
        save_as()
        run()
        text.pack(side=RIGHT)
        return

    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open ', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

# Binds
compiler.bind('<Control-r>', run)
compiler.bind('<Control-s>', save_as)
compiler.bind('<Control-o>', open_file)

# Run Bar
run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

# Options
options_bar = Menu(menu_bar, tearoff=0)
options_bar.add_command(label='Color Change', command=bg_color)
options_bar.add_command(label='Text Color', command=text_color)
menu_bar.add_cascade(label='Option', menu=options_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.configure(fg='white', bg='#363636', font='Hack')
editor.pack(fill=BOTH, expand=True)

code_output = Text(height=10)
code_output.configure(bg='#363636', fg='white', font='Hack')
code_output.pack(fill=BOTH)

compiler.mainloop()
