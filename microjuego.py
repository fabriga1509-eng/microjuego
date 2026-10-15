import random

def jugar():
    nombres = []
    for i in range(1, 5):
        nombre = input(f"Nombre del jugador {i}: ").strip() or f"Jugador {i}"
        nombres.append(nombre)

    secreto = random.randint(1, 100)
    max_rondas = 5
    intentos = {n: 0 for n in nombres}

    print("\n=== ADIVINA EL NÚMERO (4 JUGADORES) ===")
    print(f"Número entre 1 y 100. Cada uno tiene {max_rondas} intentos.\n")

    for ronda in range(1, max_rondas + 1):
        print(f"--- Ronda {ronda}/{max_rondas} ---")
        for nombre in nombres:
            while True:
                entrada = input(f"{nombre}: ")
                if entrada.isdigit():
                    break
                print("Escribe un número válido.")

            numero = int(entrada)
            intentos[nombre] += 1

            if numero == secreto:
                print(f"\ ¡{nombre} ganó! Era el {secreto} (intento {intentos[nombre]}).")
                return
            print("Más alto " if numero < secreto else "Más bajo ")
        print()

    print(f"Nadie lo logró. Era el {secreto}.")

while True:
    jugar()
    if input("\n¿Jugar de nuevo? (s/n): ").lower() != "s":
        print("¡Hasta la próxima!")
        break