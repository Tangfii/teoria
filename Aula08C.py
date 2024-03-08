#TRABALHANDO COM MÓDULOS

#As importações no python são como se fossem bibliotecas, cada uma contendo alguma função diferente. Existem as importações do próprio python como a: math, que é um básicamente uma biblioteca matemática no python, quanto a importação: emojis, onde está precisa ser instalada por fora e te dá a capacidade de adicionar emojis no seu códigos.

#Quando eu quiser chamar uma função específica basta eu digitar "import (nome da importação)". Desta maneira todos os objetos que estão dentro desta importação serão utilizados. Se eu quiser pegar apenas 1 objeto de uma importação basta eu digitar a função "from (nome da importação) import (nome do objeto escolhido)"

#Exemplos:
import math
num=int(input("Informe um número: "))
raiz =math.sqrt(num)
print("A raiz de {} é igual a {:.2f}".format (num, raiz))

from math import sqrt, floor
num1=int(input("Informe um número: "))
raiz1=sqrt(num)
print("A raiz de {} é igual a {:.2f}".format (num, floor(raiz)))

#Existem milhares de importações que você pode fazer. o próprio python ja disponibiliza um monte mas você também tem a possibilidade de instalar por fora.