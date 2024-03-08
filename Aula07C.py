#Operadores Aritméticos

#Ordem de Precedência
#1: ()
#2: **
#3: *  /  //  %
#4: +  -

#Exemplos:

print(5+3*2)
#O * vem primeiro que o +

print(3*5+4**2)
#O ** vem primeiro que o *

print(3*(5+4)**2)
#A presença dos () fazem com que a conta que esteja ali dentro tenha a prioridade.

##

n=input("Informe seu nome: ")
print("Prazer em conhecer {:20}!".format (n))
#Sempre que colocarmos : em seguida de um número fará com que o programa aumente o número de espaços. 
#Ex {:20} +20 caractérias

#Podemos também determinar a ordem onde as caractérias vão aparecer.
#Ex: para direita{:>} , para esquerda{:<} , centralizado {:^}
n=input("Informe seu nome: ")
print("Prazer em conhecer {:>20}!".format (n))

#Qualquer coisa que colocarmos antes do : que não sejam números, substituiram os espaços.
#Ex: {:=^20}
n=input("Informe seu nome: ")
print("Prazer em conhecer {:=^20}!".format (n))

#Assim como podemos aumentar o número de espaços em uma resposta, também podem diminui-lo
#Ex: {: .3f} O número dentro é o máximo de espaços que esta programação mostrará
n1=int(input("Informe um valor: "))
n2=int(input("Informe outro valor: "))
a=n1+n2
s=n1-n2
m=n1*n2
d=n1/n2
di=n1//n2
p=n1%n2

print("A soma dos valos são= {}, \na subtração= {}, \na multiplicação= {}, \na divisão= {:.3f}, \na divisão inteira= {} \ne a potência= {}".format (a, s, m, d, di, p))

#Já estes \n servem para quebrar as linhas. Porém se eu quiser que está linha não quebre  eu uso comando   end=' '
#Ex: 
print("A soma dos valos são= {}, a subtração= {}, a multiplicação= {}, a divisão= {:.3f}, a divisão inteira= {} e a potência= {}".format (a, s, m, d, di, p), end=" ") 