import random

def jugar():
    secreto = random.randint(1, 100)
    intentos = 0
    max_intentos = 7

    print("=== ADIVINA EL NÚMERO ===")
    print(f"Pensé un número entre 1 y 100. Tienes {max_intentos} intentos.\n")

    while intentos < max_intentos:
        entrada = input(f"Intento {intentos + 1}/{max_intentos}: ")

        if not entrada.isdigit():
            print("Escribe un número válido.\n")
            continue

        numero = int(entrada)
        intentos += 1

        if numero < secreto:
            print("Más alto ⬆\n")
        elif numero > secreto:
            print("Más bajo ⬇\n")
        else:
            print(f"¡Correcto! Lo lograste en {intentos} intentos.")
            return

    print(f"Se acabaron los intentos. Era el {secreto}.")

while True:
    jugar()
    if input("\n¿Jugar de nuevo? (s/n): ").lower() != "s":
        print("¡Hasta la próxima!")
        break