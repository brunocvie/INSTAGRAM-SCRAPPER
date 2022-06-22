import tkinter as tk
from tkinter import simpledialog, messagebox
import instaloader
import pandas as pd
from time import sleep

ROOT = tk.Tk()

ROOT.withdraw

class instagramScrapper():

    def __init__(self):

        self.L = instaloader.Instaloader()

    def loginConta(self):

        try:

            login=simpledialog.askstring(title="USUÁRIO", prompt="Usuário")
            senha=simpledialog.askstring(title="SENHA", prompt="Senha", show="*")

            self.L.login(str(login), str(senha))

            messagebox.showinfo(title="ATENÇÃO", message="Login realizado com sucesso")

        except:

            messagebox.showinfo(title="ATENÇÃO", message="LOGIN INCORRETO")

    def extracaoSeguidores(self):

        try:

            self.L.context.do_sleep()

            perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")
            seguidores = instaloader.Profile.from_username(self.L.context, perfil)

            #postagens = []
            followers = []

            ###CAPTURAR SEGUIDORES###
            for seg in seguidores.get_followers():
                followers.append([perfil, seg.username])
                sleep(1)

            df = pd.DataFrame(followers, columns=['Usuário','Seguidores'])

            with pd.ExcelWriter(perfil + "Seguidores" + ".xlsx") as writer:
                df.to_excel(writer, index=False)

            messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

        except:

            messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

    def extracaoSeguindo(self):

        try:

            self.L.context.do_sleep()

            perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")
            seguindo = instaloader.Profile.from_username(self.L.context, perfil)

            #postagens = []
            followees = []

            ###CAPTURAR SEGUINDO###
            for seg in seguindo.get_followees():
                followees.append([perfil, seg.username])
                sleep(1)

            df1 = pd.DataFrame(followees, columns=['Usuário', 'Seguindo'])

            with pd.ExcelWriter(perfil + "Seguindo" + ".xlsx") as writer:
                df1.to_excel(writer, index=False)

            messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

        except:

            messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

    def postagens(self):

        try:

            self.L.context.do_sleep()

            perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")

            postagens = instaloader.Profile.from_username(self.L.context, perfil).get_posts()

            for posts in postagens:
                self.L.download_post(posts, perfil)

            messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

        except:

            messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

    def stories(self):

        try:

            self.L.context.do_sleep()

            perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")

            Id = self.L.check_profile_id(perfil)

            self.L.download_stories(userids=[Id], fast_update=True, filename_target=perfil + '-stories')

            messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

        except:

            messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

    def favoritos(self):

        try:

            self.L.context.do_sleep()

            perfil = simpledialog.askstring(title="PERFIL", prompt="Perfil Alvo")

            Id = self.L.check_profile_id(perfil)

            self.L.download_highlights(Id, fast_update=True, filename_target=perfil + '-highlights')

            messagebox.showinfo(title="ATENÇÃO", message="Extração realizada com sucesso")

        except:

            messagebox.showinfo(title="ATENÇÃO", message="Tente Novamente/Refaça o Login")

scrapper = instagramScrapper()

opcao = simpledialog.askstring(title="Escolha uma opção:", prompt=" 1 - Fazer Login \n 2 - Extrair Seguidores \n 3 - Extrair Seguindo \n 4 - Extrair todos os Posts \n 5 - Extrair Stories \n 6 - Extrair Highlights \n 0 - Fechar programa \n ")

while(int(opcao) < 7 or opcao != 0):

    if (int(opcao) == 1):

        scrapper.loginConta()

    elif int(opcao) == 2:

        scrapper.extracaoSeguidores()

    elif int(opcao) == 3:

        scrapper.extracaoSeguindo()

    elif int(opcao) == 4:
        scrapper.postagens()

    elif int(opcao) == 5:
        scrapper.stories()

    elif int(opcao) == 6:
        scrapper.favoritos()

    elif int(opcao) == 0:
        messagebox.showinfo(title="ENCERRANDO", message="PROGRAMA FINALIZADO")
        break



    opcao = simpledialog.askstring(title="Escolha uma opção:", prompt=" 1 - Fazer Login \n 2 - Extrair Seguidores \n 3 - Extrair Seguindo \n 4 - Extrair todos os Posts \n 5 - Extrair Stories \n 6 - Extrair Highlights \n 0 - Fechar programa \n ")
