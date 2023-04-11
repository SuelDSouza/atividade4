de combustível gasto usando a fórmula LITROS = DISTANCIA / 12.

- Função para ler e retornar o valor do tempo gasto na viagem (em horas) 
(não recebe parâmetros)

- Função para ler e retornar o valor da velocidade média durante a viagem 
(em Km/h) (não recebe parâmetros)

- Função para calcular e retornar o valor da distância percorrida (recebe como 
parâmetros o tempo gasto e a velocidade média)

- Função para calcular e retornar a quantidade de litros de combustível gastos 
(recebe como parâmetro a distância percorrida)

- Função para exibir o resultado final (recebe como parâmetro a quantidade de 
litros de combustível gastos)

Exemplo de implementação em Python:

```
def ler_tempo():
    tempo = float(input("Informe o tempo gasto na viagem (em horas): "))
    return tempo

def ler_velocidade_media():
    velocidade_media = float(input("Informe a velocidade média durante a viagem (em Km/h): "))
    return velocidade_media

def calcular_distancia(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia

def calcular_litros_gastos(distancia):
    litros_gastos = distancia / 12
    return litros_gastos

def exibir_resultado(litros_gastos):
    print("A quantidade de litros de combustível gastos foi de: ", round(litros_gastos, 2), "litros")

# Programa principal
tempo = ler_tempo()
velocidade_media = ler_velocidade_media()
distancia = calcular_distancia(tempo, velocidade_media)
litros_gastos = calcular_litros_gastos(distancia)
exibir_resultado(litros_gastos)

Exemplo de resultado:

Informe o tempo gasto na viagem (em horas): 3
Informe a velocidade média durante a viagem (em Km/h): 90
A quantidade de litros de combustível gastos foi de:  22.5 litros
Uma possível implementação de função para apresentar o resultado seria:

def apresentar_resultado(tempo, velocidade_media, distancia, litros_gastos):
    print("Tempo gasto na viagem:", tempo, "horas")
    print("Velocidade média durante a viagem:", velocidade_media, "Km/h")
    print("Distância percorrida:", distancia, "Km")
    print("Quantidade de litros de combustível gastos:", round(litros_gastos, 2), "litros")
Essa função recebe como parâmetro os valores calculados ao longo do programa (tempo gasto, velocidade média, distância percorrida e quantidade de litros de combustível gastos) e imprime esses valores de forma formatada e legível para o usuário. 

Exemplo de chamada da função no programa principal:

def main():
    tempo = ler_tempo()
    velocidade_media = ler_velocidade_media()
    distancia = calcular_distancia(tempo, velocidade_media)
    litros_gastos = calcular_litros_gastos(distancia)
    apresentar_resultado(tempo, velocidade_media, distancia, litros_gastos)

if __name__ == "__main__":
    main()
O resultado apresentado ao usuário seria:

Tempo gasto na viagem: 3 horas
Velocidade média durante a viagem: 90 Km/h
Distância percorrida: 270.0 Km
Quantidade de litros de combustível gastos: 22.5 litros