import customtkinter as ctk
import mysql.connector

#conexão com o banco de dados mysql
try:
    conexao = mysql.connector.connect(
        host ='localhost',
        user='root',
        password='Dns158313@',
        database='CRUD'
    )
except mysql.connector.Error as erro:
    print(f"Erro ao tentar conexão com o servidor MySql: {erro}")

def func_inserir():
    #recebe os dados nos campos da tela
    produto = campoProduto.get("1.0", "end-1c")
    preco = campoPreco.get("1.0", "end-1c")
    estoque = campoEstoque.get("1.0", "end-1c")
         
    #envia os dados para o banco de dados mysql
    cursor = conexao.cursor()
    comando_SQL = 'INSERT INTO produtos (produto, preco, estoque) VALUES (%s, %s, %s)'
    dados = (produto, preco, estoque)
    cursor.execute(comando_SQL, dados)
    conexao.commit()
    
    #limpar os dados dos campos
    campoProduto.delete("1.0", "end")
    campoPreco.delete("1.0", "end")
    campoEstoque.delete("1.0", "end")
    
    print('Dados inseridos com Sucesso')

    return                         


janelaPrincipal = ctk.CTk()                                  #Contrução da janela
janelaPrincipal._set_appearance_mode('system')               #Ajusta o Tema da janela ('light', 'dark')
janelaPrincipal.title('Sistema CRUD')                        #Titulo da janela
janelaPrincipal.geometry('800x600')                          #Tamanho padrão da Janela
janelaPrincipal.maxsize(width=900, height=700)               #Tamanho máximo que a janela poderá ser ajustada pelo usuário
janelaPrincipal.minsize(width=800, height=600)               #Tamanho mínimo que a janela poderá ser ajustada pelo usuário
janelaPrincipal.resizable(width=True, height= True)          #bloqueia a ou libera o ajuste da janela pelo usuário

abas=ctk.CTkTabview(master=janelaPrincipal, width=790, height=590, fg_color="gray")
abas.pack()
abas.add('Cadastro')
abas.add('Relatório')
abas.add('Edição')

labelProduto = ctk.CTkLabel(master=abas.tab('Cadastro'),
    text='Produto', text_color='dark blue',
    font=('arial' , 18)
).place(x=20, y=75)

labelPreco = ctk.CTkLabel(master=abas.tab('Cadastro'),
    text='Preço', text_color='dark blue',
    font=('arial' , 18)
).place(x=20, y=135)

labelEstoque = ctk.CTkLabel(master=abas.tab('Cadastro'), 
    text='Estoque', text_color='dark blue', 
    font=('arial' , 18)
).place(x=20, y=195)

campoProduto = ctk.CTkTextbox(master = abas.tab('Cadastro'), 
    width=250, height=20,
    fg_color='white',
    text_color='black',
    font=('arial' , 16)
).place(x=20, y=100)

campoPreco = ctk.CTkTextbox(master = abas.tab('Cadastro'), 
    width=250, height=20,
    fg_color='white',
    text_color='black',
    font=('arial' , 16)
).place(x=20, y=160)

campoEstoque = ctk.CTkTextbox(master = abas.tab('Cadastro'), 
    width=250, height=20,
    fg_color='white', 
    text_color='black',
    font=('arial' , 16)
).place(x=20, y=220)


btnJanelaRelatorio = ctk.CTkButton(master = abas.tab('Cadastro'), text='Salvar Dados', command=func_inserir).place(x=300, y=500)


janelaPrincipal.mainloop()
