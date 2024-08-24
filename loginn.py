from tkinter import *
from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox
import sqlite3
from Tela_Principal import App_pt2
from DbAccess.DbAccess import DbAccess


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tema()
        self.tela()
        self.tela_login() 
        self.DbAccess = DbAccess()
        #self.backend.cria_tabela()


    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

    def tela(self):
        self.geometry("600x400")
        self.title("MedicineOrganizer")
        #self.iconbitmap("icon.ico")
        self.resizable(False, False)


# TELA PRINCIPAL
    def tela_login(self):

        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack()

        self.titulo = ctk.CTkLabel(self.login_frame, text= "BEM VINDO!", text_color = "white", font = ("Roboto", 18))
        self.titulo.pack(pady = 20)

        self.nome_entry = ctk.CTkEntry(self.login_frame, width=300, placeholder_text = "Seu nome", corner_radius = 15)
        self.nome_entry.pack(pady = 5)

        self.senha_entry = ctk.CTkEntry(self.login_frame, width=300, placeholder_text = "Senha", show = "*", corner_radius = 15)
        self.senha_entry.pack(pady = 5)

        checkbox = ctk.CTkCheckBox(self.login_frame, text = "Lembrar Login", corner_radius = 20)
        checkbox.pack(pady = 5)

        self.botao_login = ctk.CTkButton(self.login_frame, width = 160, text = "Login".upper(), hover_color = "#202020", corner_radius = 15, command = self.login)
        self.botao_login.pack(pady = 5)

        self.novo_usuario = ctk.CTkButton(self.login_frame, width = 160, text = "Criar Novo Usuário".upper(), hover_color = "#202020", command = self.tela_cadastro, corner_radius = 15)
        self.novo_usuario.pack(pady = 5)
        
        self.reset_senha = ctk.CTkButton(self.login_frame, width = 160, text = "Resetar senha".upper(), hover_color = "#202020", command = self.tela_reset, corner_radius = 15)
        self.reset_senha.pack(pady = 5)

# TELA DE CADASTRO
    def tela_cadastro(self):
            
        #REMOVER O FRAME DE LOGIN
        self.login_frame.pack_forget()

        self.cadastro_frame = ctk.CTkFrame(self)
        self.cadastro_frame.pack()

        self.novo_cadastro = ctk.CTkLabel(self.cadastro_frame, text= "NOVO USUÁRIO", font = ("Roboto", 18))
        self.novo_cadastro.pack(pady = 10)

        self.span = ctk.CTkLabel(self.cadastro_frame, text= "Por favor preencha todos os campos.", font = ("Roboto", 12))
        self.span.pack()

        self.novo_usuario = ctk.CTkEntry(self.cadastro_frame, width=300, placeholder_text = "Seu nome", corner_radius = 15)
        self.novo_usuario.pack(pady = 10)

        self.novo_cpf = ctk.CTkEntry(self.cadastro_frame, width=300, placeholder_text = "CPF", corner_radius = 15)
        self.novo_cpf.pack(pady = 10)

        self.nova_senha = ctk.CTkEntry(self.cadastro_frame, width=300, placeholder_text = "Senha", show = "*", corner_radius = 15)
        self.nova_senha.pack(pady = 10)

        self.confirmar_senha = ctk.CTkEntry(self.cadastro_frame, width=300, placeholder_text = "Confirmação de senha", show = "*", corner_radius = 15)
        self.confirmar_senha.pack(pady = 10)

        self.save_button = ctk.CTkButton(self.cadastro_frame, width = 150, text = "CADASTRAR", fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command = self.Cadastrar)
        self.save_button.pack(pady = 5)

        def back():
            self.cadastro_frame.pack_forget()

            self.login_frame.pack()

        self.back_button = ctk.CTkButton(self.cadastro_frame, width = 150, text = "VOLTAR", fg_color = "Gray", hover_color = "#202020", corner_radius = 15, command = back)
        self.back_button.pack(pady = 5)


# TELA RESETE DE SENHA
    def tela_reset (self):

        #REMOVER O FRAME DE LOGIN
        self.login_frame.pack_forget()

        self.resetSenha_frame = ctk.CTkFrame(self)
        self.resetSenha_frame.pack()
        
        self.reset_frame = ctk.CTkLabel(self.resetSenha_frame, text= "NOVA SENHA", font = ("Roboto", 18))
        self.reset_frame.pack(pady = 10)

        self.antiga_senha = ctk.CTkEntry(self.resetSenha_frame, width=300, placeholder_text = "Antiga senha", show = "*", corner_radius = 15)
        self.antiga_senha.pack(pady = 10)
        
        self.nova_senha1 = ctk.CTkEntry(self.resetSenha_frame, width=300, placeholder_text = "Nova senha", show = "*", corner_radius = 15)
        self.nova_senha1.pack(pady = 10)
            
        self.confirmar_senha1 = ctk.CTkEntry(self.resetSenha_frame, width=300, placeholder_text = "Confirmação de senha", show = "*", corner_radius = 15)
        self.confirmar_senha1.pack(pady = 10)

        def save_user():
            msg = messagebox.showinfo(title = "Estado de senha", message = "Parabéns! Senha resetada com sucesso.")

        self.save_button1 = ctk.CTkButton(self.resetSenha_frame, width = 150, text = "Confirmar".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command = save_user)
        self.save_button1.pack(pady = 5) 

        def back():  
            self.resetSenha_frame.pack_forget() 

            self.login_frame.pack()


        self.back_button1 = ctk.CTkButton(self.resetSenha_frame, width = 150, text = "Voltar".upper(), fg_color = "Gray", hover_color = "#202020", corner_radius = 15, command = back)
        self.back_button1.pack(pady = 5)

    def limpa_cadastro(self):
        self.novo_usuario.delete(0, END)
        self.novo_cpf.delete(0, END)
        self.nova_senha.delete(0, END)
        self.confirmar_senha.delete(0, END)

    def limpa_login(self):
        self.nome_entry.delete(0, END)
        self.senha_entry.delete(0, END) 

    def tela_principal(self):

        self.tela_frame = ctk.CTkFrame(self)
        self.tela_frame.pack()

        self.titulo2 = ctk.CTkLabel(self.tela_frame, text= "BEM VINDO!", text_color = "white", font = ("Roboto", 18))
        self.titulo2.pack(pady = 20)

        self.antiga_senha = ctk.CTkEntry(self.tela_frame, width=300, placeholder_text = "Antiga senha", show = "*", corner_radius = 15)
        self.antiga_senha.pack(pady = 10)

    def login(self):

        usuario = self.nome_entry.get()
        senha   = self.senha_entry.get()
        
        acesso = []
        acesso.append(usuario)
        acesso.append(senha)
        LoginSucesso = self.DbAccess.CriarLogin(acesso)


        if LoginSucesso:

            self.destroy()
            TelaPrincipal = App_pt2(usuario)
            TelaPrincipal.mainloop()

        else:

            messagebox.showerror(title="Login não realizado", message="Usuário e/ou senha inválidos")

    def Cadastrar(self):

        usuario = self.novo_usuario.get()
        senha   = int(self.nova_senha.get())
        cpf     = self.novo_cpf.get()

        DadosUsuario = [ usuario, senha, cpf ]

        UsuarioCriado = self.DbAccess.CriarUsuario(DadosUsuario)

        if ( UsuarioCriado ):

            messagebox.showinfo(title="Sucesso", message="Usuário Criado com Sucesso")
        else:
            messagebox.showerror(title="Erro", message="Erro ao criar usuário")


if __name__ == "__main__":
    app = App()
    app.mainloop()