
#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase="Curso em Video Python"
#Cada uma dessas letras são caracteries que ficam amarzenados no computador, todos eles têm uma númeração que sempre começara de 0, o seja o c de curso é a caractere 0 e o n de python é a 20 (obs os espaços também contam como uma caractere).


print(frase[9])
# O exemplo acima mostra que eu posso escolher qual caractere eu desejo selecionar, neste caso foi a nona caractere.
#Existe outros jeitos de escolher uma caracatere

print(frase[9:13])
#Desta maneira o python irá pegar mais de uma caractere, ele pegará do 9 até o 12, o 13 não será lido, neste caso a frase ficaria "vide".

print(frase[1:13:2])
#Desta maneira o python irá fazer da mesma forma feita no exemplo a cima, com a diferença que irá pular de 2 em 2 caracteres, então a frase ficaria "VdoPto"

print(frase[:5])
#Desta maneira o python começara a ler a frase desde o início até a 4 caractere (lembrando que o python sempre descarta a ultíma caractere) então a frase ficaria: "Curs"

print(frase[15:])
#Desta meneira o python vai começar dá caractere 15 e ir até a último, então a frase ficaria: "Python"


#ANÁLISE

print(len(frase))
#len significa comprimento, então se eu pedir len da frase será a mesma coisa de pedir o comprimento da frase.

print(frase.count('o'))

#Este comando irá contar a quantidade de letras O que existem nesta frase. 
#OBS: os valores podem mudar se as letras estivem maiúsculas ou minúsculas, ou python só selecionará os O minúsculos.

print(frase.count('o',0,13))
#O programa só pegará as quantidades de O do 0 ao 12

print(frase.find('deo')) 
#Deste modo o python irá procurar a frase que você digitou e irá indicar suas posições.

print('Curso' in frase)
#Isso é meio que uma pergunta que você faz ao python, "Existe a palavra Curno em frase?", se existir o programa informara  True, se não False


#TRANSFORMAÇÃO

print(frase.replace("Python", "Android"))
#replace significa reposicionar, ou seja a palavra Python será substituida pela palavra Android.

print(frase.upper())
#upper significa para cima. Este comando deixara todas as letras que são minúsculas em maiúculas.

print(frase.lower())
#O lower é o contrário do upper, ou seja oque está em maiúculo será tranformando em minúsculo.

print(frase.capitalize())
#Está função tranformar todas as caracteres em minúsculas menos a primeira, no caso a 0.

print(frase.title())
#Está função é basicamente a função capitalize com a diferença que ao invés de colocar a primeira caractere em maiúsculo e o resto minúsculo a função title tranforma todas as primeiras letras das palavras em maiúculas.


frase1=("   Aprenda Python  ")
#Mudamos a frase para fazer sentido apatir de agora

print(frase1.strip())
#Serve parar tirar todos os espaços inúteis do começo e no final da frase.

print(frase1.rstrip())
#Este R adicionado na strip serve para indicar o lado direito da palavra, ou seja, os espaços que seram excluídos serão apenas do dá direita.

print(frase1.lstrip())
#Este l serve para indicar o lado esquerdo, ou seja, os espaços que serão excluídos serão apenas do lado esquerdo.


#DIVISÃO

print(frase.split())
#O split basicamente causará uma divisão na frase, fazendo com que as numerações se repitam, formando uma nova lista pra cada palavra que iram ter numerações.

print('-'.join(frase))
#Está função irá fazer uma junção de todas as palavras, exluindo os espaços, também podemos colocar aspas e algo que queremos que seja colocado depois de cada caractere.


print("""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa""")

#Se por acaso eu queria escrever um texto longo e preservar seus parágrafos, eu apenas adiciono 3 aspas duplas no começo e no final do texto.