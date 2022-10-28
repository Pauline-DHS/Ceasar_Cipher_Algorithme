import tkinter as tk
from tkinter import ttk

class App(tk.Tk):

	def __init__(self):
		super().__init__()
		self.title('Application de Crypatge')
		self.geometry("800x600")
		self.name_var = tk.StringVar() 
		self.entier_var = tk.IntVar()
		
		self.config(bg='#0B3948')
	
		self.create_widgets()
		
	def create_widgets(self):

		#padding = {'padx': 10, 'pady': 10}
		# label
		label1 = ttk.Label(self, text='Votre chaîne de caractères :', background='#0B3948', font='bold').place(x=300, y=220)
		
		
		# Entry
		name_entry = ttk.Entry(self, textvariable=self.name_var)
		name_entry.place(x=190, y=250)
		name_entry.config(width=50)

		# Button
		submit_button_encrypter = ttk.Button(self, text='Encrypter',command=self.encryptage)
		submit_button_encrypter.place(x=220, y=320)
		#submit_button_encrypter.config(background='black')
     

		submit_button_decrypter = ttk.Button(self, text='Décrypter', command=self.decryptage)
		submit_button_decrypter.place(x=470, y=320)	

		


	def encryptage(self):
		Messageacrypter=self.name_var.get()
		cle=24 # Décalage par rapport à Y (code ASCII : 24 + 1 = 25e lettre de l'alphabet)

		acrypter=Messageacrypter.upper()
		lg=len(acrypter)
		MessageCrypte=""

		for i in range(lg):
			if acrypter[i]==' ':
				MessageCrypte+=' '
			else:
				asc=ord(acrypter[i])+cle
				MessageCrypte+=chr(asc+26*((asc<65)-(asc>90)))

		print(MessageCrypte)
		self.output_label=ttk.Label(self, text=MessageCrypte, background='#ACB0BD', font='bold').place(x=370, y=400)
		self.label2 = ttk.Label(self, text='Votre chaîne encryptée/décryptée :', background='#0B3948', font='bold').place(x=50, y=400)

	def decryptage(self):
		MessageCrypte=self.name_var.get()
		lg=len(MessageCrypte)
		MessageClair=""
		cle=24 # Décalage par rapport à Y (code ASCII : 24 + 1 = 25e lettre de l'alphabet)

		for i in range(lg):
			if MessageCrypte[i]==' ':
				MessageClair+=' '
			else:
				asc=ord(MessageCrypte[i])-cle
				MessageClair+=chr(asc+26*((asc<65)-(asc>90)))

		print(MessageClair)
		self.label2 = ttk.Label(self, text='Votre chaîne encryptée/décryptée :', background='#0B3948', font='bold').place(x=50, y=400)
		self.output_label=ttk.Label(self, text=MessageClair, background='#ACB0BD', font='bold').place(x=370, y=400)
		
		
if __name__ == "__main__":
	app = App()
	app.mainloop()
