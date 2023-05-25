import unittest
from main import app
from frequent import frequent_word



class FrameworkTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)


    def test_quadratic_equation_one_root(self):
        response = frequent_word('Текст, текст, слово слово текст слово текст!')
        self.assertEqual(response, 'текст')

    def test_quadratic_equation_multy_root(self):
        response = frequent_word('Это длинный текст с повторяющимся словом словом словом')
        self.assertEqual(response, 'словом')

    