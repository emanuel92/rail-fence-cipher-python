from itertools import cycle

# Inputs
mode = input("Modus - Encrypt (E), Decrypt (D): ")
message = input("Nachricht: ")
rails = int(input("Anzahl Rails: "))


def encode(message, rails):
    # Erstellen eines Grids mit entsprechender Größe
    # z.B. 4x10: [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ...]
    enc = [[" " for i in range(len(message))] for j in range(rails)]

    # Verteilen der Buchstaben
    direction = 0  # Richtung (0 = abwärts / 1 = aufwärts)
    rail = 0  # Zeile/Rail

    for i in range(len(message)):
        enc[rail][i] = message[i]
        if rail == 0:
            direction = 0
        elif rail == rails-1:
            direction = 1
        if direction == 0:
            rail += 1
        else:
            rail -= 1

    # Anzeigen des Grids
    for i in range(rails):
        print("".join(enc[i]))

    # Verschlüsselte Nachricht
    cypherText = []
    for i in range(rails):
        for j in range(len(message)):
            if enc[i][j] != ' ':
                cypherText.append(enc[i][j])

    cipher = "".join(cypherText)
    print("Verschlüsselter Text: ", cipher)


def decode(ciphertext, rails):
    # Erstellen eines Grids mit entsprechender Größe
    r = list(range(rails))
    p = cycle(r + r[-2:0:-1])
    indexes = sorted(range(len(ciphertext)), key=lambda i: next(p))
    result = [''] * len(ciphertext)

    # Verteilen der Buchstaben &
    for i, c in zip(indexes, ciphertext):
        result[i] = c

    cipher = "".join(result)
    print("Entschlüsselter Text: ", cipher)


# Modus
if mode == "D":
    decode(message, rails)
else:
    encode(message, rails)
