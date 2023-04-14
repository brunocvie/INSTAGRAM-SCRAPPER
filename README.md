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

O programa é composto por oito opções:

1 - Fazer login *: Efetuar o login na conta, a sessão será iniciada através dos cookies criados ao fazer login na conta do INSTAGRAM utilizando o navegador Mozilla/Firefox, ou seja, antes de fazer login no programa é necessário logar a conta no FIREFOX (irá funcionar apenas no FIREFOX, por enquanto...);

2 - Extrair seguidores: Informar o perfil alvo o qual se pretende extrair os usuários que estão seguindo aquele perfil (Followers), serão todos extraídos para um arquivo .xlsx (EXCEL), o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedeusuario); *

3 - Extrair Seguindo: Informar o perfil alvo o qual se pretende extrair os usuário que estão sendo seguidos pelo perfil alvo (Following), serão todos extraídos para um arquivo .xlsx (EXCEL), o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedeusuario); *

4 - Extrair todos os Posts: Informar o perfil alvo que se deseja extrair todas as postagens, incluindo imagens e vídeos, o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedousuario), uma pasta com o nome do usuário será criada com as mídias extraídas;

5 - Extrair Stories: Extrair todos os Stories de um perfil alvo, o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedousuario), uma pasta com o nome do usuário “-stories” será criada com as mídias extraídas;

6 - Extrair Highlights: Extrair todos os Highlights (favoritos) de um perfil alvo, o nome de usuário do perfil alvo deve ser informado SEM o arroba @ (Ex.: nomedeusuario), uma pasta com o nome do usuário “-highligths” será criada com as mídias extraídas;

7 - Extrair um Post específico: Com esta funcionalidade será possível baixar apenas as informações de uma única publicação, como a mídia e os comentário, estes serão salvos em uma planilha .XLSX. Será necessário informar o link da postagem;

0 - Encerrar o programa.


** Obs: A extração dos seguidores (Followers), seguindo (Following), Stories, HighLigths (Favoritos) e Posts específicos, exigem que seja realizado o login em alguma conta do INSTAGRAM, independente se o perfil é aberto ou fechado (apenas para seguidores).

***Obs2: Para cada usuário salvo em uma lista de seguidores ou seguindo o programa demora 1 segundo, para evitar bloqueios por parte da plataforma.

3 OUTRAS CONSIDERAÇÕES

O INSTAGRAM, assim como outras redes sociais, possuem mecanismos inteligentes que detectam atividades de extração em massa de dados, pode acontecer que depois de extrair um certo volume de informações o INSTAGRAM bloqueie o perfil utilizado;

A ferramentas apena extrai dados de perfis abertos ou perfis fechados que já foram aceitos como seguidores;

A extração de Seguidores/Seguindo (Followers/Following) deve ser feita de maneira controlada, pois este tipo de extração é a que mais enseja o bloqueio pela rede social.

*** ENGLISH VERSION ***

1. INTRODUCTION

System for extracting data from accounts of the social network INSTAGRAM.

Program developed using the PYTHON language, INSTALOADER and PANDAS libraries.

Link to development page:

https://github.com/brunocvie/INSTAGRAM-SCRAPPER

Link to the executable file (.exe):

https://github.com/brunocvie/INSTAGRAM-SCRAPPER/releases/tag/EXECUT%C3%81VEL

INSTALOADER project page:

https://instaloader.github.io/

PANDAS project page:

https://pandas.pydata.org/

2 USE

The program consists of eight options:

1 - Log in *: Log in to the account, the session will be initiated through the cookies created when logging in to the INSTAGRAM account using the Mozilla/Firefox browser, before logging in to the program, it is necessary to log in to the FIREFOX account (will only work in FIREFOX, for now...);

2 - Extract followers: Inform the target profile from which you intend to extract the users who are following that profile (Followers), they will all be extracted to an .xlsx file (EXCEL), the username of the target profile must be informed WITHOUT the at sign @ (Ex.: username); *

3 - Extract Following: Inform the target profile from which you intend to extract the users who are being followed by the target profile (Following), they will all be extracted to an .xlsx file (EXCEL), the username of the target profile must be informed WITHOUT the @ sign (Ex.: username); *

4 - Extract all Posts: Inform the target profile that you want to extract all posts, including images and videos, the username of the target profile must be informed WITHOUT the @ sign (Ex.: username), a folder with the name will be created with the extracted media;

5 - Extract Stories: Extract all Stories from a target profile, the username of the target profile must be informed WITHOUT the @ at sign (Ex.: username), a folder with the username “-stories” will be created with the extracted media;

6 - Extract Highlights: Extract all Highlights (favorites) of a target profile, the username of the target profile must be informed WITHOUT the @ at sign (Ex.: username), a folder with the username “-highligths” will be created with the extracted media;

7 - Extract a specific Post: With this functionality it will be possible to download only the information of a single publication, such as the media and the comments, these will be saved in an .XLSX spreadsheet. It will be necessary to inform the link of the post;

0 - Terminate the program.

** Note: The extraction of followers, following, Stories, HighLights and specific Posts, requires that you log in to an INSTAGRAM account, regardless of whether the profile is open or closed (only for followers).

***Note 2: For each user saved in a list of followers or following the program, it takes 1 second, to avoid blocks by the platform.

3 OTHER CONSIDERATIONS

INSTAGRAM, like other social networks, has intelligent mechanisms that detect mass data extraction activities. It may happen that after extracting a certain amount of information, INSTAGRAM blocks the profile used;

The tool only extracts data from open profiles or closed profiles that have already been accepted as followers;

The extraction of Followers/Following (Followers/Following) must be done in a controlled manner, as this type of extraction is the one that most leads to blocking by the social network.












