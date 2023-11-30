# Simple Notepad Made In Python.
# Created By: Luiz Gabriel Magalhães Trindade.
# This Software is Distributed Under The GPL3 License.
# GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from customtkinter import *
from sys import argv

file_name = str(argv[1])
file_lines = []
try:
    with open(file_name, "r") as file:
        file_content = file.readlines()
        for i in file_content:
            file_lines.append(i.strip())
except: pass

def Save():
    content = Text_Area.get("0.0", "end")
    try:
        with open(file_name, "w") as file:
            file.write(content+"\n")
    except: pass


app = CTk()
app.title("notepad🗒️  "+f"'{file_name}'")
app.geometry("500x500")

Save = CTkButton(master=app, text="save 💾", font=("Arial", 20, "bold"), command=Save)
Save.pack(pady=10, padx=10)

Text_Area = CTkTextbox(master=app, width=1500, height=800, font=("Times New Roman", 30))
Text_Area.pack(pady=10, padx=20)

counter = float(1)
for i in file_lines:
    Text_Area.insert(f"{counter}", i+"\n")
    counter += 1

app.mainloop()
