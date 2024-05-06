from db.engine import SESSION_MAKER
from db.orm_quary import (
    orm_query_get_data_from_year,
    orm_query_get_data_from_project,
    orm_query_get_data_from_user,
    )

import asyncio
import tkinter as tk


async def visual_get_data_from_user(output_widget, name):
    async with SESSION_MAKER() as session:
        rows = await orm_query_get_data_from_user(session=session, name=name)
        output_widget.delete('1.0', tk.END)  # Очищаем предыдущий вывод
        for i in rows:
            output_widget.insert(tk.END, f'{i.name}, {i.project}, {i.birthday}\n')


async def visual_get_data_from_project(output_widget, project):
    async with SESSION_MAKER() as session:
        rows = await orm_query_get_data_from_project(session=session, project=project)
        output_widget.delete('1.0', tk.END)  # Очищаем предыдущий вывод
        for i in rows:
            output_widget.insert(tk.END, f'{i.name}, {i.project}, {i.birthday}\n')


async def visual_get_data_from_year(output_widget, year):
    async with SESSION_MAKER() as session:
        rows = await orm_query_get_data_from_year(session=session, year=year)
        output_widget.delete('1.0', tk.END)  # Очищаем предыдущий вывод
        for i in rows:
            output_widget.insert(tk.END, f'{i.name}, {i.project}, {i.birthday}\n')

