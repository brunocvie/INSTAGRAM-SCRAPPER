# INSTAGRAM-SCRAPPER

1 INTRODUÇÃO

Sistema para a extração de dados de contas da rede social INSTAGRAM.

Programa desenvolvido utilizando a linguagem PYTHON e as bibliotecas INSTALOADER e PANDAS.

Link para a página de desenvolvimento:

https://github.com/brunocvie/INSTAGRAM-SCRAPPER

Link para o arquivo executável (.exe):

https://github.com/brunocvie/INSTAGRAM-SCRAPPER/releases/tag/EXECUT%C3%81VEL

Página do projeto INSTALOADER:

https://instaloader.github.io/

Página do projeto PANDAS:

https://pandas.pydata.org/

2 UTILIZAÇÃO

O programa é composto por sete opções:

1 - Fazer login *: Efetuar o login na conta, informar o e-mail vinculado (Ex.: meuemail@meuemail.com), o telefone (Ex: +5548990009999) ou o nome de usuário (não utilizar o arroba @ - Ex.: usuariodoinstagram);

2 - Extrair seguidores: Informar o perfil alvo o qual se pretende extrair os usuários que estão seguindo aquele perfil (Followers), serão todos extraídos para um arquivo .xlsx (EXCEL), o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedeusuario);

3 - Extrair Seguindo: Informar o perfil alvo o qual se pretende extrair os usuário que estão sendo seguidos pelo perfil alvo (Following), serão todos extraídos para um arquivo .xlsx (EXCEL), o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedeusuario);

4 - Extrair todos os Posts: Informar o perfil alvo que se deseja extrair todas as postagens, incluindo imagens e vídeos, o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedousuario), uma pasta com o nome do usuário será criada com as mídias extraídas;

5 - Extrair Stories: Extrair todos os Stories de um perfil alvo, o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedousuario), uma pasta com o nome do usuário “-stories” será criada com as mídias extraídas;
6 - Extrair Highlights: Extrair todos os Highlights (favoritos) de um perfil alvo, o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedeusuario), uma pasta com o nome do usuário “-highligths” será criada com as mídias extraídas;

0 - Encerrar o programa.


* Obs: Se a conta possuir segundo fator de autenticação este deve ser desabilitado, caso contrário não será possível fazer o login no sistema.
** Obs2: A extração dos seguidores (Followers), seguindo (Following), Stories e HighLigths (Favoritos), exigem que seja realizado o login em alguma conta do INSTAGRAM, independente se o perfil é aberto ou fechado (apenas para seguidores).

***Obs3: A extração dos Posts de um perfil não exige que seja feito o LOGIN em uma conta.

3 OUTRAS CONSIDERAÇÕES

O INSTAGRAM, assim como outras redes sociais, possuem mecanismos inteligentes que detectam atividades de extração em massa de dados, pode acontecer que depois de extrair um certo volume de informações o INSTAGRAM bloqueie o perfil utilizado;

A ferramentas apena extrai dados de perfis abertos ou perfis fechados que já foram aceitos como seguidores;

Sugere-se que a extração de todos os POSTS de um perfil aberto seja feita sem a realização de LOGIN em uma conta, se for fechado deve-se realizar o Login (caso seja seguidor);

A extração de Seguidores/Seguindo (Followers/Following) deve ser feita de maneira controlada, pois este tipo de extração é a que mais enseja o bloqueio pela rede social.












