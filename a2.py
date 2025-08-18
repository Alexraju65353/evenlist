import tkinter as tk
import time
def update_time_date():
    current_time = time.strftime('%H:%M:%S')       
    current_date = time.strftime('%A, %d %B %Y')    
    label_time.config(text=current_time)
    label_date.config(text=current_date)
    label_time.after(1000, update_time_date)          
root = tk.Tk()
root.title("Digital Clock with Date and Day")
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='black')
frame = tk.Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor='center')
label_time = tk.Label(frame, font=('Verdana', 90), bg='black', fg='red')
label_time.pack()
label_date = tk.Label(frame, font=('Verdana', 45), bg='white', fg='black')
label_date.pack()
update_time_date()
root.mainloop()
