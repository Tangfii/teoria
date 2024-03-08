#NESTA AULA, VAMOS APRENDER COMO FUNCIONAM OS TIPOS PRIMITIVOS NO PYTHON E AS PECULIARIDADES DO INT(), FLOAT(), BOOL() E STR(). Além de uma outra forma de usar o comando print


#O comando int serve para reconhecer números interos 
#EX: 1, 0, -1, 36783
varivael0 = int(input('Informe um número: '))
variavel1= int(input('Informe outro número: '))
a= variavel1+variavel1
print('A soma do valor {} com o valor {} foi de {}'.format (varivael0,variavel1,a))
#O comando float serve para reconhecer números reais(ponto flutuantes)
#EX: 2.3, 0.076, -15.543, 1.0
variavel = float(input('Informe um valor: '))


#O comando bool serve para reconhecer valores lógicos(booleanos)
#O comando bool só reconhece 2 valores os "True" e "False"
#OBS: na hora de digitar os valores True ou False, eles precisam sempre começar com a primeira letra maiúscula


#O comando str serve para reconhecer valores caractere(strings), que nada mais é que uma palavra 
#EX: 'olá', '5' e ''
n1=int(input('Informe um valor: '))
print(type(n1))



#Outra forma de usar o comando print:
print('A soma vale {}'. format(s))
