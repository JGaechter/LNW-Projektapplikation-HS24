from fractions import Fraction
import random

# Funktion zur Generierung von zwei zufälligen Brüchen
def generate_fractions():
    numerator1 = random.randint(1, 9)
    denominator1 = random.randint(2, 9)  # Vermeidet Nenner 1
    numerator2 = random.randint(1, 9)
    denominator2 = random.randint(2, 9)  # Vermeidet Nenner 1
    return Fraction(numerator1, denominator1), Fraction(numerator2, denominator2)

# Zufällige Brüche generieren
fraction1, fraction2 = generate_fractions()

# Zufällige Auswahl zwischen Addition, Subtraktion, Multiplikation und Division
operation = random.choice(['+', '-', '*', '/'])

# Berechne die richtige Antwort basierend auf der zufälligen Operation
if operation == '+':
    correct_answer = fraction1 + fraction2
    operation_text = "Addiere"
elif operation == '-':
    correct_answer = fraction1 - fraction2
    operation_text = "Subtrahiere"
elif operation == '*':
    correct_answer = fraction1 * fraction2
    operation_text = "Multipliziere"
else:  # Division
    correct_answer = fraction1 / fraction2
    operation_text = "Dividiere"
    operation = ":"  # Zeige das Divisionszeichen als ":" an

# Schüler auffordern, ihre Lösung einzugeben
print(operation_text + " die Brüche " + str(fraction1) + " " + operation + " " + str(fraction2))
user_numerator = int(input("Gib den Zähler deiner Lösung ein: "))
user_denominator = int(input("Gib den Nenner deiner Lösung ein: "))

# Antwort des Schülers als Bruch interpretieren
user_answer = Fraction(user_numerator, user_denominator)

# Überprüfen, ob die Antwort korrekt ist
if user_answer == correct_answer:
    print("Richtig!")
else:
    print("Falsch! Die richtige Antwort ist " + str(correct_answer) + ".")
