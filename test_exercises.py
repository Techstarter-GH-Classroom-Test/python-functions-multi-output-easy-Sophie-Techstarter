# test_exercises.py

import unittest
import exercises

class TestExercises(unittest.TestCase):

    def test_calc_1(self):
        # Test mit einem nicht-leeren Array
        result = exercises.calc_1([1, 2, 3, 4, 5])
        self.assertEqual(result, (3.0, 5), "Fehler: calc_1 gibt nicht den richtigen Durchschnitt und die Anzahl zurück.")
        
        # Test mit einem leeren Array
        result = exercises.calc_1([])
        self.assertIsNone(result, "Fehler: calc_1 sollte None zurückgeben, wenn das Array leer ist.")
    
    def test_calc_2(self):
        # Test mit positiven Zahlen
        result = exercises.calc_2(3, 5)
        self.assertEqual(result, (8, 15), "Fehler: calc_2 gibt nicht die korrekten Ergebnisse für Addition und Multiplikation zurück.")
        
        # Test mit einer negativen und einer positiven Zahl
        result = exercises.calc_2(-3, 5)
        self.assertEqual(result, (2, -15), "Fehler: calc_2 gibt nicht die korrekten Ergebnisse für negative Zahlen.")
        
        # Test mit Null
        result = exercises.calc_2(0, 5)
        self.assertEqual(result, (5, 0), "Fehler: calc_2 gibt nicht die korrekten Ergebnisse bei Verwendung von Null.")

if __name__ == '__main__':
    unittest.main()
