import tkinter as tk
from tkinter import messagebox

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer")
        
        self.is_running = False
        self.time_remaining = 0

        self.label = tk.Label(self.master, text="00:00", font=("Arial", 48))
        self.label.pack(pady=20)

        self.time_entry = tk.Entry(self.master, font=("Arial", 16))
        self.time_entry.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        if not self.is_running:
            try:
                duration = int(self.time_entry.get())
                if duration <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer for the timer duration.")
                return

            self.time_remaining = duration
            self.update_timer()
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.is_running:
            self.master.after_cancel(self.timer)
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset_timer(self):
        self.stop_timer()
        self.time_remaining = 0
        self.label.config(text="00:00")
        self.time_entry.delete(0, tk.END)

    def update_timer(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.label.config(text=time_string)

        if self.time_remaining > 0:
            self.time_remaining -= 1
            self.timer = self.master.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Timer", "Time's up!")
            self.reset_timer()

# Create the GUI
window = tk.Tk()
timer = Timer(window)

window.mainloop()
