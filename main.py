from tkinter import *
from tkinter import ttk
import pywhatkit


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Cria o campo de entrada para o número de telefone
        self.phone_label = ttk.Label(self, text="Número de telefone:")
        self.phone_label.pack()
        self.phone_entry = ttk.Entry(self)
        self.phone_entry.pack()

        # Cria o campo de entrada para a mensagem
        self.message_label = ttk.Label(self, text="Mensagem:")
        self.message_label.pack()
        self.message_entry = ttk.Entry(self)
        self.message_entry.pack()

        # Cria o campo de entrada para a hora
        self.hour_label = ttk.Label(self, text="Hora:")
        self.hour_label.pack()
        self.hour_entry = ttk.Entry(self)
        self.hour_entry.pack()

        # Cria o campo de entrada para o minuto
        self.minute_label = ttk.Label(self, text="Minuto:")
        self.minute_label.pack()
        self.minute_entry = ttk.Entry(self)
        self.minute_entry.pack()

        # Cria o botão de envio
        self.send_button = ttk.Button(self, text="Enviar mensagem", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        phone = self.phone_entry.get()
        message = self.message_entry.get()
        hour = int(self.hour_entry.get())
        minute = int(self.minute_entry.get())

        pywhatkit.sendwhatmsg(phone, message, hour, minute)


root = Tk()
app = Application(master=root)
app.mainloop()
