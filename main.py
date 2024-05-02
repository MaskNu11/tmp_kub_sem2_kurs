import asyncio
import json
import tkinter as tk

from db.engine import SESSION_MAKER, create_db
from db.orm_quary import orm_add_user, urm_quared_get_user_all


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

async def main(output_widget):
    await create_db()
    json_data = list()
    json_data = read_json_file('collected_data_with_dob_test.json')

    async with SESSION_MAKER() as session:

        await orm_add_user(session, json_data)
        rows = await urm_quared_get_user_all(session)
        for i in rows:
            output_widget.insert(tk.END, i.name + '\n')
        session.close()

def get_data_and_display(loop, output_widget):
    loop.run_until_complete(main(output_widget))

app = tk.Tk()
app.title("ORM Data Viewer")

output_text = tk.Text(app)
output_text.pack()

button = tk.Button(app, text="Достать данные", command=lambda: get_data_and_display(asyncio.new_event_loop(), output_text))
button.pack()

if __name__ == '__main__':
    app.mainloop()
