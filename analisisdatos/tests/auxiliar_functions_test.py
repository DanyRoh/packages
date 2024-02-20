import unittest
from paquets.analisisdatos.main.auxilar_functions import is_url


if __name__ == '__main__':
    unittest.main()

class Test_is_url(unittest.TestCase):
    def test_is_url_passed(self):
        result = is_url("https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv")
        self.assertEqual(result, True)

    def test_is_url_failed(self):
        result = is_url("xxx")
        self.assertEqual(result, False)




