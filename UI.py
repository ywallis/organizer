import tkinter
import tkinter.filedialog
from tkinter import *
from Organizer import organize_core
from tkinter import messagebox
import json

BACKGROUND_COLOR = "#56B6CF"
ACCENT_COLOR = "white"


class MyUi:

    def __init__(self):
        self.window = Tk()
        self.window.title("File Organizer")
        self.window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
        self.input_label = Label(text="Where do you need my work:", bg=BACKGROUND_COLOR, fg="white")
        self.input_label.grid(row=0, column=0, padx=10)
        self.browse_button = Button(text="Browse", width=7, command=self.select_folder, bg=ACCENT_COLOR,
                                    highlightthickness=0)
        self.browse_button.grid(row=0, column=1, padx=10)
        self.input_path = Entry(width=54)
        self.input_path.grid(row=0, column=2, columnspan=3, padx=10)
        self.input_path.insert(0, r"C:\Users\your_path\ ")
        self.organize_button = Button(text="Organize!", command=self.organize, bg=ACCENT_COLOR, highlightthickness=0)
        self.organize_button.grid(row=0, column=5, padx=10)
        self.new_entry = Label(text="Add a file type:", bg=BACKGROUND_COLOR, fg="white")
        self.new_entry.grid(row=1, column=0, padx=10, pady=10)
        self.new_extension = Label(text="Extension:", bg=BACKGROUND_COLOR, fg="white")
        self.new_extension.grid(row=1, column=1, padx=10)
        self.new_extension_entry = Entry()
        self.new_extension_entry.grid(row=1, column=2, padx=10)
        self.new_type = Label(text="Type:", bg=BACKGROUND_COLOR, fg="white")
        self.new_type.grid(row=1, column=3, padx=10)
        self.new_type_entry = Entry()
        self.new_type_entry.grid(row=1, column=4, padx=10)
        self.add_entry_button = Button(text="Add!", width=7, command=self.add_type,
                                       bg=ACCENT_COLOR, highlightthickness=0)
        self.add_entry_button.grid(row=1, column=5, padx=10)

        self.canvas = Canvas(width=612, height=521, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=6)
        self.mess_image = PhotoImage(file="images/mess.png")
        self.canvas.create_image(306, 260, image=self.mess_image)

        self.window.mainloop()

    def organize(self):
        path = self.input_path.get()
        organize_core(path)
        messagebox.showinfo(title="Oooh yah", message="So clean.")

    def add_type(self):
        new_extension = self.new_extension_entry.get()
        new_type = self.new_type_entry.get()
        with open("extensions.json", "r") as extension_file:
            file_extensions = json.load(extension_file)
            file_extensions[str(new_extension)] = str(new_type)
            print(file_extensions)
        with open("extensions.json", "w") as extension_output:
            json.dump(file_extensions, extension_output)
        messagebox.showinfo(title="Oooh yah", message="New extension added!")

    def select_folder(self):
        selected_directory = tkinter.filedialog.askdirectory()
        self.input_path.delete(0, END)
        self.input_path.insert(0, selected_directory)

