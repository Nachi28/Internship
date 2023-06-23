import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()
        listbox_tasks.delete(selected_index)
    except:
        pass

root = tk.Tk()
root.title("To-Do List")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, font=("Arial", 12))
listbox_tasks.pack()

entry_task = tk.Entry(root, font=("Arial", 12))
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task, font=("Arial", 12))
button_add_task.pack(pady=10)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task, font=("Arial", 12))
button_delete_task.pack(pady=10)

root.mainloop()