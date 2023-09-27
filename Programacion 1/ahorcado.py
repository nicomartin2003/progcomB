import random

def choose_word():
    words = ["python", "programacion", "pneumonoultramicroscopicsilicovolcanoconiosis", "hipopotomonstrosesquipedaliofobia", "electroencefalografista"]
    return random.choice(words)

def display_board(word, guessed_letters):
    board = ""
    for letter in word:
        if letter in guessed_letters:
            board += letter
        else:
            board += "_"
    return board

def play():
    word = choose_word()
    attempts = 6
    guessed_letters = []
    user_letters = [] 
    
    print("¡Bienvenido al juego de ahorcado!")
    
    while True:
        print("\nPalabra a adivinar: " + display_board(word, guessed_letters))
        print("Letras introducidas: {}".format(', '.join(user_letters)))  
        letter = input("Ingresa una letra: ").lower()
        
        if letter in user_letters:
            print("Ya has introducido esa letra.")
        elif letter in guessed_letters:
            print("Ya adivinaste esa letra.")
        elif letter in word:
            guessed_letters.append(letter)
            user_letters.append(letter)  
            if display_board(word, guessed_letters) == word:
                print("\n¡Felicidades! ¡Has adivinado la palabra: " + word + "!")
                break
        else:
            user_letters.append(letter) 
            attempts -= 1
            print("\nLetra incorrecta. Te quedan {} intentos.".format(attempts))
            
            if attempts == 0:
                print("¡Perdiste! La palabra era: " + word)
                break

if __name__ == "__main__":
    play()
