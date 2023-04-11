def ler_temperatura():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura

def converter_para_fahrenheit(temp_celsius):
    temp_fahrenheit = (9*temp_celsius + 160)/5
    return temp_fahrenheit


def mostrar_resultado(temp_fahrenheit):
    print("A temperatura em Fahrenheit é:", temp_fahrenheit)