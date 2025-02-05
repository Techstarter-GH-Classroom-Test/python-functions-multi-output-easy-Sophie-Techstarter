# Aufgabe 1: Schreibe eine Funktion mit dem Namen calc_1()
# die den Durchschnitt und die Anzahl der Elemente einers Arrays mit Zahlen mit return wieder gibt.
def calc_1(array):
    if len(array) == 0:  # Vermeidung der Division durch 0
        return (0, 0)
    else:
        count = len(array)
        average = sum(array) / count
        return (average, count)

# Aufgabe 2: Schreibe eine Funktion mit dem Namen calc_2()
# die zwei Parameter: n und m engegen nimmt mit return n + m und n * m wieder gibt
def calc_2(n, m):
    return (n + m, n * m)
