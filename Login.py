from  tkinter import *
from hashlib import sha1

class LoginForm(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.renderForm()

	def renderForm(self):
		self.title = "Área do Aluno:"
		self.geometry("320x120+500+250")
		self.resizable(width="FALSE",height="FALSE")

		self.login = StringVar()
		self.login = "Resultado"

		self.titulo = Label(self, text = "Acesso")
		self.identificacao = Label(self, text = "Usuário: ").pack()
		self.identificacao = Entry(self)
		self.identificacao.pack()
		self.senha = Label(self, text= "Senha: ").pack()
		self.senha = Entry(self, show="*", width=15)
		self.senha.pack()
		self.botao =  Button(self, text = "Submit", command = self.doLogin).pack()

	def encodePassword(self):
		return sha1(self.senha.get().encode('utf-8')).hexdigest()

	def doLogin(self):
		if self.identificacao.get() != "admin":
			print("identificacao incorreta")
			return FALSE
		#substituir por valor retirado do BD 
		defaultPasswordValue = sha1("admin".encode('utf-8')).hexdigest()
		if self.encodePassword() != defaultPasswordValue:
			print("senha incorreta")
			return FALSE
def main():

	loginForm = LoginForm()
	loginForm.mainloop()

main()
