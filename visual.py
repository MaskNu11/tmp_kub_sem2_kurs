from db.engine import SESSION_MAKER
from db.orm_quary import orm_query_get_user

import asyncio
import tkinter as tk


async def visual_get_users(output_widget, username):
    async with SESSION_MAKER() as session:
        rows = await orm_query_get_user(session=session, name=username)
        output_widget.delete('1.0', tk.END)  # Очищаем предыдущий вывод
        for i in rows:
            output_widget.insert(tk.END, f'{i.name}, {i.project}, {i.birthday}\n')