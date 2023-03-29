// Questao 1
"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);


// Resposta : 91
"""


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Questao 2
"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""
//Resposta:

def pertence_fibo(num):
    seq_fibo = [0, 1]
    contador = 0
    while num >= seq_fibo[contador]:
        if seq_fibo[contador] == num:
            return True
        seq_fibo.append(seq_fibo[contador] + seq_fibo[contador + 1])
        contador += 1
    return False
    
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Questao 3

""" 
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2, 10, 12, 16, 17, 18, 19, ____


//Resposta: 9, 128, 49, 100, 13, ?? Não sei

"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Questao 4

"""
4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.


//Resposta: Pegadinha. O caminhão estará mais perto, pois como ele está indo em direção a Ribeirão Preto, e o carro em direção à ele,
//ao passar pelo carro, ele automaticamente estará mais próximo a Ribeirão Preto.
"""

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Questao 5

"""
5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""
//Resposta:

def inverte_string(string):
    string = list(string)
    contador_ini = 0
    contador_fim = len(string) - 1
    while contador_ini != contador_fim and (contador_ini - 1) != contador_fim:
        temp = string[contador_ini]
        string[contador_ini] = string[contador_fim]
        string[contador_fim] = temp
        contador_ini += 1
        contador_fim -= 1

    return f'String invertida: {"".join(string)}'








    
    
    
