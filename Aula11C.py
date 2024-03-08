#CORES NO TERMINAL


#Sempre que você quiser representar uma cor em python vc irá começar com: \033[m], depois determinará quais códigos você irá usar: \033[style ; text ; back ;m]

#Style: é o código do comportamento, o código do estilo. Ex: qual o estilo da fonte? calibri, negrito e etc.

#Text: é o código do texto. Ex: qual a cor do texto?.

#Back: é o código do backgrund, no caso a cor de fundo. Ex: qual a cor do fundo?

#Você não precisa seguir uma ordem na hora de colocar esses códigos, pois eles já têm números específicos. Ex: \033[0;33;44m


#CÓDIGOS


#Existem vários códigos pra Style mas os que funcionam melhor são:
#0: None (Sem estilo nenhum)
#1: Bold (Texto em negrito)
#4: Underline (Texto Sublinhado)
#7: Negative (Inverte as configurações)

#As cores do Text são:
#30: Cinza
#31: Vermelho
#32: Verde
#33: Amarelo
#34: Magenta
#35: Rosa
#36: Ciano
#37: Branco
#OBS: Essas cores citas a cima são as cores que existem dentro do Padrão ANSI. Para obter mais cores você precisará instalar uma biblioteca por fora.

#As cores do Back são as mesmas que do Text, pórem ao invés de 30 usaremos 40:
#40: Cinza
#41: Vermelho
#42: Verde
#43: Amarelo
#44: Magenta
#45: Rosa
#46: Ciano
#47: Branco
#OBS: Para obter mais cores você precisará instalar uma biblioteca por fora.
    

#TESTES

print("\033[0;30;41mTESTE")
print("\033[4;33;46mTESTE")
print("\033[1;35;43mTESTE")
print("\033[30;42mTESTE")
print("\033[mTESTE")
print("\033[7;30mTESTE")


#PRATICANDO


print("\033[7;33;44mOlá, Mundo!\033[m")
#OBS: o \033[m colocado no final do código serve para determinar aonde as cores devem parar/.

a=3
b=5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!".format(a,b))

nome='Arthur'
print("Olá! Muito prazer em te conhecer, {}{}{}!!!".format("\033[4;34m",nome,"\033[m"))

nome1='Arthur'
cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7m'}
print("Olá! Muito prazer em te conhecer {}{}{}.".format(cores['pretoebranco'], nome1, cores['limpa']))