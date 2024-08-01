from tkinter import *
from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox

class App_pt2(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tema()
        self.tela_principal()
        self.tela_usuario()
         
        
    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

    def tela_principal(self):
        self.geometry("900x500")
        self.title("MedicineOrganizer")
        self.iconbitmap("icon.ico") 
        self.resizable(False, False)   


# TELA PRINCIPAL
    def tela_usuario(self):

        self.opcoes_frame = ctk.CTkFrame(self, width=250, height=490)
        self.opcoes_frame.pack(side = LEFT)

        self.img = PhotoImage(file = "usuario.png")
        self.imagem = Label(self.opcoes_frame, image = self.img, width=150, height=150)
        self.imagem.place(x=47, y=5)

        self.usuario_de_login = ctk.CTkLabel(self.opcoes_frame, text= "Usuario", font = ("Roboto", 14))
        self.usuario_de_login.place(x=100, y=160)

        self.pacientes_entry = ctk.CTkButton(self.opcoes_frame, text = "Pacientes".upper(), font = ("Roboto", 18), width = 180, fg_color = "Gray", hover_color = "#202020", corner_radius = 15, command = self.click_pacientes)
        self.pacientes_entry.place(x=33, y=230)

        self.medicamentos_entry = ctk.CTkButton(self.opcoes_frame, text = "Medicamentos".upper(), font = ("Roboto", 18), width = 180, fg_color = "Gray", hover_color = "#202020", corner_radius = 15 )
        self.medicamentos_entry.place(x=33, y=280)

        self.horarios_entry = ctk.CTkButton(self.opcoes_frame, text = "Horários".upper(), font = ("Roboto", 18), width = 180, fg_color = "Gray", hover_color = "#202020", corner_radius = 15)
        self.horarios_entry.place(x=33, y=330)

    def click_pacientes(self):

        self.pacientes_frame = ctk.CTkFrame(self, width=610, height=60)
        self.pacientes_frame.place(x=270, y= 5)

        self.cadastrar_pacientes_entry = ctk.CTkButton(self.pacientes_frame, text= "cadastrar paciente".upper(), font = ("Roboto", 14), width = 180, fg_color = "#202020", hover_color = "Gray", corner_radius = 1, command = self.novo_paciente)
        self.cadastrar_pacientes_entry.place(x=40, y=15)

        self.pacientes_ativos_entry = ctk.CTkButton(self.pacientes_frame, text= "Pacientes Ativos".upper(), font = ("Roboto", 14), width = 180, fg_color = "#202020", hover_color = "Gray", corner_radius = 1,command = self.pacientes_ativos)
        self.pacientes_ativos_entry.place(x=215, y=15)

        self.deletar_pacientes_entry = ctk.CTkButton(self.pacientes_frame, text= "deletar pacientes".upper(), font = ("Roboto", 14), width = 180, fg_color = "#202020", hover_color = "Gray", corner_radius = 1, command = self.delet_paciente)
        self.deletar_pacientes_entry.place(x=390, y=15)

    def novo_paciente(self):

        self.registro_paciente = ctk.CTkFrame(self, width=610, height=415)
        self.registro_paciente.place(x=270, y= 80)

        self.novo_cadastro_frame = ctk.CTkLabel(self.registro_paciente, text= "novo paciente".upper(), font = ("Roboto", 18))
        self.novo_cadastro_frame.place(x=240, y=25)

        self.span2 = ctk.CTkLabel(self.registro_paciente, text= "Por favor preencha todos os campos".upper(), font = ("Roboto", 12))
        self.span2.place(x=190, y=60)
            
        self.nome_paciente = ctk.CTkEntry(self.registro_paciente, width=400, placeholder_text = "Nome do paciente".upper(), corner_radius = 15)
        self.nome_paciente.place(x=110, y=100)

        
        self.novo_cpf_paciente = ctk.CTkEntry(self.registro_paciente, width=400, placeholder_text = "CPF", corner_radius = 15)
        self.novo_cpf_paciente.place(x=110, y=150)

        self.data_nasci = ctk.CTkEntry(self.registro_paciente, width=400, placeholder_text = "Data de nascimento".upper(), corner_radius = 15)
        self.data_nasci.place(x=110, y=200)

        self.save_button_paciente = ctk.CTkButton(self.registro_paciente, width = 250, text = "Cadastrar paciente".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15)
        self.save_button_paciente.place(x=185, y=250)

    
    def pacientes_ativos(self): 


        self.paciente_ativo_frame = ctk.CTkFrame(self, width=610, height=415)
        self.paciente_ativo_frame.place(x=270, y= 80)

    
    def delet_paciente(self): 


        self.delet_frame = ctk.CTkFrame(self, width=610, height=415)
        self.delet_frame.place(x=270, y= 80)

        self.span3 = ctk.CTkLabel(self.delet_frame, text= "Por favor digite uma das opcões abaixo para deletar".upper(), font = ("Roboto", 12))
        self.span3.place(x=140, y=60)
            
        self.delet_cpf = ctk.CTkEntry(self.delet_frame, width=400, placeholder_text = "CPF".upper(), corner_radius = 15)
        self.delet_cpf.place(x=110, y=100)

        self.delet_data_nasci = ctk.CTkEntry(self.delet_frame, width=400, placeholder_text = "Data de nascimento".upper(), corner_radius = 15)
        self.delet_data_nasci.place(x=110, y=150)

        self.delet_button_paciente = ctk.CTkButton(self.delet_frame, width = 250, text = "deletar paciente".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15)
        self.delet_button_paciente.place(x=185, y=200)






    

        






        



if __name__ == "__main__":
    app = App_pt2()
    app.mainloop()