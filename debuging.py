import customtkinter as ctk

# Criar a janela principal
janelaPrincipal = ctk.CTk()
janelaPrincipal.geometry("800x600")

# Criar um Frame para as abas
abas = ctk.CTkTabview(master=janelaPrincipal, width=790, height=590)
abas.pack(pady=20, padx=20)

# Adicionar abas
abas.add('Cadastro')
abas.add('Relatório')
abas.add('Edição')

# Criar uma Textbox na aba 'Cadastro'
caixaMensagem = ctk.CTkTextbox(master=abas.tab('Cadastro'), width=250, height=20)
caixaMensagem.pack(pady=10, padx=10)

# Função para imprimir o texto da Textbox
def imprimir_texto():
    texto = caixaMensagem.get("1.0", "end-1c")  # Pega o texto da Textbox
    print(texto)

# Botão para chamar a função imprimir_texto
botao_imprimir = ctk.CTkButton(master=abas.tab('Cadastro'), text="Imprimir Texto", command=imprimir_texto)
botao_imprimir.pack(pady=10)

# Rodar a aplicação
janelaPrincipal.mainloop()
