from fractions import Fraction
import random

# Zwei feste Brüche
fraction1 = Fraction(1, 2)
fraction2 = Fraction(1, 3)

# Zufällige Auswahl zwischen Addition und Subtraktion
operation = random.choice(['+', '-'])

# Berechne die richtige Antwort basierend auf der zufälligen Operation
if operation == '+':
    correct_answer = fraction1 + fraction2
    operation_text = "Addiere"
else:
    correct_answer = fraction1 - fraction2
    operation_text = "Subtrahiere"

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
