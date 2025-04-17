import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    text_area.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_area.insert(tk.END, text)
    root.title(f"Notepad - {filepath}")

def save_file():
    filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)
    root.title(f"Notepad - {filepath}")

root = tk.Tk()
root.title("Vn Notepad")

root.rowconfigure(0, minsize=600, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

text_area = tk.Text(root)
fr_buttons = tk.Frame(root, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_area.grid(row=0, column=1, sticky="nsew")

root.mainloop()