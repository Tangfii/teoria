#Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

#Basicamente aprenderemos "se"(if) e "senão"(else). If e Else são como opções que daremos pra quem está executando nosso programa.

#Exemplo: um carro precisa chegar a determinado ponto, existem 2 caminhos que este carro pode percorrer, esquerdo e o direito, o caminho esquerdo é o mais longo, já o caminho direito é o mais curso, SE o carro decidir escolher o caminho esquerdo ele chegará em 40 min ao seu destino SENÃO ele irá pelo caminho direito e levará 30 min para chegar em seu destino.

#Tanto o caminho esquerdo quando o direto são comandos que precisam ser feitos.

#Outro exemplo: 
carro=int(input("Informe quantos anos têm seu carro: "))
if carro <=3:
    print("Carro Novo")
else:
    print("Carro Velho")

#OU

carro1=int(input("Informe quantos anos têm seu carro: "))
print("Carro Novo" if carro <=3 else"Carro Velho")    

#PRATICANDO


n=str(input("Qual é seu nome? "))
if n == "Arthur":
    print("Que belo nome você tem!")
print("Prazer em te conhecer {}".format(n))


n1=float(input("Informe sua primeira nota: "))
n2=float(input("Informe sua segunda nota: "))
m=(n1+n2)/2
print("Sua média é de {:.1f}". format(m))
if m>=6.0:
    print("Sua média foi boa, PARABÉNS!")
else:
    print("Sua média não foi tão boa, estude mais!")