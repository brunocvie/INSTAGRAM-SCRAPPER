import instaloader
import pandas as pd
#import tkinter
#from tkinter import simpledialog



def loginConta():

    login=input("LOGIN = ")
    senha=input("DIGITE A SENHA = ")

    print("Login realizado com sucesso.")

    return login, senha



def extracaoSeguidores(login, senha):

    L = instaloader.Instaloader()

    L.login(str(login), str(senha))

    perfil = input("Escreva o nome do usuário do perfil alvo: ")
    #posts = instaloader.Profile.from_username(L.context, perfil).get_posts()
    seguidores = instaloader.Profile.from_username(L.context, perfil)
    seguindo = instaloader.Profile.from_username(L.context, perfil)

    #postagens = []
    followers = []
    followees = []

    ###CAPTURAR ÚLTIMA POSTAGENS###

    #for post in posts:
    #    print(post.caption)
    #    postagens.append(post.caption)

    #df = pd.DataFrame(postagens, columns=['Postagem'])

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

def postagens(login, senha):

    L = instaloader.Instaloader()

    L.login(str(login), str(senha))

    perfil = input("Escreva o nome do usuário do pefil alvo: ")

    postagens = instaloader.Profile.from_username(L.context, perfil).get_posts()

    for posts in postagens:
        L.download_post(posts, perfil)


opcao = input("Escolha uma opção: \n 1 - Fazer Login \n 2 - Extrair seguidores/seguindo \n 3 - Extrair todos os Posts \n 0 - Fechar programa \n ")

while(int(opcao) < 4 or opcao != 0):

    if (int(opcao) == 1):
        login, senha = loginConta()
    elif int(opcao) == 2:
        extracaoSeguidores(login, senha)
    elif int(opcao) == 3:
        postagens(login, senha)
    elif int(opcao) == 0:
        print("programa encerrado")
        exit()



    opcao = input("Escolha uma opção: \n 1 - Fazer Login \n 2 - Extrair seguidores/seguindo \n 3 - Extrair todos os Posts \n 0 - Fechar programa \n")






#root = tkinter.Tk()
#root.withdraw()
#perfil = simpledialog.askstring("USUÁRIO", "Nome de usuário")
#root.destroy()
