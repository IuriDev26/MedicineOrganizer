from PIL import Image as Imagemtesteiuri
from tkinter import *
from typing import Tuple
import customtkinter as ctk
from tkinter import messagebox
from DbAccess.DbAccess import DbAccess
from tkinter import ttk

class App_pt2(ctk.CTk):
    def __init__(self, usuario, cpf):
        super().__init__()
        self.tema()
        self.tela_principal()
        self.tela_usuario(usuario)
        self.DbAccess = DbAccess() 
        self.cpf_usuario_logado = cpf


    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

    def tela_principal(self):
        self.geometry("900x500")
        self.title("MedicineOrganizer")
        self.iconbitmap("icon.ico") 
        self.resizable(False, False)   


# TELA PRINCIPAL
    def tela_usuario(self, usuario):

        self.opcoes_frame = ctk.CTkFrame(self, width=250, height=490)
        self.opcoes_frame.pack(side = LEFT)

        self.img = PhotoImage(file = "usuario.png")
        self.imagem = Label(self.opcoes_frame, image = self.img, width=150, height=150)
        self.imagem['image'] = self.img
        self.imagem.place(x=47, y=5)

        self.usuario_de_login = ctk.CTkLabel(self.opcoes_frame, text= usuario, font = ("Roboto", 14))
        self.usuario_de_login.place(x=100, y=160)

        self.pacientes_entry = ctk.CTkButton(self.opcoes_frame, text = "Pacientes".upper(), font = ("Roboto", 18), width = 180, fg_color = "Gray", hover_color = "#202020", corner_radius = 15, command = self.click_pacientes)
        self.pacientes_entry.place(x=33, y=230)

        self.medicamentos_entry = ctk.CTkButton(self.opcoes_frame, text = "Medicamentos".upper(), font = ("Roboto", 18), width = 180, fg_color = "Gray", hover_color = "#202020", corner_radius = 15,
                                                command=self.click_medicamentos)
        self.medicamentos_entry.place(x=33, y=280)

        self.horarios_entry = ctk.CTkButton(self.opcoes_frame, text = "Agendamentos".upper(), font = ("Roboto", 18), width = 180, fg_color = "Gray", hover_color = "#202020", corner_radius = 15, command=self.click_agendamentos)
        self.horarios_entry.place(x=33, y=330)

    def click_pacientes(self):

        self.pacientes_frame = ctk.CTkFrame(self, width=610, height=60)
        self.pacientes_frame.place(x=270, y= 5)

        self.cadastrar_pacientes_entry = ctk.CTkButton(self.pacientes_frame, text= "cadastrar paciente".upper(), font = ("Roboto", 14), width = 200, fg_color = "#202020", hover_color = "Gray", corner_radius = 5, command = self.novo_paciente)
        self.cadastrar_pacientes_entry.place(x=100, y=15)

        self.pacientes_ativos_entry = ctk.CTkButton(self.pacientes_frame, text= "Pacientes Ativos".upper(), font = ("Roboto", 14), width = 200, fg_color = "#202020", hover_color = "Gray", corner_radius = 5,command = self.pacientes_ativos)
        self.pacientes_ativos_entry.place(x=320, y=15)

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

        self.save_button_paciente = ctk.CTkButton(self.registro_paciente, width = 250, text = "Cadastrar paciente".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command=self.criar_paciente_banco)
        self.save_button_paciente.place(x=185, y=250)


    def pacientes_ativos(self): 

        self.registro_paciente.place_forget()

        self.paciente_ativo_frame = ctk.CTkFrame(self, width=610, height=415)
        self.paciente_ativo_frame.place(x=270, y= 80)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview",
                background="#202020",  # Cor de fundo
                foreground="white",    # Cor do texto
                rowheight=25,          # Altura das linhas
                fieldbackground="#202020")  # Cor de fundo do campo

        self.pacientes_at = ttk.Treeview(self.paciente_ativo_frame, columns=("cpf", "nome"), show="headings", style="Custom.Treeview")
        self.pacientes_at.pack(fill="both", expand=True)

        # Definir os cabeçalhos das colunas
        self.pacientes_at.heading("cpf", text="CPF")

        self.pacientes_at.heading("nome", text="Nome")

        # Definir o tamanho das colunas
        self.pacientes_at.column("cpf", anchor="center", width=305)

        self.pacientes_at.column("nome", anchor="center", width=305)



        pacientes = self.DbAccess.GetPacientesAtivos( self.cpf_usuario_logado )

        for paciente in pacientes:
            self.pacientes_at.insert("", "end", values=(paciente[0], paciente[1], "Excluir"))

    def criar_paciente_banco(self):

        nome = self.nome_paciente.get()
        cpf  = self.novo_cpf_paciente.get()

        paciente = [ nome, cpf ]

        self.DbAccess.CriarPaciente(paciente)

        messagebox.showinfo( title="Sucesso", message="Paciente adicionado com sucesso" )

    def click_medicamentos(self):

        self.medicamentos_frame = ctk.CTkFrame(self, width=610, height=60)
        self.medicamentos_frame.place(x=270, y= 5)

        self.cadastrar_medicamento_entry = ctk.CTkButton(self.medicamentos_frame, text= "cadastrar medicamento".upper(), font = ("Roboto", 14), width = 200, fg_color = "#202020", hover_color = "Gray", corner_radius = 5, command = self.novo_medicamento)
        self.cadastrar_medicamento_entry.place(x=100, y=15)

        self.deletar_medicamento_entry = ctk.CTkButton(self.medicamentos_frame, text= "medicamentos ativos".upper(), font = ("Roboto", 14), width = 200, fg_color = "#202020", hover_color = "Gray", corner_radius = 5, command = self.medicamento_ativos)
        self.deletar_medicamento_entry.place(x=320, y=15)

    def novo_medicamento(self):

        self.registro_medicamento = ctk.CTkFrame(self, width=610, height=415)
        self.registro_medicamento.place(x=270, y= 80)

        self.novo_medicamento_frame = ctk.CTkLabel(self.registro_medicamento, text= "novo medicamento".upper(), font = ("Roboto", 18))
        self.novo_medicamento_frame.place(x=220, y=25)
            
        self.nome_medicamento = ctk.CTkEntry(self.registro_medicamento, width=400, placeholder_text = "Nome do Medicamento".upper(), corner_radius = 15)
        self.nome_medicamento.place(x=110, y=100)

        self.save_button_medicamento = ctk.CTkButton(self.registro_medicamento, width = 250, text = "Cadastrar medicamento".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command=self.criar_medicamento_banco)
        self.save_button_medicamento.place(x=185, y=160)

    def medicamento_ativos(self):

        self.registro_medicamento.place_forget()

        self.delet_medicamento_frame = ctk.CTkFrame(self, width=610, height=415)
        self.delet_medicamento_frame.place(x=270, y= 80)
        
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview", 
                background="#202020",  # Cor de fundo
                foreground="white",    # Cor do texto
                rowheight=25,          # Altura das linhas
                fieldbackground="#202020")  # Cor de fundo do campo
                
        self.medicamento_at = ttk.Treeview(self.delet_medicamento_frame, columns=("medicamento"), show="headings", style="Custom.Treeview")
        self.medicamento_at.pack(fill="both", expand=True)

        # Definir os cabeçalhos das colunas
        self.medicamento_at.heading("medicamento", text="Medicamentos")
        
        # Definir o tamanho das colunas
        self.medicamento_at.column("medicamento", anchor="center", width=608)
        
        
        # Adicionar dados à tabela
        medicamentos = self.DbAccess.GetRemedios()
        for medicamento in medicamentos:
            self.medicamento_at.insert("", "end", values=(medicamento[0], "Excluir"), iid=medicamento[1])

        delet_medicamento_at = ctk.CTkButton(self.delet_medicamento_frame, text = "deletar medicamento selecionado".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command= self.excluir_medicamento)
        delet_medicamento_at.pack() 

    def excluir_medicamento(self):
        
        selected_item = self.medicamento_at.selection()  # Seleciona o item
        if selected_item:  # Verifica se há um item selecionado

            excluiu, description_error = self.DbAccess.delete_medicamento(int(selected_item[0]))

            if ( not excluiu ):

                messagebox.showerror(message=description_error)
            
            else:
                self.medicamento_at.delete(selected_item)  # Exclui o item
                messagebox.showinfo(message="Tudo certo")
    def criar_medicamento_banco(self):

        medicamento = self.nome_medicamento.get()

        self.DbAccess.CriarMedicamento(medicamento)

        messagebox.showinfo( title="Sucesso", message="Medicamento adicionado com sucesso" )

    def click_agendamentos(self):

        self.agendamentos_frame = ctk.CTkFrame(self, width=610, height=60)
        self.agendamentos_frame.place(x=270, y=5)

        self.cadastrar_agendamento_entry = ctk.CTkButton(self.agendamentos_frame, text= "Novo Agendamento".upper(), font = ("Roboto", 14), width = 200, fg_color = "#202020", hover_color = "Gray", corner_radius = 5, command = self.novo_agendamento)
        self.cadastrar_agendamento_entry.place(x=100, y=15)

        self.agendamentos_ativos_entry = ctk.CTkButton(self.agendamentos_frame, text= "Agendamentos Ativos".upper(), font = ("Roboto", 14), width = 200, fg_color = "#202020", hover_color = "Gray", corner_radius = 5, command = self.agendamentos_ativos)
        self.agendamentos_ativos_entry.place(x=320, y=15)       

    def novo_agendamento(self):

        self.registro_agendamento = ctk.CTkFrame(self, width=610, height=415)
        self.registro_agendamento.place(x=270, y= 80)

        self.novo_agendamento_frame = ctk.CTkLabel(self.registro_agendamento, text= "".upper(), font = ("Roboto", 18))
        self.novo_agendamento_frame.place(x=240, y=25)

        self.span2 = ctk.CTkLabel(self.registro_agendamento, text= "click na lupa e escolha uma opção".upper(), font = ("Roboto", 11))
        self.span2.place(x=210, y=60)
        
        pacientesCadastrados = self.DbAccess.GetPacientes()
        
        search_image = ctk.CTkImage( dark_image=Imagemtesteiuri.open("Resources/Images/lupa.png") )
    
        buscar_cpf_paciente = ctk.CTkButton( self.registro_agendamento, width=5, corner_radius=10, image=search_image, text='', fg_color="#2b2b2b", hover_color = "#202020", command= self.lupa_cpf_paciente)
        buscar_cpf_paciente.place(x=508, y=100)

        buscar_remedio = ctk.CTkButton( self.registro_agendamento, width=5, corner_radius=10, image=search_image, text='', fg_color="#2b2b2b", hover_color = "#202020", command= self.lupa_remedios )
        buscar_remedio.place(x=508, y=190)

        self.cpf = ctk.CTkEntry( self.registro_agendamento, placeholder_text= "CPF", width=160, font=("Roboto", 14), corner_radius=15)
        self.cpf.configure(state="disabled")
        self.cpf.place( x=105, y=100 )
        
        self.nome_paciente = ctk.CTkEntry( self.registro_agendamento, placeholder_text= "PACIENTE", width=230, font=("Roboto", 14), corner_radius=15)
        self.nome_paciente.configure(state="disabled")
        self.nome_paciente.place( x=275, y=100 )

        self.span3 = ctk.CTkLabel(self.registro_agendamento, text= "digite o horario".upper(), font = ("Roboto", 11))
        self.span3.place(x=140, y=160)

        self.horario_remedio = ctk.CTkEntry( self.registro_agendamento, placeholder_text= "HORARIO", width=160, font=("Roboto", 14), corner_radius=15)
        self.horario_remedio.bind( "<KeyRelease>", self.mascara_horario )
        self.horario_remedio.place( x=105, y=190 )

        self.span4 = ctk.CTkLabel(self.registro_agendamento, text= "click na lupa e escolha uma opção".upper(), font = ("Roboto", 11))
        self.span4.place(x=285, y=160)

        self.remedio = ctk.CTkEntry( self.registro_agendamento, placeholder_text= "MEDICAMENTO", width=230, font=("Roboto", 14), corner_radius=15)
        self.remedio.configure(state="disabled")
        self.remedio.place( x=275, y=190 )

        self.agen_button_paciente = ctk.CTkButton(self.registro_agendamento, width = 250, text = "confirmar agendamento".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command=self.agendar)
        self.agen_button_paciente.place(x=185, y=250)

    def agendar(self):

        cpf_paciente = self.cpf.get()
        horario = self.horario_remedio.get()
        codigo_medicamento = int(self.item_selecionado_remedio[0])
        cpf_enfermeiro = self.cpf_usuario_logado

        dados = [ cpf_paciente, horario, codigo_medicamento, cpf_enfermeiro ]

        self.DbAccess.CriarAgendamento( dados )

        messagebox.showinfo( message="Agendamento realizado com Sucesso!" )



    def mascara_horario(self, event):

        text = self.horario_remedio.get()
        ultimoindice = len(text) - 1
        ultimodigito = text[ultimoindice] if ultimoindice >=0 else ""

        if not ( ultimodigito.isdigit() ):

            self.horario_remedio.delete(ultimoindice)

        if len(text) > 5:

            self.horario_remedio.delete(ultimoindice)

        if len(text) == 2:

                self.horario_remedio.insert(2, ":")



    def delet_agendamento(self):

        self.delet_agendamento_frame = ctk.CTkFrame(self, width=610, height=415)
        self.delet_agendamento_frame.place(x=270, y= 80)

        self.span3 = ctk.CTkLabel(self.delet_agendamento_frame, text= "Por favor digite o cpf".upper(), font = ("Roboto", 12))
        self.span3.place(x=240, y=60)
            
        self.deletar_agendamento = ctk.CTkEntry(self.delet_agendamento_frame, width=400, placeholder_text = "CPF".upper(), corner_radius = 15)
        self.deletar_agendamento.place(x=110, y=100)

        self.delet_button_agendamento = ctk.CTkButton(self.delet_agendamento_frame, width = 250, text = "deletar agendamento".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15)
        self.delet_button_agendamento.place(x=185, y=160)  

    def selecionar_cpf_paciente(self):
        
        item_selecionado = self.cpf_paciente.selection()
        if item_selecionado:
            valores = self.cpf_paciente.item(item_selecionado, 'values')
            # Preenchendo os campos CTkEntry com os valores correspondentes
            self.cpf.configure(state="normal")
            self.cpf.delete(0, ctk.END)
            self.cpf.insert(0, valores[0])
            self.cpf.configure(state="disabled")
            
            self.nome_paciente.configure(state="normal")
            self.nome_paciente.delete(0, ctk.END)
            self.nome_paciente.insert(0, valores[1])
            self.nome_paciente.configure(state="disabled")
        
        self.cpf_paciente_frame.destroy()

    def lupa_cpf_paciente(self):

        self.cpf_paciente_frame = ctk.CTkFrame(self, width=610, height=415)
        self.cpf_paciente_frame.place(x=270, y= 80)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview", 
                background="#202020",  # Cor de fundo
                foreground="white",    # Cor do texto
                rowheight=25,          # Altura das linhas
                fieldbackground="#202020")  # Cor de fundo do campo
                
        self.cpf_paciente = ttk.Treeview(self.cpf_paciente_frame, columns=("cpf", "paciente"), show="headings", style="Custom.Treeview")
        self.cpf_paciente.pack(fill="both", expand=True)

        # Definir os cabeçalhos das colunas
        self.cpf_paciente.heading("cpf", text="CPF")
        self.cpf_paciente.heading("paciente", text="Paciente")
        
        # Definir o tamanho das colunas
        self.cpf_paciente.column("cpf", anchor="center", width=250)
        self.cpf_paciente.column("paciente", anchor="center", width=358)
        
        # Adicionar dados à tabela
        pacientesCadastrados = self.DbAccess.GetPacientes()

        for pessoas in pacientesCadastrados:
            self.cpf_paciente.insert("", "end", values=pessoas)  

        select_cpf_paciente = ctk.CTkButton(self.cpf_paciente_frame, text = "CONFIRMAR".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command= self.selecionar_cpf_paciente)
        select_cpf_paciente.pack()  
        
    def lupa_remedios(self):

        self.remedio_frame = ctk.CTkFrame(self, width=610, height=415)
        self.remedio_frame.place(x=270, y= 80)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview", 
                background="#202020",  # Cor de fundo
                foreground="white",    # Cor do texto
                rowheight=25,          # Altura das linhas
                fieldbackground="#202020")  # Cor de fundo do campo
                
        self.remedio_paciente = ttk.Treeview(self.remedio_frame, columns=("remedio"), show="headings", style="Custom.Treeview")
        self.remedio_paciente.pack(fill="both", expand=True)

        # Definir os cabeçalhos das colunas
        self.remedio_paciente.heading("remedio", text="REMEDIO")
        
        # Definir o tamanho das colunas
        self.remedio_paciente.column("remedio", anchor="center", width=608)
        
        
        # Adicionar dados à tabela
        remedios = self.DbAccess.GetRemedios()
        for pessoas in remedios:
            self.remedio_paciente.insert("", "end", values=pessoas[0], iid=pessoas[1])  

        select_remedio_paciente = ctk.CTkButton(self.remedio_frame, text = "CONFIRMAR".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command= self.selecionar_remedio)
        select_remedio_paciente.pack() 

    def selecionar_remedio(self):

        self.item_selecionado_remedio = self.remedio_paciente.selection()
        if self.item_selecionado_remedio:
            valores = self.remedio_paciente.item(self.item_selecionado_remedio, 'values')
            
            self.remedio.configure(state="normal")
            self.remedio.delete(0, ctk.END)
            self.remedio.insert(0, valores[0])
            self.remedio.configure(state="disabled")
        
        self.remedio_frame.destroy()

    def agendamentos_ativos(self):

        self.registro_agendamento.place_forget()

        self.agendamento_ativo_frame = ctk.CTkFrame(self, width=610, height=415)
        self.agendamento_ativo_frame.place(x=270, y= 80)
        
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Custom.Treeview", 
                background="#202020",  # Cor de fundo
                foreground="white",    # Cor do texto
                rowheight=25,          # Altura das linhas
                fieldbackground="#202020")  # Cor de fundo do campo
                
        self.agendamento_at = ttk.Treeview(self.agendamento_ativo_frame, columns=("cpf", "nome", "medicamento", "horario"), show="headings", style="Custom.Treeview")
        self.agendamento_at.pack(fill="both", expand=True)

        # Definir os cabeçalhos das colunas
        self.agendamento_at.heading("cpf", text="CPF")
        self.agendamento_at.heading("nome", text="Nome")
        self.agendamento_at.heading("medicamento", text="Medicamento")
        self.agendamento_at.heading("horario", text="Horario")
        
        # Definir o tamanho das colunas
        self.agendamento_at.column("cpf", anchor="center", width=150)
        self.agendamento_at.column("nome", anchor="center", width=154)
        self.agendamento_at.column("medicamento", anchor="center", width=154)
        self.agendamento_at.column("horario", anchor="center", width=150)

        # Adicionar dados à tabela
        dados = self.DbAccess.GetPacientesAtivos( self.cpf_usuario_logado )
        for cpf, nome, medicamento, horario, codremedio in dados:
            self.agendamento_at.insert("", "end", values=(cpf, nome, medicamento, horario, codremedio))

        delet_agendamento_ativo = ctk.CTkButton(self.agendamento_ativo_frame, text = "deletar agendamento selecionado".upper(), fg_color = "Green", hover_color = "#014B05", corner_radius = 15, command= self.excluir_agendamento)
        delet_agendamento_ativo.pack()

    def excluir_agendamento(self):

        selected_item = self.agendamento_at.selection()  # Seleciona o item
        item = self.agendamento_at.item( selected_item[0])['values']
        if selected_item:  # Verifica se há um item selecionado

            cpf_enfermeiro = self.cpf_usuario_logado
            cpf_paciente   = item[0]
            codigo_remedio = item[4]
            dados = [cpf_enfermeiro, cpf_paciente, codigo_remedio]

            sucesso, error = self.DbAccess.delete_agendamento(dados)

            if sucesso:

                messagebox.showinfo(message = "Agendamento exlcuido")
                self.agendamento_at.delete(selected_item)  # Exclui o item

            else:

                messagebox.showerror(message=error)






if __name__ == "__main__":
    app = App_pt2("Iuri", 11246558408)
    app.mainloop()
