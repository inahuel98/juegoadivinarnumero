num1 = int(input("Participante 1 ingrese su numero: "))
num2 = int(input("Participante 2 ingrese el numero de Participante 1: "))
intentos = 1
if num1 == num2:
    print("Felicitaciones adivinaste el numero del Participante 1 en el intento: ", intentos)
else:
    while num2 != num1:
        if num2 > num1:
            print("el numero del P1 es menor")
        else:
            print("El numero de P1 es mayor")
        num2 = int(input("Participante 2 ingrese su numero: "))
        intentos += 1
        if intentos == 20:
            num1 = num2
    if intentos == 20:
        print("Intentos superados --------GAME OVER--------")
    else:
        print("Felicidades lograste acertar el numero en el intento ", intentos)
