import instaloader
import pandas as pd

def loginConta():

    try:
        L = instaloader.Instaloader()

        login=input("Nome de Usuário: ")
        senha=input("Senha do Usuário: ")

        L.login(str(login), str(senha))

        print("Login realizado com sucesso!")

        return login, senha

    except:

        print("Login inválido, tente novamente")

        return login, senha





def extracaoSeguidores(login, senha):

    L = instaloader.Instaloader()

    try:

        L.login(str(login), str(senha))

        perfil = input("Insira o perfil alvo: ")
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

        print("Extração realizado com sucesso")

    except:

        print("Tente Novamente/Refaça o Login")

def postagens(login, senha):

    L = instaloader.Instaloader()

    try:

        L.login(str(login), str(senha))

        perfil = input("Perfil Alvo: ")

        postagens = instaloader.Profile.from_username(L.context, perfil).get_posts()

        for posts in postagens:
            L.download_post(posts, perfil)

        print("Extração realizada com sucesso")

    except:

        print("Tente Novamente/Refaça o Login")

def stories(login, senha):

    L = instaloader.Instaloader()

    try:

        L.login(str(login), str(senha))

        perfil = input("Perfil Alvo: ")

        Id = L.check_profile_id(perfil)

        L.download_stories(userids=[Id], fast_update=True, filename_target=perfil + '-stories')

        print("Extração realizada com sucesso")

    except:

        print("Tente Novamente/Refaça o Login")

opcao = input("1 - Fazer Login \n 2 - Extrair seguidores/seguindo \n 3 - Extrair todos os Posts \n 4 - Extrair Stories \n 0 - Fechar programa \n ")

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
        print("PROGRAMA FINALIZADO")
        break



    opcao = input("1 - Fazer Login \n 2 - Extrair seguidores/seguindo \n 3 - Extrair todos os Posts \n 4 - Extrair Stories \n 0 - Fechar programa \n ")
