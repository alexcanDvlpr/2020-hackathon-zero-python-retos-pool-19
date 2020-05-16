import random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    message = ''
    if player.lower() == 'piedra':
        if ai.lower() == player.lower():
            message = 'Empate!'
        elif ai.lower() == 'papel':
            message = 'Perdiste!'
        else:
            message = 'Ganaste!'
    elif player.lower() == 'tijeras':
        if ai.lower() == player.lower():
            message = 'Empate!'
        elif ai.lower() == 'piedra':
            message = 'Perdiste!'
        else:
            message = 'Ganaste!'
    elif player.lower() == 'papel':
        if ai.lower() == player.lower():
            message = 'Empate!'
        elif ai.lower() == 'tijeras':
            message = 'Perdiste!'
        else:
            message = 'Ganaste!'
    return message

# Entry Point
def Game():
    # Titulo del programa y las elecciones que tenemos activas.
    print('Esto es el piedra, papel, tijeras')

    # Pedimos al usuario el input
    userOption = input('¿Cual es tu eleccion?  [Piedra, Papel o Tijeras] \n')
    aiOption = random.choice(options)

    # Mostramos que ha elegido cada jugador
    print('Tu has elegido: ' + userOption)
    print('La IA ha elegido: ' + aiOption)
    print('\n')
    
    winner = quienGana(userOption, aiOption)

    print(winner)
