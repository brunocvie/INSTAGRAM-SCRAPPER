import tkinter as tk
from tkinter import simpledialog, messagebox
import instaloader
import pandas as pd

ROOT = tk.Tk()

ROOT.withdraw


def loginConta():

    try:
        L = instaloader.Instaloader()

        login=simpledialog.askstring(title="USUÁRIO", prompt="Usuário")
        senha=simpledialog.askstring(title="SENHA", prompt="Senha")

        L.login(str(login), str(senha))

        messagebox.showinfo(title="ATENÇÃO", message="Login realizado com sucesso")

        return login, senha

    except:

        messagebox.showinfo(title="ATENÇÃO", message="LOGIN INCORRETO")

        return login, senha





def extracaoSeguidores(login, senha):

    L = instaloader.Instaloader()

    try:

        L.login(str(login), str(senha))

        perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")
        seguidores = instaloader.Profile.from_username(L.context, perfil)
        seguindo = instaloader.Profile.from_username(L.context, perfil)

        #postagens = []
        followers = []
        followees = []


        ###CAPTURAR SEGUIDORES###
        for seg in seguidores.get_followers():
            followers.append([perfil, seg.username])
        ###CAPTURAR SEGUINDO###
        for seg in seguindo.get_followees():
            followees.append([perfil, seg.username])

        df = pd.DataFrame(followers, columns=['Usuário','Seguidores'])
        df1 = pd.DataFrame(followees, columns=['Usuário', 'Seguindo'])

        with pd.ExcelWriter(perfil + "Seguidores" + ".xlsx") as writer:
            df.to_excel(writer, index=False)

        with pd.ExcelWriter(perfil + "Seguindo" + ".xlsx") as writer:
            df1.to_excel(writer, index=False)

        messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

    except:

        messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

def postagens(login, senha):

    L = instaloader.Instaloader()

    try:

        L.login(str(login), str(senha))

        perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")

        postagens = instaloader.Profile.from_username(L.context, perfil).get_posts()

        for posts in postagens:
            L.download_post(posts, perfil)

        messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

    except:

        messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

def stories(login, senha):

    L = instaloader.Instaloader()

    try:

        L.login(str(login), str(senha))

        perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")

        Id = L.check_profile_id(perfil)

        L.download_stories(userids=[Id], fast_update=True, filename_target=perfil + '-stories')

        messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

    except:

        messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

opcao = simpledialog.askstring(title="Escolha uma opção:", prompt="1 - Fazer Login \n 2 - Extrair seguidores/seguindo \n 3 - Extrair todos os Posts \n 4 - Extrair Stories \n 0 - Fechar programa \n ")

while(int(opcao) < 4 or opcao != 0):

    if (int(opcao) == 1):
        login, senha = loginConta()
    elif int(opcao) == 2:
        extracaoSeguidores(login, senha)
    elif int(opcao) == 3:
        postagens(login, senha)

    elif int(opcao) == 4:
        stories(login, senha)

    elif int(opcao) == 0:
        messagebox.showinfo(title="ENCERRANDO", message="PROGRAMA FINALIZADO")
        break



    opcao = simpledialog.askstring(title="Escolha uma opção:", prompt="1 - Fazer Login \n 2 - Extrair seguidores/seguindo \n 3 - Extrair todos os Posts \n 4 - Extrair Stories \n 0 - Fechar programa \n ")
