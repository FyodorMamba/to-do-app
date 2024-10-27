import tkinter
from tkinter import *
from tkinter import messagebox

# Root setup
root = Tk()
root.title("Cipher-DO-List-App")
root.geometry("400x600+400+100")
root.resizable(False, False)

# Default theme colors
current_theme = {
    "bg": "#32405b",
    "fg": "white",
    "listbox_bg": "#32405b",
    "listbox_fg": "white",
    "button_bg": "#5a95ff",
    "button_fg": "white",
    "entry_bg": "white",
    "entry_fg": "black"
}

# Task list (with time)
task_list = []

# Function to add a new task with time
def addTask(event=None):
    task = task_entry.get()
    task_time = f"{hour_spinbox.get()}:{minute_spinbox.get()}"
    
    if task != "":
        full_task = f"{task} - [{task_time}]"
        task_list.append(full_task)
        listbox.insert(END, full_task)
        task_entry.delete(0, 'end')
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task
def deleteTask(event=None):
    try:
        selected_task_index = listbox.curselection()[0]
        task_list.pop(selected_task_index)
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Settings window to change theme
def openSettings():
    settings_window = Toplevel(root)
    settings_window.title("Settings")
    settings_window.geometry("300x200+500+200")
    settings_window.resizable(False, False)

    Label(settings_window, text="Choose Theme:", font=("Arial", 14)).pack(pady=10)

    Button(settings_window, text="Light Theme", font=("Arial", 12), command=lambda: change_theme("light")).pack(pady=5)
    Button(settings_window, text="Dark Theme", font=("Arial", 12), command=lambda: change_theme("dark")).pack(pady=5)

# Change theme based on user choice
def change_theme(theme):
    global current_theme
    if theme == "light":
        current_theme = {
            "bg": "white",
            "fg": "black",
            "listbox_bg": "white",
            "listbox_fg": "black",
            "button_bg": "#5a95ff",
            "button_fg": "white",
            "entry_bg": "white",
            "entry_fg": "black"
        }
    elif theme == "dark":
        current_theme = {
            "bg": "#32405b",
            "fg": "white",
            "listbox_bg": "#32405b",
            "listbox_fg": "white",
            "button_bg": "#5a95ff",
            "button_fg": "white",
            "entry_bg": "white",
            "entry_fg": "black"
        }
    apply_theme()

# Apply the selected theme across the UI
def apply_theme():
    root.config(bg=current_theme["bg"])
    heading.config(bg=current_theme["bg"], fg=current_theme["fg"])
    task_entry.config(bg=current_theme["entry_bg"], fg=current_theme["entry_fg"])
    listbox.config(bg=current_theme["listbox_bg"], fg=current_theme["listbox_fg"])
    add_button.config(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    delete_button.config(bg=current_theme["button_bg"], fg=current_theme["button_fg"])
    time_frame.config(bg=current_theme["bg"])
    frame.config(bg=current_theme["bg"])
    frame1.config(bg=current_theme["bg"])

# Icon setup
image_icon = PhotoImage(file="/home/fyodormamba/Downloads/code0.1/todoapp/icon/icon.png")
root.iconphoto(False, image_icon)

# Top bar
TopImage = PhotoImage(file="/home/fyodormamba/Downloads/code0.1/todoapp/icon/topbar.png")
Label(root, image=TopImage).pack()

# Settings button (dockImage as button)
dockImage = PhotoImage(file="/home/fyodormamba/Downloads/code0.1/todoapp/icon/dock.png")
settings_button = Button(root, image=dockImage, bd=0, command=openSettings, bg=current_theme["bg"])
settings_button.place(x=30, y=25)

# Task icon at top-right
noteImage = PhotoImage(file="/home/fyodormamba/Downloads/code0.1/todoapp/icon/task.png")
Label(root, image=noteImage, bg=current_theme["bg"]).place(x=340, y=30)

# Heading for the task list
heading = Label(root, text="ALL TASKS", font="arial 18 bold", fg=current_theme["fg"], bg=current_theme["bg"])
heading.place(x=130, y=20)

# Main input frame (for task and time)
frame = Frame(root, width=400, height=50, bg=current_theme["bg"])
frame.place(x=0, y=130)

task_entry = Entry(frame, width=20, font="arial 16", bd=0, bg=current_theme["entry_bg"], fg=current_theme["entry_fg"])
task_entry.place(x=10, y=10)

# Add task button
add_button = Button(frame, text="ADD", font="arial 14 bold", width=5, bg=current_theme["button_bg"], fg=current_theme["button_fg"], bd=0, command=addTask)
add_button.place(x=300, y=5)

# Time selection for task
time_frame = Frame(root, width=400, height=50, bg=current_theme["bg"])
time_frame.place(x=0, y=190)

Label(time_frame, text="Set Time: ", font="arial 12", bg=current_theme["bg"], fg=current_theme["fg"]).place(x=10, y=10)

hour_spinbox = Spinbox(time_frame, from_=0, to=23, width=3, font="arial 12", format="%02.0f")
hour_spinbox.place(x=100, y=10)

Label(time_frame, text=":", font="arial 12", bg=current_theme["bg"], fg=current_theme["fg"]).place(x=150, y=10)

minute_spinbox = Spinbox(time_frame, from_=0, to=59, width=3, font="arial 12", format="%02.0f")
minute_spinbox.place(x=170, y=10)

# Listbox for tasks
frame1 = Frame(root, bd=3, width=400, height=250, bg=current_theme["bg"])
frame1.pack(pady=(250, 0))

listbox = Listbox(frame1, font=('arial', 12), width=40, height=10, bg=current_theme["listbox_bg"], fg=current_theme["listbox_fg"], cursor="hand2", selectbackground=current_theme["button_bg"])
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Delete task button
delete_icon = PhotoImage(file="/home/fyodormamba/Downloads/code0.1/todoapp/icon/delete.png")
delete_button = Button(root, image=delete_icon, bd=0, command=deleteTask)
delete_button.pack(side=BOTTOM, pady=20)

# Key Bindings
root.bind('<Return>', addTask)  # Enter key to add task
root.bind('<Delete>', deleteTask)  # Delete key to delete task
root.bind('<BackSpace>', deleteTask)  # Backspace key to delete task

root.mainloop()
