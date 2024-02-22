import tkinter as tk
from tkinter import filedialog, messagebox
import random
import fitz  # PyMuPDF
from PIL import Image, ImageTk

class DiceRollerApp:
    def __init__(self, master):
        self.master = master
        master.title("Bafo do Dragão - Rolagens")
        master.geometry("800x600")

        self.label = tk.Label(master, text="Escolha o dado para rolar:")
        self.label.pack()

        self.dice_options = [4, 6, 8, 10, 12, 20]
        self.dice_choice = tk.StringVar(master)
        self.dice_choice.set(self.dice_options[0])

        self.dice_menu = tk.OptionMenu(master, self.dice_choice, *self.dice_options)
        self.dice_menu.pack()

        self.roll_button = tk.Button(master, text="Rolar", command=self.roll_dice)
        self.roll_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.pdf_viewer = tk.Label(master, bg="white")
        self.pdf_viewer.pack(fill=tk.BOTH, expand=True)

        self.load_pdf_button = tk.Button(master, text="Abrir PDF", command=self.load_pdf)
        self.load_pdf_button.pack()

        self.current_pdf_images = []

    def roll_dice(self):
        dice_value = int(self.dice_choice.get())
        result = random.randint(1, dice_value)
        messagebox.showinfo("Resultado", f"Você rolou um d{dice_value} e obteve: {result}")
        self.result_label.config(text=f"Último resultado: {result}")

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                self.current_pdf_images = []
                doc = fitz.open(file_path)
                for page in doc:
                    img = self.convert_page_to_image(page)
                    self.current_pdf_images.append(img)
                self.show_page(0)
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao abrir o PDF: {str(e)}")

    def convert_page_to_image(self, page):
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return ImageTk.PhotoImage(img)

    def show_page(self, page_number):
        if self.current_pdf_images:
            page_image = self.current_pdf_images[page_number]
            self.pdf_viewer.config(image=page_image)
            self.pdf_viewer.image = page_image

root = tk.Tk()
app = DiceRollerApp(root)
root.mainloop()