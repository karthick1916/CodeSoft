import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650")
root.resizable(False, False)

# Load Images (Icons)
app_icon = tk.PhotoImage(file="img/task.png")
topImg = tk.PhotoImage(file="img/topbar.png")
docImg = tk.PhotoImage(file="img/dock.png")
noteImg = tk.PhotoImage(file="img/task.png")
delete_icon = tk.PhotoImage(file="img/delete.png")

# Set App Icon
root.iconphoto(True, app_icon)

# Set Top Bar Image
tk.Label(root, image=topImg).pack()

# Set Left Side Image
tk.Label(root, image=docImg, bg="#32405b").place(x=30, y=25)

# Set Right Side Image
tk.Label(root, image=noteImg, bg="#32405b").place(x=340, y=15)

# Heading
head = tk.Label(root, text="My Task", font="arial 25 bold", fg="white", bg="#32405b")
head.place(x=130, y=15)

# Task List Storage
tasks = []

# Update Listbox function
def update_task_listbox():
    listbox.delete(0, tk.END)  # Clear the Listbox before updating
    for task in tasks:
        task_text = f"{task['task']} - {'Pending' if not task['completed'] else 'Completed'}"
        listbox.insert(tk.END, task_text)

# Add task function
def add_task():
    task = task_var.get().strip()
    if task:
        tasks.append({"task": task, "completed": False})
        task_var.set("")  # Clear the entry
        update_task_listbox()  # Update the Listbox
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Delete task function
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]  # Get the index of the selected task
        del tasks[selected_task_index]  # Delete the task from the list
        update_task_listbox()  # Update the Listbox
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Mark task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]  # Get the index of the selected task
        tasks[selected_task_index]["completed"] = True  # Mark the task as completed
        update_task_listbox()  # Update the Listbox
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# UI Components
task_var = tk.StringVar()

# Create Frame for the Listbox and other elements
frame = tk.Frame(root, bd=3, width=350, height=280, bg="#32405b")
frame.place(x=10, y=270)

# Create Listbox widget for tasks
listbox = tk.Listbox(frame, font=("Arial", 12), width=40, height=12, bg="#32405b", fg="white", selectbackground="#5a95ff", selectmode=tk.SINGLE)
listbox.pack(fill=tk.BOTH, padx=2, pady=5)

# Entry Box Placement (Centered)
task_entry = tk.Entry(root, textvariable=task_var, font="arial 20", bd=0)
task_entry.place(relx=0.5, y=180, width=300, height=40, anchor="center")  # Center horizontally

# ADD Button Placement (Centered)
add_button = tk.Button(
    root,
    text="ADD",
    font="arial 18 bold",
    width=10,
    bg="#5a95ff",
    fg="white",
    bd=0,
    relief="flat",
    activebackground="#4a85e0",
    activeforeground="white",
    command=add_task,
)
add_button.place(relx=0.5, y=230, anchor="center")  # Center horizontally

# Action buttons (delete and complete)
delete_button = tk.Button(root, image=delete_icon, bd=0, command=delete_task)
delete_button.pack(side=tk.BOTTOM, pady=5)

complete_button = tk.Button(root, text="Complete", font="arial 14", bg="green", fg="white", bd=0, command=mark_completed)
complete_button.pack(side=tk.BOTTOM, pady=5)

# Run the Tkinter event loop
root.mainloop()
