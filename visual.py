import tkinter as tk
from tkinter import ttk

root = tk.Tk()

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Имя:").grid(column=0, row=0, sticky=tk.W)
name_entry = ttk.Entry(frame)
name_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Дата рождения:").grid(column=0, row=1, sticky=tk.W)
birthday_entry = ttk.Entry(frame)
birthday_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Проекты:").grid(column=0, row=2, sticky=tk.W)
project_entry = ttk.Entry(frame)
project_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Роль:").grid(column=0, row=3, sticky=tk.W)
role_entry = ttk.Entry(frame)
role_entry.grid(column=1, row=3, sticky=(tk.W, tk.E))

# ttk.Button(frame, text="Искать", command=search).grid(column=0, row=4, sticky=tk.W)
ttk.Button(frame, text="Показать всё", command=show_all).grid(column=1, row=4, sticky=tk.W)
# ttk.Button(frame, text="Добавить", command=add).grid(column=2, row=4, sticky=tk.W)

root.mainloop()


