import tkinter as tk
from fractions import Fraction
import random

# Neue Aufgabe generieren
def new_task():
    global fraction1, fraction2, correct_answer

    numerator1 = random.randint(1, 9)
    denominator1 = random.randint(2, 9)
    numerator2 = random.randint(1, 9)
    denominator2 = random.randint(2, 9)

    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    operation = random.choice(["+", "-", "*", "/"])
    if operation == "+":
        correct_answer = fraction1 + fraction2
        task_label.config(text=f"Addiere: {fraction1} + {fraction2}")
    elif operation == "-":
        correct_answer = fraction1 - fraction2
        task_label.config(text=f"Subtrahiere: {fraction1} - {fraction2}")
    elif operation == "*":
        correct_answer = fraction1 * fraction2
        task_label.config(text=f"Multipliziere: {fraction1} * {fraction2}")
    elif operation == "/":
        correct_answer = fraction1 / fraction2
        task_label.config(text=f"Dividiere: {fraction1} : {fraction2}")

    numerator_entry.delete(0, tk.END)
    denominator_entry.delete(0, tk.END)
    result_label.config(text="")

# Antwort überprüfen
def check_answer():
    try:
        user_numerator = int(numerator_entry.get())
        user_denominator = int(denominator_entry.get())

        if user_denominator == 0:
            result_label.config(text="Nenner darf nicht 0 sein!")
            return

        user_answer = Fraction(user_numerator, user_denominator)

        if user_answer == correct_answer:
            result_label.config(text="Richtig!")
        else:
            result_label.config(text=f"Falsch! Richtige Antwort: {correct_answer}")
    except ValueError:
        result_label.config(text="Ungültige Eingabe!")

# GUI-Elemente direkt erstellen
tk.Tk().title("Brüche Quiz")  # Fenster mit Titel erstellen

# Aufgabe anzeigen
task_label = tk.Label(text="Aufgabe erscheint hier...")
task_label.pack()

# Eingabe für Zähler
tk.Label(text="Zähler:").pack()
numerator_entry = tk.Entry()
numerator_entry.pack()

# Eingabe für Nenner
tk.Label(text="Nenner:").pack()
denominator_entry = tk.Entry()
denominator_entry.pack()

# Button zum Überprüfen
tk.Button(text="Antwort überprüfen", command=check_answer).pack()

# Button für neue Aufgabe
tk.Button(text="Neue Aufgabe", command=new_task).pack()

# Ergebnis anzeigen
result_label = tk.Label(text="")
result_label.pack()

# Erste Aufgabe generieren
new_task()

# GUI starten
tk.mainloop()
