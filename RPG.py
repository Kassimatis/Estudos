import tkinter as tk
from tkinter import filedialog, messagebox
import random
import fitz
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime

class MainMenu(tk.Toplevel):
    def __init__(self, master, on_continue, on_new_game):
        super().__init__(master)
        self.title("Menu Principal")
        self.geometry("400x300")

        self.title_label = tk.Label(self, text="Menu Principal", font=("Arial", 18))
        self.title_label.pack(pady=20)

        self.on_continue = on_continue
        self.on_new_game = on_new_game

        self.continue_button = tk.Button(self, text="CONTINUAR", command=self.continue_game)
        self.continue_button.pack()

        self.new_game_button = tk.Button(self, text="NOVO JOGO", command=self.new_game)
        self.new_game_button.pack()

        self.enter_session_button = tk.Button(self, text="ENTRAR EM SESSÃO", command=self.enter_session)
        self.enter_session_button.pack()

    def continue_game(self):
        if self.on_continue:
            self.on_continue()

    def new_game(self):
        if self.on_new_game:
            self.on_new_game()

    def enter_session(self):
        player_name = input("Digite o seu nome: ")  # Altere para um campo de entrada de texto no GUI
        self.master.start_session(player_name)

class DiceRollerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bafo do Dragão - Rolagens")
        self.geometry("800x600")

        # Visualizador de PDF
        self.pdf_viewer = tk.Label(self, bg="white")
        self.pdf_viewer.pack(fill=tk.BOTH, expand=True)

        # Opções de dado
        self.label = tk.Label(self, text="Escolha o dado para rolar:")
        self.label.pack()

        self.dice_options = [4, 6, 8, 10, 12, 20]
        self.dice_choice = tk.StringVar(self)
        self.dice_choice.set(self.dice_options[0])

        self.dice_menu = tk.OptionMenu(self, self.dice_choice, *self.dice_options)
        self.dice_menu.pack()

        # Botão de rolar
        self.roll_button = tk.Button(self, text="Rolar", command=self.roll_dice)
        self.roll_button.pack()

        # Lista de imagens do PDF atual
        self.current_pdf_images = []

        # Conectar ao banco de dados (ou criar se não existir)
        self.conn = sqlite3.connect('sessions.db')
        self.create_session_table()

    def create_session_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS sessions
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            player_name TEXT NOT NULL,
                            start_time TIMESTAMP NOT NULL,
                            end_time TIMESTAMP)''')
        self.conn.commit()

    def start_session(self, player_name):
        start_time = datetime.now()
        self.conn.execute('INSERT INTO sessions (player_name, start_time) VALUES (?, ?)', (player_name, start_time))
        self.conn.commit()
        print(f'Sessão iniciada para o jogador {player_name} às {start_time}')

    def roll_dice(self):
        dice_value = int(self.dice_choice.get())
        result = random.randint(1, dice_value)
        messagebox.showinfo("Resultado", f"Você rolou um d{dice_value} e obteve: {result}")

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

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    def on_continue():
        app = DiceRollerApp()
        app.mainloop()

    def on_new_game():
        app = DiceRollerApp()
        app.mainloop()

    root = tk.Tk()
    menu = MainMenu(root, on_continue, on_new_game)
    root.mainloop()