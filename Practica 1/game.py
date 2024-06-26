import random

# Lista de palabras posibles
words = ["python", "programacion", "computadora", "codigo", "desarrollo", 
"inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_fails = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)

#Elegir dificultad
difficulty = int(input('Ingrese la dificultad (1:facil, 2:medio, 3:dificil): '))
match difficulty:
    case 1:
        guessed_letters = ['a','e','i','o','u']
        letters = []
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case 2:
        word_displayed = secret_word[0]+'_' * (len(secret_word) - 2)+secret_word[-1]
        print("Importante: las letras mostradas pueden repetirse")
    case 3:
        word_displayed = "_" * len(secret_word)

# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

#Bucle principal de juego
while(True):

    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    #Verifica que no se haya ingresado vacio
    if not letter or len(letter)>1:
        print('ERROR: el caracter ingresado no es valido')
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta y 
    if letter in (secret_word):
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        max_fails -= 1
        if max_fails == 0:
            print('¡Oh no! Has agotado tus intentos.')
            print(f"La palabra secreta era: {secret_word}")
            break
        print(f'Te quedan {max_fails}')

    # Mostrar la palabra parcialmente adivinada
    letters = []
    if(difficulty == 2):
        letters.append(secret_word[0])
        for letter in secret_word[1:-1]:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        letters.append(secret_word[-1])
    else:
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")