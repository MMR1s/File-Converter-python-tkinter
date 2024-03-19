import csv
import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def text_to_csv(file_input):
    if file_input.endswith(".txt") and os.path.exists(file_input):
        with open(file_input, "r") as txt_file:
            reader = [line.strip().split() for line in txt_file]

        with open("csvfile.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(reader)

        messagebox.showinfo("Conversion Complete", "Text to CSV conversion successful!")
    else:
        messagebox.showerror("File Error", "File not found or not a .txt file.")


def text_to_json(file_input):
    if file_input.endswith(".txt") and os.path.exists(file_input):
        with open(file_input, "r") as txt_file:
            reader = [line.strip().split() for line in txt_file]

        data_dict = {"Infos": reader}

        with open("jsonfile.json", "w") as json_file:
            json.dump(data_dict, json_file, indent=2)

        messagebox.showinfo(
            "Conversion Complete", "Text to JSON conversion successful!"
        )
    else:
        messagebox.showerror("File Error", "File not found or not a .txt file.")


def csv_to_json(file_input):
    if file_input.endswith(".csv") and os.path.exists(file_input):
        with open(file_input, "r") as csv_file:
            reader = list(csv.reader(csv_file))

        data_dict = {"Infos": reader}

        with open("jsonfile.json", "w") as json_file:
            json.dump(data_dict, json_file, indent=2)

        messagebox.showinfo("Conversion Complete", "CSV to JSON conversion successful!")
    else:
        messagebox.showerror("File Error", "File not found or not a .csv file.")


def csv_to_text(file_input):
    if file_input.endswith(".csv") and os.path.exists(file_input):
        with open(file_input, "r") as csv_file:
            reader = csv.reader(csv_file)
            lines = [" ".join(row) for row in reader]

        with open("textfile.txt", "w") as text_file:
            text_file.write("\n".join(lines))

        messagebox.showinfo("Conversion Complete", "CSV to Text conversion successful!")
    else:
        messagebox.showerror("File Error", "File not found or not a .csv file.")


def json_to_text(file_input):
    if file_input.endswith(".json") and os.path.exists(file_input):
        with open(file_input, "r") as json_file:
            reader = json.load(json_file)

        with open("textfile.txt", "w") as text_file:
            for elements in reader["Infos"]:
                text_file.write(" ".join(elements) + "\n")

        messagebox.showinfo(
            "Conversion Complete", "JSON to Text conversion successful!"
        )
    else:
        messagebox.showerror("File Error", "File not found or not a .json file.")


def json_to_csv(file_input):
    if file_input.endswith(".json") and os.path.exists(file_input):
        with open(file_input, "r") as json_file:
            reader = json.load(json_file)

        with open("csvfile.csv", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(reader["Infos"])

        messagebox.showinfo("Conversion Complete", "JSON to CSV conversion successful!")
    else:
        messagebox.showerror("File Error", "File not found or not a .json file.")


def browse_file():
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def convert_file():
    file_path = entry.get()
    choice = var.get()
    functions = [
        text_to_csv,
        text_to_json,
        csv_to_json,
        csv_to_text,
        json_to_text,
        json_to_csv,
    ]

    if 0 < choice <= len(functions):
        functions[choice - 1](file_path)
    else:
        messagebox.showerror(
            "Invalid Choice", "Please choose a number between 1 and 6."
        )


app = tk.Tk()
app.title("File Converter")

frame = tk.Frame(app)
frame.pack(padx=20, pady=10)

label = tk.Label(frame, text="Choose Conversion Type:")
label.grid(row=0, column=0, columnspan=2, pady=5)

var = tk.IntVar()
choices = [
    ("Text to CSV", 1),
    ("Text to JSON", 2),
    ("CSV to JSON", 3),
    ("CSV to Text", 4),
    ("JSON to Text", 5),
    ("JSON to CSV", 6),
]

row = 1
for text, val in choices:
    tk.Radiobutton(frame, text=text, variable=var, value=val).grid(
        row=row, column=0, sticky=tk.W, padx=5
    )
    row += 1

button_browse = tk.Button(frame, text="Browse", command=browse_file)
button_browse.grid(row=row, column=0, pady=10)

entry = tk.Entry(frame, width=50)
entry.grid(row=row, column=1, pady=10)

button_convert = tk.Button(frame, text="Convert", command=convert_file)
button_convert.grid(row=row + 1, column=0, columnspan=2, pady=10)

app.mainloop()
