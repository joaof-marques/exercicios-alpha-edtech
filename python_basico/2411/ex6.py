import moduloTeste
#Nessa linha de código nós importamos um arquivo python chamado moduloTeste, e isso é a mesma coisa de dar um ctrl+c e ctrl+v de todo o código desse arquivo nesse projeto atual
#A diferença acontece quando você precisa utilizar as funções deste módulo. Como estamos importando o pacote inteiro, precisamos primeiro dizer de qual pacote estamos pegando algo para depois dizer qual é o item que está sendo pego

moduloTeste.imprimirNumerosPares()
#Nessa linha estamos acessando a função imprimirNumerosPares do moduloTeste

#Porém, podemos importar as funções diretamente para o programa, sem precisar importar o pacote todo
from moduloTeste import imprimirNumerosImpares()

#Nesse caso estamos importando somente a função imprimirNumerosImpares do moduloTeste. E como estamos pegando um item específico, não precisamos nem dizer de qual pacote ele veio:
imprimirNumerosImpares()

#Desta maneira podemos também importar todas as funções de um módulo sem precisar ficar definindo uma a uma
#Fazemos da seguinte maneira:
from moduloTeste import *
#O * significa all. Então, a leitura ficaria importe tudo do pacote moduloTeste

#E depois disso, todas as funções podem ser acessadas diretamente:
imprimirNumerosPares()
imprimirNumerosImpares()

#Porém, existem riscos ao se fazer isso. Quando utilizamos o * estamos importando tudo que está presente no pacote, podendo trazer variáveis globais, informações do pacote em si e todos os nomes definidos em um módulo.
#Então é necessário ter cautela ao utilizar esse método de importação