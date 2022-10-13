import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

	def __init__(self):
		super().__init__()
		self.title('Application de Crypatge')
		self.geometry("800x600")

		self.name_var = tk.StringVar() 
		
		self.columnconfigure(0, weight=1)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)
	
		self.create_widgets()
		
	def create_widgets(self):

		padding = {'padx': 10, 'pady': 10}
		# label
		ttk.Label(self, text='Votre chaîne de caractères:').place(x=100, y=100)

		# Entry
		name_entry = ttk.Entry(self, textvariable=self.name_var)
		name_entry.place(x=300, y=100)
		name_entry.config(width=50)
		name_entry.focus()

		# Button
		submit_button_encrypter = ttk.Button(self, text='Encrypter', command=self.submit)
		submit_button_encrypter.place(x=250, y=200)

		submit_button_decrypter = ttk.Button(self, text='Décrypter', command=self.submit)
		submit_button_decrypter.place(x=450, y=200)

		# Output label
		self.output_label = ttk.Label(self)
		self.output_label.place(x=300, y=100)


	def submit(self):
		self.output_label.config(text=self.name_var.get())


if __name__ == "__main__":
	app = App()
	app.mainloop()
