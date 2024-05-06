import asyncio
import json
import tkinter as tk

from tkinter import ttk  # Импортируем модуль ttk для использования Combobox
from db.engine import SESSION_MAKER, create_db

from visual import (
    visual_get_data_from_user,
    visual_get_data_from_project,
    visual_get_data_from_year,
    )


# def read_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data

# async def main(output_widget):
#     await create_db()
#     json_data = list()
#     json_data = read_json_file('collected_data_with_dob_test.json')

#     async with SESSION_MAKER() as session:

#         # await orm_add_user(session, json_data)
#         # rows = await urm_quared_get_user_all(session)
#         # for i in rows:
#         #     output_widget.insert(tk.END, i.name + '\n')
#         # session.close()
#         rows = await orm_query_get_user(session=session, name='СЕРГЕЙ АКИМОВ')
#         for i in rows:
#             print(i.name)

async def get_data_and_display(output_widget, entry, selection, task):
    if task and not task.done():
        return
    value = entry.get()
    if not value:
        return
    if selection == "ФИО":
        task = asyncio.create_task(visual_get_data_from_user(output_widget, value))
    elif selection == "Название проекта":
        task = asyncio.create_task(visual_get_data_from_project(output_widget, value))
    elif selection == "Год":
        task = asyncio.create_task(visual_get_data_from_year(output_widget, value))
    entry.delete(0, tk.END)  # Очищаем поле ввода

async def main():
    app = tk.Tk()
    app.title("ORM Data Viewer")

    output_text = tk.Text(app)
    output_text.pack()

    entry_frame = tk.Frame(app)
    entry_frame.pack()

    # Создаем Combobox для выбора категории
    categories = ["ФИО", "Название проекта", "Год"]
    selected_category = tk.StringVar()
    category_combobox = ttk.Combobox(entry_frame, textvariable=selected_category, values=categories, width=20)
    category_combobox.grid(row=0, column=0)

    entry = tk.Entry(entry_frame, width=20)  
    entry.grid(row=0, column=1)

    task = None
    button = tk.Button(entry_frame, text="Получить данные", command=lambda: asyncio.create_task(get_data_and_display(output_text, entry, selected_category.get(), task)), width=20)  # Увеличиваем ширину кнопки
    button.grid(row=0, column=2)

    async def update_tkinter():
        while True:
            try:
                app.update()
                await asyncio.sleep(0.01)
            except tk.TclError:
                break

    await asyncio.gather(update_tkinter(), asyncio.sleep(0.01))
    app.mainloop()

if __name__ == '__main__':
    asyncio.run(main())