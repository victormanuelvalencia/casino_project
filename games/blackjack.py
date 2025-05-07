import random
"""
# Calcula el valor de una sola carta
def calculate_hand_value(card, hand):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        # Si al sumar 11 te pasas, el As vale 1
        return 11 if hand + 11 <= 21 else 1
    else:
        return int(card)


# Reparte una carta
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Juego principal
def blackjack(hand=0, turn=0):
    if turn == 0:
        # Primer turno: repartir dos cartas
        card1 = deal_card()
        card2 = deal_card()
        value1 = calculate_hand_value(card1, hand)
        value2 = calculate_hand_value(card2, hand)
        hand = value1 + value2
        print(f"Start: {card1}, value: ({value1}), {card2}, value: ({value2})")
        return blackjack(hand, turn + 1)


    print(f"Your current hand value: {hand}")
    choice = input("Do you want another card? (y/n): ").lower()
    if choice == 'y':
        card = deal_card()
        value = calculate_hand_value(card, hand)
        print(f"Dealt card: {card}, value: {value}")
        hand += value
        if hand > 21:
            print("You went over 21. You lose.")
            return False
        return blackjack(hand, turn + 1) + value

    else:
        return hand

# Ejecutar el juego
print("Result:", blackjack())
"""

import random

# Método para calcular el valor de las cartas
def calculate_hand_value(card, hand):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        # Si al sumar 11 te pasas, el As vale 1
        return 11 if hand + 11 <= 21 else 1
    else:
        return int(card)

# Método para repartir una carta
def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Juego con recursividad de pila de blackjack
def blackjack(hand=0, turn=0, total=0):
    # Repartir las dos cartas iniciales en el primer turno
    if turn == 0:
        card1 = deal_card()
        card2 = deal_card()
        value1 = calculate_hand_value(card1, hand)
        value2 = calculate_hand_value(card2, hand)
        hand += value1 + value2
        total += value1 + value2
        print(f"Start: {card1} ({value1}), {card2} ({value2})")
        return blackjack(hand, turn + 1, total)  # Siguiente turno, pasamos los valores

    # Verificar si el jugador se pasa de 21
    if hand > 21:
        print("You went over 21. You lose.")
        return total  # Regresa el total al final si el jugador se pasa

    # Mostrar el valor actual de la mano
    print(f"Your current hand value: {total}")
    choice = input("Do you want another card? (y/n): ").lower()

    if choice == 'y':
        # Si decide tomar otra carta
        card = deal_card()
        value = calculate_hand_value(card, hand)
        print(f"Dealt card: {card}, value: {value}")

        total += value
        if total > 21:
            print("You went over 21. You lose.")
            return total
        return blackjack(hand, turn + 1, total) + value  # Llamada recursiva, se acumula el valor de la carta

    else:
        # Si decide retirarse, devuelve el valor final de la mano acumulado
        print(f"Final hand value: {total}")
        return total  # Regresa el total final de la mano


print("Result: ", blackjack())
